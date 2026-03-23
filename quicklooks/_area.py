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

    Each call stacks on top of any previous ``ql.area()`` calls on the same
    chart. The baseline is tracked on the chart object and resets whenever
    ``ql.chart()`` is called. Always call ``ql.chart()`` in the same cell as
    all ``ql.area()`` calls to ensure a clean baseline on every run.

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

    # -- stacking baseline (lazily initialised on first call) ------------------
    if not hasattr(chart, "_area_baseline"):
        chart._area_baseline = np.zeros(len(y_arr))

    y_bottom_arr = chart._area_baseline
    y_top_arr = y_bottom_arr + y_arr
    chart._area_baseline = y_top_arr.copy()

    # -- resolve color ---------------------------------------------------------
    fill_c, line_c, _ = resolve_color(chart.color_library, color, _fn)

    # -- filled area -----------------------------------------------------------
    fill_artist = chart.ax.fill_between(
        x, y_bottom_arr, y_top_arr,
        color=fill_c, alpha=opacity, label=None,
        zorder=layer_order + 2,
    )

    # -- top edge line (carries the label so the legend shows the darker color)
    line_artist = chart.ax.plot(
        x, y_top_arr,
        linewidth=linewidth, color=line_c,
        solid_capstyle="round", label=label,
        zorder=layer_order + 3,
    )

    # -- end label -------------------------------------------------------------
    if end_label and label:
        x_end = x.iloc[-1] if isinstance(x, pd.Series) else np.asarray(x)[-1]
        y_mid = (y_bottom_arr[-1] + y_top_arr[-1]) / 2

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
