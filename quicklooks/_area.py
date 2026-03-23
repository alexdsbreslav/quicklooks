"""Stacked area plot function for quicklooks."""

from __future__ import annotations

from datetime import timedelta
from typing import Any, Union

import numpy as np
import pandas as pd  # type: ignore

from ._chart import Chart
from ._colors import resolve_color
from ._types import AreaResult
from ._validation import (
    validate_1d_array,
    validate_chart,
    validate_matching_shapes,
)


def area(
    chart: Chart,
    *,
    x: Any,
    y: Any,
    color: Union[str, tuple, list] = "default",
    linewidth: Union[int, float] = 2,
    opacity: float = 0.8,
    label: str = "",
    end_label: bool = True,
    layer_order: int = 1,
) -> AreaResult:
    """Add a filled area band to a chart, stacking automatically on prior bands.

    Positive values stack upward from zero; negative values stack downward,
    each tracked on independent baselines. A series with mixed signs is split
    and drawn correctly on both sides. All-positive data behaves identically
    to a single-baseline implementation.

    The baselines reset whenever ``ql.chart()`` is called, so ``ql.chart()``
    and all ``ql.area()`` calls must always be in the same cell.

    Args:
        chart: Chart object created by ``ql.chart()``.
        x: 1D array of x-axis values.
        y: 1D array of y values for this band (the height of this band, not
            the cumulative total).
        color: Color name from the chart's color library, or a 3-tuple.
        linewidth: Width of the top-edge line.
        opacity: Alpha transparency for the filled area (0 to 1).
        label: Label for the legend. The legend entry shows the top-edge line
            color (darker) rather than the fill color.
        end_label: If ``True``, draw the label at the right end of the band,
            vertically centered within the band.
        layer_order: Z-order layer (higher = on top).

    Returns:
        An ``AreaResult`` with references to the matplotlib artists.
    """
    _fn = "area"

    # -- validation ------------------------------------------------------------
    validate_chart(chart, _fn)
    validate_1d_array(x, "x", _fn)
    validate_1d_array(y, "y", _fn)
    validate_matching_shapes(x, y, "x", "y", _fn)

    y_arr = np.nan_to_num(np.asarray(y, dtype=float))

    # -- diverging baselines (lazily initialised on first call) ----------------
    if not hasattr(chart, "_area_baseline_pos"):
        chart._area_baseline_pos = np.zeros(len(y_arr))
    if not hasattr(chart, "_area_baseline_neg"):
        chart._area_baseline_neg = np.zeros(len(y_arr))

    y_pos = np.maximum(y_arr, 0)
    y_neg = np.minimum(y_arr, 0)

    pos_bottom = chart._area_baseline_pos.copy()
    neg_bottom = chart._area_baseline_neg.copy()
    pos_top = pos_bottom + y_pos
    neg_top = neg_bottom + y_neg

    chart._area_baseline_pos = pos_top.copy()
    chart._area_baseline_neg = neg_top.copy()

    has_pos = np.any(y_pos > 0)
    has_neg = np.any(y_neg < 0)

    # -- resolve color ---------------------------------------------------------
    fill_c, line_c, _ = resolve_color(chart.color_library, color, _fn)

    # -- filled areas ----------------------------------------------------------
    fill_artist = None
    if has_pos:
        fill_artist = chart.ax.fill_between(
            x, pos_bottom, pos_top,
            color=fill_c, alpha=opacity, label=None,
            zorder=layer_order + 2,
        )
    if has_neg:
        fill_neg = chart.ax.fill_between(
            x, neg_top, neg_bottom,
            color=fill_c, alpha=opacity, label=None,
            zorder=layer_order + 2,
        )
        if fill_artist is None:
            fill_artist = fill_neg

    # -- top/bottom edge lines -------------------------------------------------
    # Use NaN where the series has no contribution so matplotlib draws a gap
    # rather than a misleading connecting line across zero.
    line_artist = None
    _label = label  # consume label on first line drawn to avoid double entries

    if has_pos:
        pos_line = np.where(y_arr > 0, pos_top, np.nan)
        line_artist = chart.ax.plot(
            x, pos_line,
            linewidth=linewidth, color=line_c,
            solid_capstyle="round", label=_label,
            zorder=layer_order + 3,
        )
        _label = None

    if has_neg:
        neg_line = np.where(y_arr < 0, neg_top, np.nan)
        neg_line_artist = chart.ax.plot(
            x, neg_line,
            linewidth=linewidth, color=line_c,
            solid_capstyle="round", label=_label,
            zorder=layer_order + 3,
        )
        if line_artist is None:
            line_artist = neg_line_artist

    # -- end label -------------------------------------------------------------
    if end_label and label:
        x_end = x.iloc[-1] if isinstance(x, pd.Series) else np.asarray(x)[-1]

        last_y = y_arr[-1]
        if last_y >= 0:
            y_mid = (pos_bottom[-1] + pos_top[-1]) / 2
        else:
            y_mid = (neg_bottom[-1] + neg_top[-1]) / 2

        if chart.xaxis_type == "timeseries":
            x_loc = x_end + timedelta(days=chart.xrange * 0.01)
        else:
            x_loc = x_end + chart.xrange * 0.01

        chart.ax.text(
            x_loc, y_mid, label,
            fontproperties=chart.font_style.label,
            horizontalalignment="left",
            verticalalignment="center",
            size=chart.font_style.size.l,
            color=line_c,
            zorder=layer_order + 3,
        )

    return AreaResult(fill=fill_artist, line=line_artist)
