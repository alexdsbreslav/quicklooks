"""Create the chart skeleton that all other quicklooks functions draw onto."""

from __future__ import annotations

import datetime
from typing import Any, Optional, Tuple, Union

import matplotlib.dates as mdates  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import numpy as np
import pandas as pd  # type: ignore
from dateutil import relativedelta  # type: ignore

from ._colors import ColorLibrary, get_library
from ._config import (
    TIMESERIES_XTICK_LABELS,
    VALID_COLOR_LIBRARIES,
    VALID_FONTS,
    VALID_SIZES,
    VALID_XTICK_LABELS,
    VALID_YTICK_LABELS,
)
from ._styling import ChartStyle, FontStyle, set_tick_labels
from ._validators import validate_bool, validate_option, validate_type


class Chart:
    """The chart object that holds the matplotlib figure/axes and style state.

    Users should not instantiate this directly — use ``ql.chart()`` instead.
    """

    def __init__(
        self,
        fig: Any,
        ax: Any,
        size: str,
        color_library: ColorLibrary,
        font: str,
        font_style: FontStyle,
        plot_style: ChartStyle,
        x_min_max: tuple,
        y_min_max: tuple,
        xrange: Any,
        yrange: float,
        xaxis_type: str,
        xlabel: str,
    ) -> None:
        self.fig = fig
        self.ax = ax
        self.size = size
        self.color_library = color_library
        self.font = font
        self.font_style = font_style
        self.plot_style = plot_style
        self.x_min_max = x_min_max
        self.y_min_max = y_min_max
        self.xrange = xrange
        self.yrange = yrange
        self.xaxis_type = xaxis_type
        self.xlabel = xlabel
        # (label, "pos"|"neg") per ql.area / ql.stacked_bar call with a label;
        # used by ql.legend(..., stacked_plot=True) for diverging charts.
        self._stacked_legend_entries: list[tuple[str, str]] = []


def _record_stacked_legend_label(
    chart: Chart,
    label: str,
    *,
    has_pos: bool,
    has_neg: bool,
) -> None:
    """Append legend metadata for stacked area/bar (see ql.legend stacked_plot)."""
    if not label:
        return
    if has_pos and not has_neg:
        side = "pos"
    elif has_neg and not has_pos:
        side = "neg"
    else:
        # Mixed-sign series: label is attached to the positive artist first.
        side = "pos"
    chart._stacked_legend_entries.append((label, side))


def _end_label_pad_points(chart: Chart) -> float:
    """Horizontal/vertical gap from anchor for end-style labels (typography-based)."""
    return max(4.0, 0.28 * chart.font_style.size.l)


def _end_label_offset_from_anchor(
    chart: Chart,
    *,
    x_anchor: Any,
    y_anchor: Any,
    text: str,
    color: Any,
    zorder: int,
    dx_pts: float,
    dy_pts: float,
    horizontalalignment: str = "left",
    verticalalignment: str = "center",
) -> None:
    """Draw *text* using ``annotate`` + ``offset points`` from data (*x_anchor*, *y_anchor*)."""
    chart.ax.annotate(
        text,
        xy=(x_anchor, y_anchor),
        xytext=(dx_pts, dy_pts),
        textcoords="offset points",
        xycoords="data",
        horizontalalignment=horizontalalignment,
        verticalalignment=verticalalignment,
        color=color,
        fontproperties=chart.font_style.label,
        zorder=zorder,
    )


def _end_label_right_of_anchor(
    chart: Chart,
    *,
    x_anchor: Any,
    y: Any,
    text: str,
    color: Any,
    zorder: int,
    horizontalalignment: str = "left",
    verticalalignment: str = "center",
) -> None:
    """End label to the right of the anchor (``dx`` = pad pts, ``dy`` = 0)."""
    p = _end_label_pad_points(chart)
    _end_label_offset_from_anchor(
        chart,
        x_anchor=x_anchor,
        y_anchor=y,
        text=text,
        color=color,
        zorder=zorder,
        dx_pts=p,
        dy_pts=0.0,
        horizontalalignment=horizontalalignment,
        verticalalignment=verticalalignment,
    )


