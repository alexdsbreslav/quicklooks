"""Scatter plot function for quicklooks."""

from __future__ import annotations

from typing import Any, Optional, Union

import matplotlib.patches as mpatches  # type: ignore
import numpy as np

from ._chart import Chart
from ._colors import resolve_color
from ._config import VALID_MARKERS
from ._styling import get_marker_size
from ._types import ScatterResult
from ._validation import (
    validate_1d_array,
    validate_chart,
    validate_matching_shapes,
    validate_option,
    validate_optional_1d_array,
)


def scatter(
    chart: Chart,
    *,
    x: Any,
    y: Any,
    color: Union[str, tuple, list] = "default",
    x_error: Optional[Any] = None,
    y_error: Optional[Any] = None,
    marker: str = "o",
    opacity: float = 1,
    label: str = "",
    layer_order: int = 1,
) -> ScatterResult:
    """Add a scatter plot to a chart.

    Error display depends on which error arrays are provided:
    - Both *x_error* and *y_error*: draws error ellipses.
    - Only *x_error*: draws horizontal error bars.
    - Only *y_error*: draws vertical error bars.
    - Neither: no error display.

    Args:
        chart: Chart object created by ``ql.chart()``.
        x: 1D array of x-axis values.
        y: 1D array of y-axis values (same length as *x*).
        color: Color name from the chart's color library, or a 3-tuple.
        x_error: Optional 1D array of x-error magnitudes.
        y_error: Optional 1D array of y-error magnitudes.
        marker: Marker shape.
        opacity: Alpha transparency (0 to 1).
        label: Label for the legend.
        layer_order: Z-order layer (higher = on top).

    Returns:
        A ``ScatterResult`` with references to the matplotlib artists.
    """
    _fn = "scatter"

    # -- validation ------------------------------------------------------------
    validate_chart(chart, _fn)

    if chart.xaxis_type == "timeseries":
        raise ValueError(
            f"ql.{_fn}() error: scatter plots are not compatible with "
            f"timeseries x-axes.\n\n"
            f"Use xtick_labels=\"default\" in ql.chart() for scatter plots."
        )

    validate_1d_array(x, "x", _fn)
    validate_1d_array(y, "y", _fn)
    validate_matching_shapes(x, y, "x", "y", _fn)
    validate_optional_1d_array(x_error, "x_error", _fn)
    validate_optional_1d_array(y_error, "y_error", _fn)
    validate_option(marker, VALID_MARKERS, "marker", _fn)

    # -- resolve color ---------------------------------------------------------
    fill_c, line_c, edge_c = resolve_color(chart.color_library, color, _fn)

    # -- marker sizing ---------------------------------------------------------
    markersize, markeredgewidth = get_marker_size(chart.size, marker)

    # -- error display ---------------------------------------------------------
    error_artist = None

    if x_error is not None and y_error is not None:
        # Ellipses for combined x/y error
        all_shapes = [x_error, y_error]
        for arr in all_shapes:
            validate_matching_shapes(x, arr, "x", "error", _fn)

        x_arr = np.atleast_1d(x)
        y_arr = np.atleast_1d(y)
        xe_arr = np.atleast_1d(x_error)
        ye_arr = np.atleast_1d(y_error)

        error_artist = {"fill": [], "outline": []}
        for i in range(len(x_arr)):
            ell_fill = chart.ax.add_patch(mpatches.Ellipse(
                (x_arr[i], y_arr[i]), xe_arr[i] * 2, ye_arr[i] * 2,
                facecolor=fill_c, alpha=0.8, zorder=layer_order + 2,
            ))
            ell_outline = chart.ax.add_patch(mpatches.Ellipse(
                (x_arr[i], y_arr[i]), xe_arr[i] * 2, ye_arr[i] * 2,
                facecolor="none", edgecolor=edge_c, alpha=1,
                linewidth=0.5, zorder=layer_order + 2,
            ))
            error_artist["fill"].append(ell_fill)
            error_artist["outline"].append(ell_outline)

    elif x_error is not None:
        error_artist = chart.ax.errorbar(
            x, y, xerr=x_error, linestyle="",
            ecolor=edge_c, elinewidth=markeredgewidth,
            capsize=2, capthick=2, zorder=layer_order + 2,
        )

    elif y_error is not None:
        error_artist = chart.ax.errorbar(
            x, y, yerr=y_error, linestyle="",
            ecolor=edge_c, elinewidth=markeredgewidth,
            capsize=2, zorder=layer_order + 2,
        )

    # -- scatter points --------------------------------------------------------
    has_ellipses = x_error is not None and y_error is not None

    scatter_artist = chart.ax.plot(
        x, y,
        linewidth=0,
        marker=marker,
        markersize=markersize,
        mec=None if has_ellipses else edge_c,
        mfc=line_c,
        mew=0 if has_ellipses else markeredgewidth,
        label=label,
        alpha=opacity,
        zorder=layer_order + 2,
    )

    return ScatterResult(scatter=scatter_artist, error=error_artist)
