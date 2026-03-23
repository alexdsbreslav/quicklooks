"""Stacked bar plot function for quicklooks."""

from __future__ import annotations

from typing import Any, Union

import matplotlib.pyplot as plt  # type: ignore
import numpy as np

from .._chart import Chart
from .._colors import resolve_color
from .._types import StackedBarResult
from .._validators import (
    validate_1d_array,
    validate_chart,
    validate_matching_shapes,
    validate_type,
)


def stacked_bar(
    chart: Chart,
    *,
    xlabels: Any,
    y: Any,
    color: Union[str, tuple, list] = "default",
    opacity: float = 1,
    label: str = "",
    layer_order: int = 1,
) -> StackedBarResult:
    """Add a segment to a stacked bar chart.

    Positive values stack upward and negative values stack downward, each on
    independent baselines tracked on the chart object. Mixed-sign series are
    split and drawn correctly on both sides.

    The baselines reset whenever ``ql.chart()`` is called, so ``ql.chart()``
    and all ``ql.stacked_bar()`` calls must always be in the same cell.

    Args:
        chart: Chart object created by ``ql.chart()``.
        xlabels: 1D array of category labels (must be the same for every call
            on the same chart).
        y: 1D array of segment heights for this series (same length as
            *xlabels*).
        color: Color name from the chart's color library, or a 3-tuple.
        opacity: Alpha transparency (0 to 1).
        label: Label for the legend.
        layer_order: Z-order layer (higher = on top).

    Returns:
        A ``StackedBarResult`` with references to the matplotlib artists.
    """
    _fn = "stacked_bar"

    # -- validation ------------------------------------------------------------
    validate_chart(chart, _fn)

    if chart.xaxis_type == "timeseries":
        raise ValueError(
            f"ql.{_fn}() error: stacked bar plots are not compatible with "
            f"timeseries x-axes.\n\nUse xtick_labels=\"default\" in ql.chart()."
        )

    validate_1d_array(xlabels, "xlabels", _fn)
    validate_1d_array(y, "y", _fn)
    validate_matching_shapes(xlabels, y, "xlabels", "y", _fn)

    y_arr = np.asarray(y, dtype=float)
    n_labels = len(xlabels)

    # -- x positions and bar width ---------------------------------------------
    xlim = (-0.5, n_labels - 0.5)
    plt.xlim(xlim[0], xlim[1])
    plt.xticks(ticks=range(n_labels), labels=xlabels)

    x_loc = list(chart.ax.get_xticks())
    width = 0.8 if n_labels <= 2 else 0.8 - (n_labels * 0.01)

    # -- diverging baselines (lazily initialised on first call) ----------------
    if not hasattr(chart, "_sbar_baseline_pos"):
        chart._sbar_baseline_pos = np.zeros(n_labels)
    if not hasattr(chart, "_sbar_baseline_neg"):
        chart._sbar_baseline_neg = np.zeros(n_labels)

    y_pos = np.maximum(y_arr, 0)
    y_neg = np.minimum(y_arr, 0)

    pos_baseline = chart._sbar_baseline_pos.copy()
    neg_baseline = chart._sbar_baseline_neg.copy()

    # -- resolve color ---------------------------------------------------------
    _, line_c, edge_c = resolve_color(chart.color_library, color, _fn)

    # -- draw bars -------------------------------------------------------------
    bar_artist = None
    _label = label

    if np.any(y_pos > 0):
        bar_artist = chart.ax.bar(
            x=x_loc, height=y_pos, bottom=pos_baseline,
            width=width, color=line_c, edgecolor=edge_c, linewidth=2,
            joinstyle="round", alpha=opacity, label=_label,
            zorder=layer_order + 2,
        )
        _label = None

    if np.any(y_neg < 0):
        neg_artist = chart.ax.bar(
            x=x_loc, height=y_neg, bottom=neg_baseline,
            width=width, color=line_c, edgecolor=edge_c, linewidth=2,
            joinstyle="round", alpha=opacity, label=_label,
            zorder=layer_order + 2,
        )
        if bar_artist is None:
            bar_artist = neg_artist

    # -- advance baselines -----------------------------------------------------
    chart._sbar_baseline_pos = pos_baseline + y_pos
    chart._sbar_baseline_neg = neg_baseline + y_neg

    return StackedBarResult(bars=bar_artist, xlim=xlim)
