"""Valid options for all quicklooks parameters.

These tuples are the single source of truth used by validation functions
and referenced by the companion Cursor skill.
"""

from __future__ import annotations

VALID_SIZES = ("notebook", "half_slide", "full_slide")

VALID_FONTS = (
    "lato", "montserrat", "oswald", "roboto",
    "rubik", "source_sans", "work_sans",
)

VALID_COLOR_LIBRARIES = ("extended", "neon", "sorbet", "bloom", "hockney")

VALID_XTICK_LABELS = (
    "default", "percents",
    "years", "quarters", "months", "weeks", "days",
)

VALID_YTICK_LABELS = ("default", "percents", "1k", "100k", "1m")

TIMESERIES_XTICK_LABELS = ("years", "quarters", "months", "weeks", "days")

VALID_LINESTYLES = (
    "solid", "dashed", "dotted", "dashdot",
    "-", "--", ":", "-.",
)

VALID_MARKERS = (None, "o", ".", "v", "^", "s", "d", "D", "X", "x")

VALID_DIST_TYPES = ("binned_counts", "binned_density", "smooth_density")

VALID_LEGEND_LOCATIONS = (
    "best", "upper right", "upper left",
    "lower left", "lower right", "right",
    "center left", "center right",
    "lower center", "upper center", "center",
    "outside right", "below",
)

VALID_REFLINE_DIRECTIONS = (
    "horizontal", "vertical", "diagonal_up", "diagonal_down",
)

VALID_TEXT_SIZES = ("xl", "l", "m", "s")

VALID_HORIZONTAL_ALIGNS = ("center", "left", "right")

VALID_VERTICAL_ALIGNS = ("center", "top", "bottom")

VALID_SAVE_FORMATS = ("png", "pdf", "svg", "jpg")
