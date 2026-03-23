"""quicklooks — create presentation-ready charts quickly.

Usage::

    import quicklooks as ql

    cs = ql.chart(title="My Chart", x_min_max=(0, 10), y_min_max=(0, 100),
                  xtick_interval=2, ytick_interval=20)
    ql.line(cs, x=x, y=y, color="blue", label="Series A")
    ql.legend(cs, location="upper right")
"""

from ._chart import chart
from .plots import area, bar, dist, line, refline, scatter, stacked_bar, text
from ._legend import legend
from ._save import save
from ._install_skill import install_skill
from ._cell_linter import validate_cell

__all__ = [
    "chart",
    "line", "area", "bar", "stacked_bar", "scatter", "dist",
    "refline", "text",
    "legend", "save",
    "install_skill", "validate_cell",
]
