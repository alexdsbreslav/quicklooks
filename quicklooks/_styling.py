"""Internal styling helpers: chart dimensions, fonts, markers, tick labels.

These are not part of the public API. They are used by ``_chart.py`` and
the individual plot modules.
"""

from __future__ import annotations

import os
import warnings
from pathlib import Path
from typing import Any, Optional, Sequence, Tuple

import numpy as np
from matplotlib import font_manager  # type: ignore
import matplotlib.ticker as ticker  # type: ignore
import matplotlib.dates as mdates  # type: ignore


# ---------------------------------------------------------------------------
# Chart skeleton sizing
# ---------------------------------------------------------------------------

_FIGSIZE = {
    "notebook": (6 * 16 / 9, 6),
    "half_slide": (15, 15 * 3 / 4),
    "full_slide": (30, 30 / 1.94),
}

_TITLE_PAD = {"notebook": 30, "half_slide": 35, "full_slide": 35}
_LINEWIDTH = {"notebook": 2, "half_slide": 2, "full_slide": 4}
_TICK_PAD = {"notebook": (5, 5), "half_slide": (5, 5), "full_slide": (10, 10)}
_TICK_LENGTH = {"notebook": 6, "half_slide": 6, "full_slide": 10}


def _find_text_width(text: str) -> Tuple[int, int]:
    """Return ``(line_break_count, max_line_length)`` for *text*."""
    lines = text.split("\n")
    return (len(lines) - 1, max(len(line) for line in lines))


class ChartStyle:
    """Layout dimensions that depend on chart *size* and *ylabel* text."""

    def __init__(self, size: str, ylabel: str) -> None:
        self.figsize = _FIGSIZE[size]
        self.title_pad = _TITLE_PAD[size]
        self.linewidth = _LINEWIDTH[size]
        self.tick_pad = _TICK_PAD[size]
        self.tick_length = _TICK_LENGTH[size]

        _, text_width = _find_text_width(ylabel)
        label_pad_map = {
            "notebook": (15, 3 * text_width + 20),
            "half_slide": (15, 15),
            "full_slide": (30, 3 * text_width + 70),
        }
        self.label_pad = label_pad_map[size]


# ---------------------------------------------------------------------------
# Font sizing and loading
# ---------------------------------------------------------------------------

_BASE_FONT_SIZE = {"notebook": 20, "half_slide": 32, "full_slide": 48}


class FontSizes:
    """Named font sizes derived from the chart *size*."""

    def __init__(self, size: str) -> None:
        base = _BASE_FONT_SIZE[size]
        self.xl = base
        self.l = base - 4  # noqa: E741
        self.m = base - 8
        self.s = base - 12


class FontStyle:
    """Font properties loaded from the bundled fonts directory."""

    def __init__(self, size: str, font_name: str) -> None:
        font_folder = Path(__file__).parent / "fonts" / font_name
        font_dir = os.listdir(font_folder)

        title_candidates = [f for f in font_dir if "title" in f]
        if not title_candidates:
            raise FileNotFoundError(
                f"Font folder '{font_folder}' is missing a title font file "
                f"(title.ttf or title.otf)."
            )
        title_path = font_folder / title_candidates[0]

        text_candidates = [f for f in font_dir if "text" in f]
        if not text_candidates:
            raise FileNotFoundError(
                f"Font folder '{font_folder}' is missing a text font file "
                f"(text.ttf or text.otf)."
            )
        text_path = font_folder / text_candidates[0]

        self.size = FontSizes(size)
        self.title = font_manager.FontProperties(fname=str(title_path), size=self.size.xl)
        self.label = font_manager.FontProperties(fname=str(text_path), size=self.size.l)
        self.legend = font_manager.FontProperties(fname=str(text_path), size=self.size.m)


# ---------------------------------------------------------------------------
# Marker helpers
# ---------------------------------------------------------------------------

_MARKER_SIZE = {"notebook": 7, "half_slide": 10, "full_slide": 14}
_MARKER_EDGE_WIDTH = {"notebook": 2, "half_slide": 2, "full_slide": 3}


def get_marker_size(size: str, marker: Optional[str]) -> Tuple[int, int]:
    """Return ``(markersize, markeredgewidth)`` for the given chart *size*.

    If *marker* is ``None`` both values are 0.
    """
    if marker is None:
        return (0, 0)
    return (_MARKER_SIZE[size], _MARKER_EDGE_WIDTH[size])


# ---------------------------------------------------------------------------
# Tick-label formatting
# ---------------------------------------------------------------------------

