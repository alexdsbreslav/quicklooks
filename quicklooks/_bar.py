"""Bar plot function for quicklooks."""

from __future__ import annotations

from typing import Any, Optional, Union

import matplotlib.pyplot as plt  # type: ignore
import numpy as np

from ._chart import Chart
from ._colors import resolve_color
from ._types import BarResult
from ._validation import (
    validate_1d_array,
    validate_chart,
    validate_matching_shapes,
    validate_optional_1d_array,
    validate_type,
)


def bar(
    chart: Chart,
    *,
    xlabels: Any,
    y: Any,
    color: Union[str, tuple, list] = "default",
    yerror: Optional[Any] = None,
    bars_per_group: int = 1,
    bar_index: int = 0,
    opacity: float = 1,
    label: str = "",
    layer_order: int = 1,
) -> BarResult:
    """Add bars to a chart.

    For grouped bars, call ``ql.bar()`` once per group with the same
    *xlabels* and *bars_per_group*, incrementing *bar_index* each time.

    Args:
        chart: Chart object created by ``ql.chart()``.
        xlabels: 1D array of category labels.
        y: 1D array of bar heights (same length as *xlabels*).
        color: Color name from the chart's color library, or a 3-tuple.
        yerror: Optional 1D array of y-error magnitudes.
        bars_per_group: Total number of bars at each x-label.
        bar_index: Zero-based index of this bar within the group.
        opacity: Alpha transparency (0 to 1).
        label: Label for the legend.
        layer_order: Z-order layer (higher = on top).

    Returns:
        A ``BarResult`` with references to the matplotlib artists.
    """
    _fn = "bar"

    # -- validation ------------------------------------------------------------
    validate_chart(chart, _fn)

    if chart.xaxis_type == "timeseries":
        raise ValueError(
            f"ql.{_fn}() error: bar plots are not compatible with timeseries "
            f"x-axes.\n\nUse xtick_labels=\"default\" in ql.chart() for bar plots."
        )

    validate_1d_array(xlabels, "xlabels", _fn)
    validate_1d_array(y, "y", _fn)
    validate_matching_shapes(xlabels, y, "xlabels", "y", _fn)
    validate_optional_1d_array(yerror, "yerror", _fn)

    if not isinstance(bars_per_group, int) or bars_per_group < 1:
        raise TypeError(
            f"ql.{_fn}() error: 'bars_per_group' must be a positive integer.\n\n"
            f"Received: {bars_per_group!r}"
        )
    if not isinstance(bar_index, int):
        raise TypeError(
            f"ql.{_fn}() error: 'bar_index' must be an integer.\n\n"
            f"Received: {type(bar_index).__name__} = {bar_index!r}"
        )
    if bar_index < 0 or bar_index >= bars_per_group:
        raise IndexError(
            f"ql.{_fn}() error: 'bar_index' ({bar_index}) is out of range.\n\n"
            f"With bars_per_group={bars_per_group}, bar_index must be "
            f"between 0 and {bars_per_group - 1}."
        )

    # -- resolve color ---------------------------------------------------------
    fill_c, line_c, edge_c = resolve_color(chart.color_library, color, _fn)

    # -- compute bar positions -------------------------------------------------
    n_labels = len(xlabels)
    xlim = (-0.5, n_labels - 0.5)
    plt.xlim(xlim[0], xlim[1])
    plt.xticks(ticks=range(n_labels), labels=xlabels)

    label_to_x = dict(zip(xlabels, chart.ax.get_xticks()))

    width = 0.8 if n_labels <= 2 else 0.8 - (n_labels * 0.01)
    width = width / bars_per_group

    idx = list(range(bars_per_group))
    bar_offsets = [(i - np.median(idx)) * 1.1 for i in idx]
    offset = bar_offsets[bar_index] * width

    ylim = chart.ax.get_ylim()
    x_loc = [label_to_x[lbl] + offset for lbl in xlabels]

    y_arr = np.asarray(y, dtype=float)
    bottom = np.array([
        (v / abs(v)) * ((ylim[1] - ylim[0]) * 0.002) if v != 0 else 0
        for v in y_arr
    ])
    height = y_arr - bottom

    # -- draw bars -------------------------------------------------------------
    bar_artist = chart.ax.bar(
        x=x_loc, width=width, height=height, bottom=bottom,
        color=line_c, edgecolor=edge_c, linewidth=2,
        joinstyle="round", alpha=opacity, label=label,
        zorder=layer_order + 2,
    )

    # -- error whiskers --------------------------------------------------------
    if yerror is not None:
        total_bars = bars_per_group * n_labels
        if total_bars >= 30:
            err_width = 2
        elif total_bars >= 20:
            err_width = 3
        elif total_bars >= 10:
            err_width = 4
        else:
            err_width = 5

        yerror_arr = np.asarray(yerror, dtype=float)
        for i in range(n_labels):
            chart.ax.plot(
                np.full(10, x_loc[i]),
                np.linspace(y_arr[i] - yerror_arr[i], y_arr[i] + yerror_arr[i], 10),
                linewidth=err_width, color=edge_c, alpha=opacity,
                zorder=layer_order + 2.1, solid_capstyle="round",
            )

    return BarResult(bars=bar_artist, xlim=xlim)
