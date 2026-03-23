# quicklooks

quicklooks is a Python package for creating presentation-ready data visualizations quickly. It wraps matplotlib with a simple, consistent API designed for data scientists, product managers, and researchers working in Jupyter notebooks.

## v2.0 — designed for AI agents

quicklooks v2 is built for the AI-agent workflow. Every chart the agent writes follows the same template, making it easy to scan, understand, and modify. A companion [Cursor skill](#cursor-skill) guides agents to produce consistent, well-structured code every time.

## Install

```bash
pip install quicklooks
```

Then in your notebook:

```python
import quicklooks as ql
```

## AI agent skill

quicklooks includes a companion skill that teaches AI agents how to use the package consistently. Install it once after `pip install quicklooks`:

```python
import quicklooks as ql
ql.install_skill()
```

This auto-detects which agents are installed on your machine:

- **Cursor** — copies skill files to `~/.cursor/skills/ql-viz/`. Restart Cursor to activate.
- **Claude Code** — copies skill files to `~/.claude/quicklooks/` and adds an import line to `~/.claude/CLAUDE.md`.

If both are installed, both are set up in one call. Safe to re-run — it updates the skill files and won't duplicate the Claude Code import.

## Quick start

```python
import numpy as np
import quicklooks as ql

x = np.linspace(0, 10, 50)
y = np.sin(x) * 40 + 50
```

```python
# https://github.com/alexdsbreslav/quicklooks/blob/main/quicklooks/skill/reference.md
cs = ql.chart(
    title="Sine Wave",
    xlabel="X",
    ylabel="Y",
    x_min_max=(0, 10),
    y_min_max=(0, 100),
    xtick_interval=2,
    ytick_interval=20,
    size="notebook",
    colors="bloom",
    font="rubik",
    xtick_labels="default",
    ytick_labels="default",
    horizontal_gridlines=False,
    vertical_gridlines=False,
);

ql.line(cs,
    x=x,
    y=y,
    color="default",
    yerror=None,
    linewidth=3,
    linestyle="solid",
    marker=None,
    opacity=1,
    label="sin(x)",
    end_label=True,
    layer_order=1,
);
```

## API overview

| Function | Purpose |
|----------|---------|
| `ql.chart()` | Create the chart skeleton (axes, title, styling) |
| `ql.line()` | Add a line plot |
| `ql.area()` | Add a stacked area band |
| `ql.bar()` | Add a bar chart |
| `ql.stacked_bar()` | Add a segment to a stacked bar chart |
| `ql.scatter()` | Add a scatter plot |
| `ql.dist()` | Add a distribution (histogram / density) plot |
| `ql.refline()` | Add a reference line (horizontal, vertical, diagonal) |
| `ql.legend()` | Add a legend |
| `ql.text()` | Add a text annotation |
| `ql.save()` | Save the chart to disk |

## Color libraries

quicklooks ships with five color libraries: **extended**, **neon**, **sorbet**, **bloom**, and **hockney**. Pass the library name to `ql.chart()` and color names as strings to each plot function:

```python
cs = ql.chart(..., colors="bloom")
ql.line(cs, x=x, y=y, color="cornflower")
ql.line(cs, x=x, y=y2, color="purple")
```

## Acknowledgments

quicklooks is built on [matplotlib](https://matplotlib.org/), [NumPy](https://numpy.org/), [pandas](https://pandas.pydata.org/), [seaborn](https://seaborn.pydata.org/), [Open Color](https://yeun.github.io/open-color/), and [Figma's brand colors](https://www.figma.com/blog/bringing-new-life-to-figmas-brand/).
