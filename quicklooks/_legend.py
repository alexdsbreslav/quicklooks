"""Legend function for quicklooks."""

from __future__ import annotations

from typing import Any, Union

from ._chart import Chart
from ._config import VALID_LEGEND_LOCATIONS
from ._types import LegendResult
from ._validation import validate_chart, validate_option


def legend(
    chart: Chart,
    *,
    location: str = "best",
    frame: bool = False,
) -> LegendResult:
    """Add a legend to a chart.

    Args:
        chart: Chart object created by ``ql.chart()``.
        location: Legend placement.
        frame: If ``True``, draw a border around the legend.

    Returns:
        A ``LegendResult`` with a reference to the matplotlib legend.
    """
    _fn = "legend"

    # -- validation ------------------------------------------------------------
    validate_chart(chart, _fn)
    validate_option(location, VALID_LEGEND_LOCATIONS, "location", _fn)

    # -- common kwargs ---------------------------------------------------------
    common = dict(
        prop=chart.font_style.legend,
        frameon=frame,
        fancybox=True,
        facecolor=chart.color_library.background,
        borderpad=0.75,
        labelspacing=0.75,
        framealpha=1,
    )

    # -- create legend ---------------------------------------------------------
    if location == "outside right":
        legend_artist = chart.ax.legend(
            loc="center left", bbox_to_anchor=(1.025, 0.5), **common,
        )
    elif location == "below":
        offset = -0.2 if chart.xlabel else -0.1
        ncol = 3 if chart.size == "half_slide" else 4
        legend_artist = chart.ax.legend(
            loc="upper center", bbox_to_anchor=(0.5, offset),
            ncol=ncol, **common,
        )
    else:
        legend_artist = chart.ax.legend(loc=location, **common)

    # -- text color ------------------------------------------------------------
    for text_obj in legend_artist.get_texts():
        text_obj.set_color(chart.color_library.text)

    # -- frame styling ---------------------------------------------------------
    if frame:
        legend_artist.get_frame().set_linewidth(1)
        legend_artist.get_frame().set_edgecolor("0.8")

    return LegendResult(legend=legend_artist)
