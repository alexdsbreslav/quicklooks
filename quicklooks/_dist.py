"""Distribution plot function for quicklooks."""

from __future__ import annotations

from typing import Any, Optional, Union

import matplotlib.pyplot as plt  # type: ignore
import numpy as np
import pandas as pd  # type: ignore
import seaborn as sns  # type: ignore

from ._chart import Chart
from ._colors import resolve_color
from ._config import VALID_DIST_TYPES
from ._types import DistResult
from ._validation import validate_1d_array, validate_chart, validate_option


def dist(
    chart: Chart,
    *,
    data: Any,
    color: Union[str, tuple, list] = "default",
    dist_type: str = "binned_counts",
    auto_fit: bool = True,
    distribution_min_max: tuple = (None, None),
    bin_interval: Optional[float] = None,
    opacity: float = 1,
    label: str = "",
    layer_order: int = 1,
) -> DistResult:
    """Add a distribution (histogram or density) plot to a chart.

    Args:
        chart: Chart object created by ``ql.chart()``.
        data: 1D array of values to plot.
        color: Color name from the chart's color library, or a 3-tuple.
        dist_type: Distribution type.
        auto_fit: If ``True``, automatically compute axis limits, bins, and
            ticks from the data and print the settings used.
        distribution_min_max: Tuple of (min, max) for manual bin range.
            Used when *auto_fit* is ``False``.
        bin_interval: Bin width for histogram types. Used when *auto_fit*
            is ``False``.
        opacity: Alpha transparency (0 to 1).
        label: Label for the legend.
        layer_order: Z-order layer (higher = on top).

    Returns:
        A ``DistResult`` with references to the matplotlib artists.
    """
    _fn = "dist"

    # -- validation ------------------------------------------------------------
    validate_chart(chart, _fn)

    if chart.xaxis_type == "timeseries":
        raise ValueError(
            f"ql.{_fn}() error: distribution plots are not compatible with "
            f"timeseries x-axes.\n\n"
            f"Use xtick_labels=\"default\" in ql.chart() for distribution plots."
        )

    validate_1d_array(data, "data", _fn)
    validate_option(dist_type, VALID_DIST_TYPES, "dist_type", _fn)

    data = pd.Series(data)

    # -- resolve color ---------------------------------------------------------
    _, line_c, _ = resolve_color(chart.color_library, color, _fn)

    # -- auto-fit mode ---------------------------------------------------------
    bins = None
    interval = None

    if auto_fit:
        bins, interval = _auto_fit_bins(chart, data, dist_type, _fn)
    elif dist_type in ("binned_density", "binned_counts"):
        if distribution_min_max[0] is None or distribution_min_max[1] is None:
            raise ValueError(
                f"ql.{_fn}() error: when auto_fit=False and dist_type is "
                f"\"binned_counts\" or \"binned_density\", you must provide "
                f"distribution_min_max as a (min, max) tuple."
            )
        if bin_interval is None:
            raise ValueError(
                f"ql.{_fn}() error: when auto_fit=False and dist_type is "
                f"\"binned_counts\" or \"binned_density\", you must provide "
                f"bin_interval."
            )
        bins = np.arange(
            distribution_min_max[0],
            distribution_min_max[1] + bin_interval,
            bin_interval,
        )

    # -- check for excessive ticks ---------------------------------------------
    if chart.ax.get_xticks().shape[0] > 20:
        raise RuntimeError(
            f"ql.{_fn}() error: too many x-axis ticks "
            f"({chart.ax.get_xticks().shape[0]}).\n\n"
            f"Increase xtick_interval in ql.chart() or adjust your data range."
        )
    if chart.ax.get_yticks().shape[0] > 20:
        raise RuntimeError(
            f"ql.{_fn}() error: too many y-axis ticks "
            f"({chart.ax.get_yticks().shape[0]}).\n\n"
            f"Increase ytick_interval in ql.chart() or adjust your data range."
        )

    # -- plot ------------------------------------------------------------------
    if dist_type == "smooth_density":
        clip = (
            chart.ax.get_xlim() if auto_fit
            else distribution_min_max
        )
        dist_artist = sns.kdeplot(
            data, fill=True, linewidth=0, color=line_c,
            clip=clip, alpha=opacity, ax=chart.ax,
            zorder=3, label=label,
        )
    else:
        dist_artist = chart.ax.hist(
            data, bins=bins, alpha=opacity, rwidth=0.85,
            color=line_c, density=(dist_type == "binned_density"),
            linewidth=0, label=label, zorder=3, joinstyle="round",
        )

    # -- print auto-fit info ---------------------------------------------------
    if auto_fit:
        print(
            "auto_fit is on.\n"
            "Review the automatic settings below and update your code with "
            "appropriate values.\n"
            "We recommend setting auto_fit=False after updating your code.\n\n"
            f"Suggested ql.chart() settings:\n"
            f"  x_min_max = {chart.ax.get_xlim()}\n"
            f"  y_min_max = {chart.ax.get_ylim()}\n"
            f"  xtick_interval = "
            f"{chart.ax.get_xticks()[1] - chart.ax.get_xticks()[0]}\n"
            f"  ytick_interval = {chart.ax.get_yticks()[1]}\n\n"
            f"Suggested ql.dist() settings:\n"
            f"  distribution_min_max = {chart.ax.get_xlim()}\n"
            f"  bin_interval = {interval}\n"
        )

    return DistResult(distribution=dist_artist)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _auto_fit_bins(
    chart: Chart,
    data: pd.Series,
    dist_type: str,
    func_name: str,
) -> tuple:
    """Compute bins and axis limits automatically from *data*. Returns (bins, interval)."""
    data_range = np.max(data) - np.min(data)

    if data_range >= 10:
        plt.xlim(np.floor(np.min(data)), np.ceil(np.max(data)))
        interval = 1
        bins = np.arange(
            np.floor(np.min(data)),
            np.ceil(np.max(data)) + 1,
            interval,
        )
        while bins.shape[0] >= 15:
            interval += 1
            bins = np.arange(
                np.floor(np.min(data)),
                np.ceil(np.max(data)) + 1,
                interval,
            )
    else:
        intervals = [0.5, 0.25, 0.2, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.00001]
        decimals = [2, 2, 2, 2, 2, 3, 3, 4, 4, 5]
        i = 0
        interval = intervals[i]
        d = decimals[i]

        def _floor(val: float, dec: int) -> float:
            return np.floor(val * 10**dec) / 10**dec

        def _ceil(val: float, dec: int) -> float:
            return np.ceil(val * 10**dec) / 10**dec

        bins = np.arange(
            _floor(np.min(data), d),
            _ceil(np.max(data), d) + interval,
            interval,
        )
        while bins.shape[0] < 10 and i < len(intervals) - 1:
            i += 1
            interval = intervals[i]
            d = decimals[i]
            bins = np.arange(
                _floor(np.min(data), d),
                _ceil(np.max(data), d) + interval,
                interval,
            )

        plt.xlim(
            _floor(np.min(data), d),
            _ceil(np.max(data), d) + interval,
        )

    # -- set y-limits based on binned data -------------------------------------
    binned_data = pd.cut(data, bins=bins).value_counts()
    if dist_type in ("binned_density", "smooth_density"):
        plt.ylim(0, binned_data.max() / (binned_data.sum() * interval))
    elif dist_type == "binned_counts":
        plt.ylim(0, np.ceil(binned_data.max()))

    # -- set x-ticks to bin edges, reduce if too many --------------------------
    xticks = bins
    plt.xticks(xticks)
    tick_step = 1
    while chart.ax.get_xticks().shape[0] > 10:
        tick_step += 1
        plt.xticks(xticks[::tick_step])

    chart.ax.yaxis.set_major_locator(plt.MaxNLocator(5))

    return bins, interval