def chart(
    *,
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    x_min_max: tuple = (0, 1),
    y_min_max: tuple = (0, 1),
    xtick_interval: Union[int, float] = 0.25,
    ytick_interval: Union[int, float] = 0.25,
    size: str = "notebook",
    colors: str = "extended",
    font: str = "rubik",
    xtick_labels: Union[str, list] = "default",
    ytick_labels: Union[str, list] = "default",
    horizontal_gridlines: bool = False,
    vertical_gridlines: bool = False,
) -> Chart:
    """Create a chart skeleton with axes, title, and styling.

    Args:
        title: Chart title text.
        xlabel: X-axis label text.
        ylabel: Y-axis label text.
        x_min_max: Tuple of (min, max) for the x-axis.
        y_min_max: Tuple of (min, max) for the y-axis.
        xtick_interval: Spacing between x-axis ticks.
        ytick_interval: Spacing between y-axis ticks.
        size: Chart size preset.
        colors: Color library name.
        font: Font family name.
        xtick_labels: X-axis tick label format or list of custom labels.
        ytick_labels: Y-axis tick label format or list of custom labels.
        horizontal_gridlines: Show horizontal grid lines.
        vertical_gridlines: Show vertical grid lines.

    Returns:
        A ``Chart`` object to pass to all other quicklooks functions.
    """
    _fn = "chart"

    # -- validate scalar params ------------------------------------------------
    validate_option(size, VALID_SIZES, "size", _fn)
    validate_option(font, VALID_FONTS, "font", _fn)
    validate_type(title, (str,), "title", _fn)
    validate_type(xlabel, (str,), "xlabel", _fn)
    validate_type(ylabel, (str,), "ylabel", _fn)
    validate_bool(horizontal_gridlines, "horizontal_gridlines", _fn)
    validate_bool(vertical_gridlines, "vertical_gridlines", _fn)

    # -- resolve color library -------------------------------------------------
    color_library = get_library(colors, _fn)

    # -- validate y_min_max ----------------------------------------------------
    if not isinstance(y_min_max, tuple) or len(y_min_max) != 2:
        raise TypeError(
            f"ql.{_fn}() error: 'y_min_max' must be a tuple of two values, "
            f"e.g. (0, 100).\n\nReceived: {y_min_max!r}"
        )
    if y_min_max[1] <= y_min_max[0]:
        raise ValueError(
            f"ql.{_fn}() error: 'y_min_max' second value must be greater than "
            f"the first. Received: {y_min_max!r}"
        )
    yrange = y_min_max[1] - y_min_max[0]

    # -- validate xtick_labels type --------------------------------------------
    if not isinstance(xtick_labels, (str, list)):
        raise TypeError(
            f"ql.{_fn}() error: 'xtick_labels' must be a string or a list of "
            f"strings.\n\nReceived: {type(xtick_labels).__name__}"
        )
    if isinstance(xtick_labels, str):
        validate_option(xtick_labels, VALID_XTICK_LABELS, "xtick_labels", _fn)

    # -- validate ytick_labels type --------------------------------------------
    if not isinstance(ytick_labels, (str, list)):
        raise TypeError(
            f"ql.{_fn}() error: 'ytick_labels' must be a string or a list of "
            f"strings.\n\nReceived: {type(ytick_labels).__name__}"
        )
    if isinstance(ytick_labels, str) and ytick_labels != "default":
        validate_option(ytick_labels, VALID_YTICK_LABELS, "ytick_labels", _fn)

    # -- determine axis type and parse x_min_max -------------------------------
    xaxis_type = "default"

    if isinstance(xtick_labels, str) and xtick_labels in TIMESERIES_XTICK_LABELS:
        xaxis_type = "timeseries"
        x_min_max = _parse_timeseries_min_max(x_min_max, _fn)

    # -- validate x_min_max for non-timeseries ---------------------------------
    if xaxis_type == "default":
        if not isinstance(x_min_max, tuple) or len(x_min_max) != 2:
            raise TypeError(
                f"ql.{_fn}() error: 'x_min_max' must be a tuple of two values, "
                f"e.g. (0, 100).\n\nReceived: {x_min_max!r}"
            )

    # -- validate tick intervals -----------------------------------------------
    xrange = _validate_tick_intervals(
        x_min_max, y_min_max, xtick_interval, ytick_interval,
        xtick_labels, xaxis_type, yrange, _fn,
    )

    # -- build styling ---------------------------------------------------------
    ps = ChartStyle(size, ylabel)
    fs = FontStyle(size, font)

    # -- create figure and axes ------------------------------------------------
    fig, ax = plt.subplots(nrows=1, figsize=ps.figsize)

    # -- title -----------------------------------------------------------------
    ax.set_title(
        title,
        color=color_library.text,
        pad=ps.title_pad,
        fontproperties=fs.title,
    )

    # -- background ------------------------------------------------------------
    ax.patch.set_xy((-0.16, -0.14))
    ax.patch.set_height(1.2)
    ax.patch.set_width(1.28)
    ax.set_facecolor(color_library.background)
    fig.set_facecolor(color_library.background)

    # -- gridlines -------------------------------------------------------------
    if horizontal_gridlines:
        ax.yaxis.grid(
            which="major", linestyle=":", linewidth=ps.linewidth,
            color="0.8", zorder=1,
        )
    if vertical_gridlines:
        ax.xaxis.grid(
            which="major", linestyle=":", linewidth=ps.linewidth,
            color="0.8", zorder=1,
        )

    # -- spines ----------------------------------------------------------------
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("bottom", "left"):
        ax.spines[spine].set_linewidth(ps.linewidth)
        ax.spines[spine].set_color(color_library.text)
        ax.spines[spine].set_zorder(2)

    # -- tick styling ----------------------------------------------------------
    for i, which in enumerate(("x", "y")):
        ax.tick_params(
            which, colors=color_library.text,
            width=ps.linewidth, pad=ps.tick_pad[i], length=ps.tick_length,
        )
    for tick_label in ax.get_xticklabels():
        tick_label.set_font_properties(fs.label)
    for tick_label in ax.get_yticklabels():
        tick_label.set_font_properties(fs.label)

    # -- axis limits -----------------------------------------------------------
    ax.set_ylim(y_min_max)
    ax.set_xlim(x_min_max)

    # -- tick locators ---------------------------------------------------------
    ax.yaxis.set_major_locator(plt.MultipleLocator(ytick_interval))

    if xaxis_type == "default":
        ax.xaxis.set_major_locator(plt.MultipleLocator(xtick_interval))
    else:
        _set_timeseries_locator(ax, xtick_labels, xtick_interval)

    # -- axis labels -----------------------------------------------------------
    ax.set_ylabel(
        ylabel,
        color=color_library.text,
        rotation=90 if size == "half_slide" else 0,
        labelpad=ps.label_pad[1],
        horizontalalignment="center",
        linespacing=1.6,
        fontproperties=fs.label,
    )
    ax.set_xlabel(
        xlabel,
        color=color_library.text,
        labelpad=ps.label_pad[0],
        fontproperties=fs.label,
    )

    # -- tick label formatting -------------------------------------------------
    set_tick_labels(xtick_labels, "x", ax, x_min_max)
    set_tick_labels(ytick_labels, "y", ax, y_min_max)

    plt.tight_layout()

    return Chart(
        fig=fig,
        ax=ax,
        size=size,
        color_library=color_library,
        font=font,
        font_style=fs,
        plot_style=ps,
        x_min_max=x_min_max,
        y_min_max=y_min_max,
        xrange=xrange,
        yrange=yrange,
        xaxis_type=xaxis_type,
        xlabel=xlabel,
    )


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _parse_timeseries_min_max(x_min_max: tuple, func_name: str) -> tuple:
    """Convert x_min_max strings/dates into datetime.date objects."""
    parsed = [None, None]
    for i in range(2):
        val = x_min_max[i]
        if isinstance(val, str):
            parsed[i] = datetime.datetime.strptime(val, "%Y-%m-%d").date()
        elif isinstance(val, (datetime.date, datetime.datetime)):
            parsed[i] = val
        elif hasattr(pd, "_libs") and isinstance(val, pd.Timestamp):
            parsed[i] = val
        else:
            raise TypeError(
                f"ql.{func_name}() error: when xtick_labels is a timeseries "
                f"format, x_min_max values must be date strings (\"YYYY-MM-DD\") "
                f"or datetime objects.\n\n"
                f"Received x_min_max[{i}]: {type(val).__name__} = {val!r}"
            )
    return (parsed[0], parsed[1])