def set_tick_labels(
    labels: Any,
    axis: str,
    ax: Any,
    min_max: tuple,
) -> None:
    """Apply tick-label formatting to *ax* for the given *axis* ('x' or 'y').

    *labels* can be:
    - ``"default"`` — no formatting changes.
    - A ``list`` of strings — applied as custom tick labels.
    - A preset string (``"percents"``, ``"years"``, etc.) — applies the
      corresponding matplotlib formatter.
    """
    if labels == "default":
        return

    if isinstance(labels, list):
        _set_custom_tick_labels(labels, axis, ax)
        return

    if axis == "x":
        _set_x_tick_format(labels, ax, min_max)
    elif axis == "y":
        _set_y_tick_format(labels, ax)


def _set_custom_tick_labels(labels: list, axis: str, ax: Any) -> None:
    """Replace displayed tick labels with a user-provided list of strings."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        if axis == "x":
            positions = [t.get_position()[0] for t in ax.get_xticklabels()]
        else:
            positions = [t.get_position()[1] for t in ax.get_yticklabels()]

        displayed = positions[1:-1]
        if len(labels) != len(displayed):
            raise ValueError(
                f"Expected {len(displayed)} custom {axis}_labels but received "
                f"{len(labels)}. The number of labels must match the number of "
                f"displayed ticks."
            )

        new_labels = [None] + list(labels) + [None]
        if axis == "x":
            ax.set_xticklabels(new_labels)
        else:
            ax.set_yticklabels(new_labels)


def _set_x_tick_format(labels: str, ax: Any, min_max: tuple) -> None:
    """Apply a preset x-axis tick formatter."""
    labels_need_edit = False

    if labels == "percents":
        ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
    elif labels == "years":
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    elif labels == "quarters":
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
        labels_need_edit = True
    elif labels == "months":
        if min_max[0].year == min_max[1].year:
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
        else:
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
            labels_need_edit = True
    elif labels in ("days", "weeks"):
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
    else:
        raise ValueError(
            f"ql.chart() error: invalid value for 'xtick_labels': \"{labels}\"\n\n"
            f"Valid options: \"default\", \"percents\", \"years\", \"quarters\", "
            f"\"months\", \"weeks\", \"days\", or a list of strings."
        )

    if labels_need_edit:
        _post_process_x_labels(labels, ax)


def _post_process_x_labels(labels: str, ax: Any) -> None:
    """Rewrite quarter / month+year x-tick labels after initial formatting."""
    positions = [t.get_position()[0] for t in ax.get_xticklabels()]
    ax.xaxis.set_major_locator(ticker.FixedLocator(positions))
    raw_labels = [t.get_text() for t in ax.get_xticklabels()]

    if labels == "quarters":
        replacements = {"Jan": "Q1", "Apr": "Q2", "Jul": "Q3", "Oct": "Q4"}
        new_labels = []
        for lbl in raw_labels:
            parts = lbl.split(" ")
            quarter = replacements.get(parts[0], parts[0])
            new_labels.append(f"{quarter}\n{parts[1]}" if len(parts) > 1 else lbl)
        ax.set_xticklabels(new_labels)

    elif labels == "months":
        new_labels = []
        for i, lbl in enumerate(raw_labels):
            parts = lbl.split("\n")
            if len(parts) == 2 and (parts[0] == "Jan" or i == 0):
                new_labels.append(lbl)
            elif len(parts) == 2:
                new_labels.append(parts[0])
            else:
                new_labels.append(lbl)
        ax.set_xticklabels(new_labels)


def _set_y_tick_format(labels: str, ax: Any) -> None:
    """Apply a preset y-axis tick formatter."""
    if labels == "percents":
        ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
    elif labels in ("1k", "100k", "1m"):
        positions = [t.get_position()[1] for t in ax.get_yticklabels()]
        ax.yaxis.set_major_locator(ticker.FixedLocator(positions))

        denom_map = {"1k": 1e3, "100k": 1e3, "1m": 1e6}
        denom = denom_map[labels]
        suffix = labels[-1].upper()
        fmt = "{:3.0f}{}" if labels == "100k" else "{:3.1f}{}"

        new_labels = [
            fmt.format(t.get_position()[1] / denom, suffix)
            for t in ax.get_yticklabels()
        ]
        ax.set_yticklabels(new_labels)
    else:
        raise ValueError(
            f"ql.chart() error: invalid value for 'ytick_labels': \"{labels}\"\n\n"
            f"Valid options: \"default\", \"percents\", \"1k\", \"100k\", \"1m\", "
            f"or a list of strings."
        )
