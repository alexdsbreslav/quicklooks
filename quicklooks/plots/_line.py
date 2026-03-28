"""Line plot function for quicklooks."""

from __future__ import annotations

from typing import Any, Optional, Union

import numpy as np
import pandas as pd  # type: ignore

from .._chart import Chart, _end_label_right_of_anchor
from .._colors import resolve_color
from .._config import VALID_LINESTYLES, VALID_MARKERS
from .._styling import get_marker_size
from .._types import LineResult
from .._validators import (
    validate_1d_array,
    validate_chart,
    validate_matching_shapes,
    validate_option,
    validate_optional_1d_array,
)


def line(
    chart: Chart,
    *,
    x: Any,
    y: Any,
    color: Union[str, tuple, list] = "default",
    yerror: Optional[Any] = None,
    linewidth: Union[int, float] = 3,
    linestyle: str = "solid",
    marker: Optional[str] = None,
    opacity: float = 1,
    label: str = "",
    end_label: bool = True,
    layer_order: int = 1,
) -> LineResult:
    """Add a line to a chart.

    Args:
        chart: Chart object created by ``ql.chart()``.
        x: 1D array of x-axis values.
        y: 1D array of y-axis values (same length as *x*).
        color: Color name from the chart's color library, or a 3-tuple.
        yerror: Optional 1D array of y-error magnitudes (same length as *x*).
        linewidth: Line width in points.
        linestyle: Line style.
        marker: Marker shape, or ``None`` for no markers.
        opacity: Alpha transparency (0 to 1).
        label: Label for the legend.
        end_label: If ``True``, draw the label text at the end of the line.
        layer_order: Z-order layer (higher = on top).

    Returns:
        A ``LineResult`` with references to the matplotlib artists.
    """
    _fn = "line"

    # -- validation ------------------------------------------------------------
    validate_chart(chart, _fn)
    validate_1d_array(x, "x", _fn)
    validate_1d_array(y, "y", _fn)
    validate_matching_shapes(x, y, "x", "y", _fn)
    validate_optional_1d_array(yerror, "yerror", _fn)
    validate_option(linestyle, VALID_LINESTYLES, "linestyle", _fn)
    validate_option(marker, VALID_MARKERS, "marker", _fn)

    # -- resolve color ---------------------------------------------------------
    fill_c, line_c, edge_c = resolve_color(chart.color_library, color, _fn)

    # -- marker sizing ---------------------------------------------------------
    markersize, markeredgewidth = get_marker_size(chart.size, marker)

    # -- y-error fill ----------------------------------------------------------
    fill_artist = None
    upper_artist = None
    lower_artist = None

    if yerror is not None:
        fill_alpha = 0.6 if fill_c == "#000000" else 0.8
        fill_artist = chart.ax.fill_between(
            x, y - yerror, y + yerror,
            color=fill_c, label=None, alpha=fill_alpha,
            zorder=layer_order + 2,
        )
        upper_artist = chart.ax.plot(
            x, y + yerror,
            linewidth=0.5, color=edge_c, label=None,
            zorder=layer_order + 2,
        )
        lower_artist = chart.ax.plot(
            x, y - yerror,
            linewidth=0.5, color=edge_c, label=None,
            zorder=layer_order + 2,
        )

    # -- main line -------------------------------------------------------------
    line_artist = chart.ax.plot(
        x, y,
        linewidth=linewidth, linestyle=linestyle, color=line_c,
        marker=marker, markersize=markersize,
        markeredgecolor=edge_c, markeredgewidth=markeredgewidth,
        alpha=opacity, label=label, solid_capstyle="round",
        zorder=layer_order + 2,
    )

    # -- end label -------------------------------------------------------------
    if end_label and label:
        x_end = x.iloc[-1] if isinstance(x, pd.Series) else x[-1]
        y_end = y.iloc[-1] if isinstance(y, pd.Series) else y[-1]
        _end_label_right_of_anchor(
            chart,
            x_anchor=x_end,
            y=y_end,
            text=label,
            color=line_c,
            zorder=layer_order + 2,
        )

    return LineResult(
        line=line_artist,
        fill=fill_artist,
        upper=upper_artist,
        lower=lower_artist,
    )
