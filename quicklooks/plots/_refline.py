"""Reference line function for quicklooks."""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any, Optional, Union

import numpy as np
import pandas as pd  # type: ignore

from .._chart import Chart
from .._colors import resolve_color
from .._config import VALID_LINESTYLES, VALID_MARKERS, VALID_REFLINE_DIRECTIONS
from .._styling import get_marker_size
from .._types import RefLineResult
from .._validators import validate_chart, validate_option


def refline(
    chart: Chart,
    *,
    direction: str = "horizontal",
    location: Any = 0,
    color: Union[str, tuple, list] = "gray",
    linewidth: Union[int, float] = 2,
    linestyle: str = "dashed",
    marker: Optional[str] = None,
    opacity: float = 1,
    label: str = "",
    end_label: bool = False,
    layer_order: int = 1,
) -> RefLineResult:
    """Add a reference line to a chart.

    Args:
        chart: Chart object created by ``ql.chart()``.
        direction: Line direction.
        location: Position on the relevant axis. Ignored for diagonal
            directions. For timeseries x-axes, pass a ``"YYYY-MM-DD"`` string.
        color: Color name from the chart's color library, or a 3-tuple.
        linewidth: Line width in points.
        linestyle: Line style.
        marker: Marker shape, or ``None`` for no markers.
        opacity: Alpha transparency (0 to 1).
        label: Label for the legend.
        end_label: If ``True``, draw the label text at the end of the line
            instead of (or in addition to) using a legend entry.
        layer_order: Z-order layer (higher = on top).

    Returns:
        A ``RefLineResult`` with a reference to the matplotlib artist.
    """
    _fn = "refline"

    # -- validation ------------------------------------------------------------
    validate_chart(chart, _fn)
    validate_option(direction, VALID_REFLINE_DIRECTIONS, "direction", _fn)
    validate_option(linestyle, VALID_LINESTYLES, "linestyle", _fn)
    validate_option(marker, VALID_MARKERS, "marker", _fn)

    # -- resolve color ---------------------------------------------------------
    _, line_c, edge_c = resolve_color(chart.color_library, color, _fn)

    # -- marker sizing ---------------------------------------------------------
    markersize, markeredgewidth = get_marker_size(chart.size, marker)

    # -- compute x, y arrays ---------------------------------------------------
    n_points = 10
    parsed_location = location  # may be updated for timeseries vertical lines

    if direction == "horizontal":
        if chart.xaxis_type == "timeseries":
            x = pd.date_range(
                chart.x_min_max[0], chart.x_min_max[1], periods=n_points,
            )
        else:
            x = np.linspace(chart.x_min_max[0], chart.x_min_max[1], n_points)
        y = np.full(n_points, location)

    elif direction == "vertical":
        parsed_location = location
        if chart.xaxis_type == "timeseries":
            if isinstance(parsed_location, str):
                parsed_location = datetime.strptime(parsed_location, "%Y-%m-%d")
            else:
                raise TypeError(
                    f"ql.{_fn}() error: when the chart uses a timeseries x-axis, "
                    f"'location' must be a date string in \"YYYY-MM-DD\" format.\n\n"
                    f"Received: {type(parsed_location).__name__} = {parsed_location!r}"
                )
        x = np.full(n_points, parsed_location)
        y = np.linspace(chart.y_min_max[0], chart.y_min_max[1], n_points)

    elif direction == "diagonal_up":
        x = np.linspace(chart.x_min_max[0], chart.x_min_max[1], n_points)
        y = np.linspace(chart.y_min_max[0], chart.y_min_max[1], n_points)

    else:  # diagonal_down
        x = np.linspace(chart.x_min_max[0], chart.x_min_max[1], n_points)
        y = np.linspace(chart.y_min_max[1], chart.y_min_max[0], n_points)

    # -- draw line -------------------------------------------------------------
    line_artist = chart.ax.plot(
        x, y,
        linewidth=linewidth, linestyle=linestyle, color=line_c,
        marker=marker, markersize=markersize,
        mec=edge_c, mew=markeredgewidth,
        alpha=opacity, label=label,
        zorder=layer_order + 2,
    )

    # -- end label -------------------------------------------------------------
    if end_label and label:
        yrange = chart.y_min_max[1] - chart.y_min_max[0]

        if direction == "horizontal":
            if chart.xaxis_type == "timeseries":
                x_loc = x[-1] + timedelta(days=chart.xrange * 0.01)
            else:
                x_loc = x[-1] + chart.xrange * 0.01
            y_loc = location
            ha, va = "left", "center"

        elif direction == "vertical":
            x_loc = parsed_location
            y_loc = chart.y_min_max[1] + yrange * 0.01
            ha, va = "center", "bottom"

        else:  # diagonal_up / diagonal_down — label at the right end
            if chart.xaxis_type == "timeseries":
                x_loc = x[-1] + timedelta(days=chart.xrange * 0.01)
            else:
                x_loc = x[-1] + chart.xrange * 0.01
            y_loc = y[-1]
            ha, va = "left", "center"

        chart.ax.text(
            x_loc, y_loc, label,
            fontproperties=chart.font_style.label,
            horizontalalignment=ha,
            verticalalignment=va,
            size=chart.font_style.size.l,
            color=line_c,
            zorder=layer_order + 2,
        )

    return RefLineResult(line=line_artist)
