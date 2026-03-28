"""Legend function for quicklooks."""

from __future__ import annotations

from ._chart import Chart
from ._config import VALID_LEGEND_LOCATIONS
from ._types import LegendResult
from ._validators import validate_bool, validate_chart, validate_option


def _ordered_stacked_legend_handles(
    chart: Chart,
    handles: list,
    labels: list,
) -> tuple[list, list]:
    """Reorder legend rows for stacked plots; supports diverging pos/neg stacks."""
    entries = getattr(chart, "_stacked_legend_entries", None) or []
    if not entries:
        return handles[::-1], labels[::-1]
    label_to_handle = dict(zip(labels, handles))
    pos_labels = [lab for lab, side in entries if side == "pos"]
    neg_labels = [lab for lab, side in entries if side == "neg"]
    # Above zero: reverse call order (first drawn = bottom of stack).
    # Below zero: keep call order (first drawn = closest to axis = top of neg stack).
    ordered_labels = pos_labels[::-1] + neg_labels
    ordered_handles = [
        label_to_handle[lab] for lab in ordered_labels if lab in label_to_handle
    ]
    used = set(ordered_labels)
    extra_h: list = []
    extra_l: list = []
    for h, lab in zip(handles, labels):
        if lab not in used:
            extra_h.append(h)
            extra_l.append(lab)
    return ordered_handles + extra_h, ordered_labels + extra_l


def legend(
    chart: Chart,
    *,
    location: str = "best",
    frame: bool = False,
    stacked_plot: bool = False,
) -> LegendResult:
    """Add a legend to a chart.

    Args:
        chart: Chart object created by ``ql.chart()``.
        location: Legend placement.
        frame: If ``True``, draw a border around the legend.
        stacked_plot: If ``True``, order legend rows to match stacked layers.
            For diverging charts (values above and below zero), positive
            series appear first (top to bottom: top-of-stack to bottom), then
            negative series (same). Other legend entries (e.g. ``ql.refline()``
            with a label) follow.

    Returns:
        A ``LegendResult`` with a reference to the matplotlib legend.
    """
    _fn = "legend"

    # -- validation ------------------------------------------------------------
    validate_chart(chart, _fn)
    validate_option(location, VALID_LEGEND_LOCATIONS, "location", _fn)
    validate_bool(stacked_plot, "stacked_plot", _fn)

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
    if stacked_plot:
        handles, labels = chart.ax.get_legend_handles_labels()
        handles, labels = _ordered_stacked_legend_handles(chart, handles, labels)
        legend_kw = dict(handles=handles, labels=labels, **common)
    else:
        legend_kw = common

    if location == "outside right":
        legend_artist = chart.ax.legend(
            loc="center left", bbox_to_anchor=(1.025, 0.5), **legend_kw,
        )
    elif location == "below":
        offset = -0.2 if chart.xlabel else -0.1
        ncol = 3 if chart.size == "half_slide" else 4
        legend_artist = chart.ax.legend(
            loc="upper center", bbox_to_anchor=(0.5, offset),
            ncol=ncol, **legend_kw,
        )
    else:
        legend_artist = chart.ax.legend(loc=location, **legend_kw)

    # -- text color ------------------------------------------------------------
    for text_obj in legend_artist.get_texts():
        text_obj.set_color(chart.color_library.text)

    # -- frame styling ---------------------------------------------------------
    if frame:
        legend_artist.get_frame().set_linewidth(1)
        legend_artist.get_frame().set_edgecolor("0.8")

    return LegendResult(legend=legend_artist)
