"""quicklooks — create presentation-ready charts quickly.

Usage::

    import quicklooks as ql

    cs = ql.chart(title="My Chart", x_min_max=(0, 10), y_min_max=(0, 100),
                  xtick_interval=2, ytick_interval=20)
    ql.line(cs, x=x, y=y, color="blue", label="Series A")
    ql.legend(cs, location="upper right")
"""

from ._chart import chart
from ._line import line
from ._bar import bar
from ._scatter import scatter
from ._dist import dist
from ._refline import refline
from ._legend import legend
from ._text import text
from ._save import save
from ._install_skill import install_skill
from ._validate import validate_cell

__all__ = [
    "chart",
    "line",
    "bar",
    "scatter",
    "dist",
    "refline",
    "legend",
    "text",
    "save",
    "install_skill",
    "validate_cell",
]