def _validate_tick_intervals(
    x_min_max: tuple,
    y_min_max: tuple,
    xtick_interval: Union[int, float],
    ytick_interval: Union[int, float],
    xtick_labels: Union[str, list],
    xaxis_type: str,
    yrange: float,
    func_name: str,
) -> Any:
    """Validate tick intervals against axis ranges. Returns xrange."""
    _fn = func_name

    # -- y-axis checks (always numeric) ----------------------------------------
    if ytick_interval > yrange:
        raise ValueError(
            f"ql.{_fn}() error: 'ytick_interval' ({ytick_interval}) is larger "
            f"than the y-axis range ({yrange}).\n\n"
            f"Decrease ytick_interval or widen y_min_max."
        )
    if 20 * ytick_interval < yrange:
        raise ValueError(
            f"ql.{_fn}() error: 'ytick_interval' ({ytick_interval}) would create "
            f"more than 20 ticks on the y-axis.\n\n"
            f"Increase ytick_interval or narrow y_min_max."
        )

    # -- x-axis checks ---------------------------------------------------------
    if xaxis_type == "timeseries":
        return _validate_timeseries_xtick(
            x_min_max, xtick_interval, xtick_labels, _fn,
        )
    else:
        xrange = x_min_max[1] - x_min_max[0]
        if xtick_interval > xrange:
            raise ValueError(
                f"ql.{_fn}() error: 'xtick_interval' ({xtick_interval}) is "
                f"larger than the x-axis range ({xrange}).\n\n"
                f"Decrease xtick_interval or widen x_min_max."
            )
        if 20 * xtick_interval < xrange:
            raise ValueError(
                f"ql.{_fn}() error: 'xtick_interval' ({xtick_interval}) would "
                f"create more than 20 ticks on the x-axis.\n\n"
                f"Increase xtick_interval or narrow x_min_max."
            )
        return xrange


