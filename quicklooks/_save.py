"""Save chart function for quicklooks."""

from __future__ import annotations

import os
from typing import Any

import matplotlib.pyplot as plt  # type: ignore

from ._chart import Chart
from ._config import VALID_SAVE_FORMATS
from ._validators import validate_chart, validate_option


_DPI = {"notebook": 300, "half_slide": 72, "full_slide": 72}


def save(
    chart: Chart,
    *,
    name: str = "chart",
    folder: str = "./",
    format: str = "png",
) -> None:
    """Save a chart to disk.

    Args:
        chart: Chart object created by ``ql.chart()``.
        name: File name (without extension).
        folder: Directory to save into.
        format: Image format.
    """
    _fn = "save"

    # -- validation ------------------------------------------------------------
    validate_chart(chart, _fn)
    validate_option(format, VALID_SAVE_FORMATS, "format", _fn)

    if not isinstance(name, str) or not name:
        raise ValueError(
            f"ql.{_fn}() error: 'name' must be a non-empty string.\n\n"
            f"Received: {name!r}"
        )

    if not os.path.isdir(folder):
        raise FileNotFoundError(
            f"ql.{_fn}() error: folder does not exist: \"{folder}\"\n\n"
            f"Create the folder first or provide a valid path."
        )

    # -- save ------------------------------------------------------------------
    filepath = os.path.join(folder, f"{name}.{format}")
    dpi = _DPI.get(chart.size, 300)

    chart.fig.savefig(filepath, format=format, dpi=dpi, bbox_inches="tight")
