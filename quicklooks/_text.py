"""Text annotation function for quicklooks."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from ._chart import Chart
from ._colors import resolve_color
from ._config import (
    VALID_HORIZONTAL_ALIGNS,
    VALID_TEXT_SIZES,
    VALID_VERTICAL_ALIGNS,
)
from ._types import TextResult
from ._validation import validate_chart, validate_option


def text(
    chart: Chart,
    *,
    text: str = "",
    x: Any = 0,
    y: Any = 0,
    size: Union[str, int, float] = "m",
    color: Union[str, tuple, list] = "black",
    horizontal_align: str = "center",
    vertical_align: str = "center",
    rotation: Union[int, float] = 0,
    box: bool = False,
    layer_order: int = 1,
) -> TextResult:
    """Add text annotation to a chart.

    Args:
        chart: Chart object created by ``ql.chart()``.
        text: The text string to display.
        x: X-axis position. For timeseries axes, a ``"YYYY-MM-DD"`` string.
        y: Y-axis position.
        size: Font size as a named preset or a numeric point size.
        color: Color name from the chart's color library, or a 3-tuple.
        horizontal_align: Horizontal alignment.
        vertical_align: Vertical alignment.
        rotation: Text rotation in degrees.
        box: If ``True``, draw a box around the text.
        layer_order: Z-order layer (higher = on top).

    Returns:
        A ``TextResult`` with a reference to the matplotlib text artist.
    """
    _fn = "text"

    # -- validation ------------------------------------------------------------
    validate_chart(chart, _fn)
    validate_option(horizontal_align, VALID_HORIZONTAL_ALIGNS, "horizontal_align", _fn)
    validate_option(vertical_align, VALID_VERTICAL_ALIGNS, "vertical_align", _fn)

    # -- resolve text size -----------------------------------------------------
    if isinstance(size, str):
        validate_option(size, VALID_TEXT_SIZES, "size", _fn)
        size_map = {
            "xl": chart.font_style.size.xl,
            "l": chart.font_style.size.l,
            "m": chart.font_style.size.m,
            "s": chart.font_style.size.s,
        }
        text_size = size_map[size]
    else:
        text_size = size

    # -- resolve color ---------------------------------------------------------
    resolved = resolve_color(chart.color_library, color, _fn)
    text_color = resolved[1]  # use the "line/mid" color

    # -- handle timeseries x position ------------------------------------------
    x_pos = x
    if chart.xaxis_type == "timeseries":
        if isinstance(x_pos, str):
            x_pos = datetime.strptime(x_pos, "%Y-%m-%d")
        else:
            raise TypeError(
                f"ql.{_fn}() error: when the chart uses a timeseries x-axis, "
                f"'x' must be a date string in \"YYYY-MM-DD\" format.\n\n"
                f"Received: {type(x_pos).__name__} = {x_pos!r}"
            )

    # -- draw text -------------------------------------------------------------
    common_kwargs = dict(
        fontproperties=chart.font_style.label,
        horizontalalignment=horizontal_align,
        verticalalignment=vertical_align,
        size=text_size,
        color=text_color,
        zorder=layer_order + 2,
    )

    if box:
        text_artist = chart.ax.text(
            x_pos, y, text,
            bbox=dict(
                facecolor=chart.color_library.background,
                edgecolor=chart.color_library.text,
                boxstyle="round, pad = 0.5",
                alpha=1,
                linewidth=0.5,
            ),
            rotation=rotation,
            **common_kwargs,
        )
    else:
        text_artist = chart.ax.text(
            x_pos, y, text,
            rotation=rotation,
            **common_kwargs,
        )

    return TextResult(text=text_artist)