def _validate_timeseries_xtick(
    x_min_max: tuple,
    xtick_interval: Union[int, float],
    xtick_labels: Union[str, list],
    func_name: str,
) -> int:
    """Validate timeseries x-tick settings. Returns xrange in days."""
    xrange_days = (x_min_max[1] - x_min_max[0]).days
    rd = relativedelta.relativedelta(x_min_max[1], x_min_max[0])
    total_months = rd.years * 12 + rd.months

    if xtick_labels == "days":
        if xtick_interval > xrange_days:
            raise ValueError(
                f"ql.{func_name}() error: 'xtick_interval' is larger than the "
                f"date range ({xrange_days} days).\n\n"
                f"Decrease xtick_interval or widen x_min_max."
            )
        if 20 * xtick_interval < xrange_days:
            raise ValueError(
                f"ql.{func_name}() error: 'xtick_interval' would create too many "
                f"ticks for a {xrange_days}-day range.\n\n"
                f"Increase xtick_interval or use xtick_labels=\"weeks\"."
            )

    elif xtick_labels == "weeks":
        weeks = np.floor(xrange_days / 7)
        if xtick_interval > weeks:
            raise ValueError(
                f"ql.{func_name}() error: 'xtick_interval' is larger than the "
                f"date range ({int(weeks)} weeks).\n\n"
                f"Decrease xtick_interval or widen x_min_max."
            )
        if 20 * xtick_interval < weeks:
            raise ValueError(
                f"ql.{func_name}() error: 'xtick_interval' would create too many "
                f"ticks for a {int(weeks)}-week range.\n\n"
                f"Increase xtick_interval or use xtick_labels=\"months\"."
            )

    elif xtick_labels == "months":
        if total_months < 2:
            raise ValueError(
                f"ql.{func_name}() error: date range is too short for monthly "
                f"ticks ({total_months} months).\n\n"
                f"Use xtick_labels=\"days\" or \"weeks\" for ranges under 2 months."
            )
        if total_months > 15:
            raise ValueError(
                f"ql.{func_name}() error: date range is too long for monthly "
                f"ticks ({total_months} months).\n\n"
                f"Use xtick_labels=\"quarters\" for ranges over 15 months."
            )

    elif xtick_labels == "quarters":
        if total_months < 9:
            raise ValueError(
                f"ql.{func_name}() error: date range is too short for quarterly "
                f"ticks ({total_months} months).\n\n"
                f"Use xtick_labels=\"months\" for ranges under 9 months."
            )
        if total_months > 48:
            raise ValueError(
                f"ql.{func_name}() error: date range is too long for quarterly "
                f"ticks ({total_months} months).\n\n"
                f"Use xtick_labels=\"years\" for ranges over 4 years."
            )

    elif xtick_labels == "years":
        if xtick_interval > rd.years:
            raise ValueError(
                f"ql.{func_name}() error: 'xtick_interval' is larger than the "
                f"date range ({rd.years} years).\n\n"
                f"Decrease xtick_interval or widen x_min_max."
            )
        if rd.years > 0 and 20 * xtick_interval < rd.years:
            raise ValueError(
                f"ql.{func_name}() error: 'xtick_interval' would create too many "
                f"ticks for a {rd.years}-year range.\n\n"
                f"Increase xtick_interval."
            )

    return xrange_days


def _set_timeseries_locator(
    ax: Any,
    xtick_labels: Union[str, list],
    xtick_interval: Union[int, float],
) -> None:
    """Set the appropriate matplotlib date locator on the x-axis."""
    if xtick_labels == "years":
        ax.xaxis.set_major_locator(mdates.YearLocator(base=1))
    elif xtick_labels == "quarters":
        ax.xaxis.set_major_locator(mdates.MonthLocator((1, 4, 7, 10)))
    elif xtick_labels == "months":
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    elif xtick_labels == "weeks":
        ax.xaxis.set_major_locator(
            mdates.WeekdayLocator(byweekday=0, interval=int(xtick_interval))
        )
    elif xtick_labels == "days":
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=int(xtick_interval)))
