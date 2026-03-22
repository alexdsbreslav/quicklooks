"""Result dataclasses returned by quicklooks plotting functions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class LineResult:
    """Matplotlib artists created by ``ql.line()``."""

    line: Any
    fill: Optional[Any] = None
    upper: Optional[Any] = None
    lower: Optional[Any] = None


@dataclass
class BarResult:
    """Matplotlib artists created by ``ql.bar()``."""

    bars: Any
    xlim: tuple = (0, 0)


@dataclass
class ScatterResult:
    """Matplotlib artists created by ``ql.scatter()``."""

    scatter: Any
    error: Optional[Any] = None


@dataclass
class DistResult:
    """Matplotlib artists created by ``ql.dist()``."""

    distribution: Any


@dataclass
class RefLineResult:
    """Matplotlib artists created by ``ql.refline()``."""

    line: Any


@dataclass
class TextResult:
    """Matplotlib artists created by ``ql.text()``."""

    text: Any


@dataclass
class LegendResult:
    """Matplotlib artists created by ``ql.legend()``."""

    legend: Any
