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

## Quick start

```python
import numpy as np
import quicklooks as ql

x = np.linspace(0, 10, 50)
y = np.sin(x) * 40 + 50

cs = ql.chart(
    title="Sine Wave",
    xlabel="X",
    ylabel="Y",
    x_min_max=(0, 10),
    y_min_max=(0, 100),
    xtick_interval=2,
    ytick_interval=20,
    size="notebook",
    colors="opencolor",
    font="rubik",
    xtick_labels="default",
    ytick_labels="default",
    horizontal_gridlines=False,
    vertical_gridlines=False,
)

ql.line(cs,
    x=x,
    y=y,
    color="blue",
    yerror=None,
    linewidth=3,
    linestyle="solid",
    marker=None,
    opacity=1,
    label="sin(x)",
    end_label=True,
    layer_order=1,
)
```

## API overview

| Function | Purpose |
|----------|---------|
| `ql.chart()` | Create the chart skeleton (axes, title, styling) |
| `ql.line()` | Add a line plot |
| `ql.bar()` | Add a bar chart |
| `ql.scatter()` | Add a scatter plot |
| `ql.dist()` | Add a distribution (histogram / density) plot |
| `ql.refline()` | Add a reference line (horizontal, vertical, diagonal) |
| `ql.legend()` | Add a legend |
| `ql.text()` | Add text annotation |
| `ql.save()` | Save the chart to disk |

Every function takes the chart object (`cs`) as its first argument. All other parameters are keyword-only with sensible defaults.

## Color libraries

quicklooks ships with four color libraries: **opencolor**, **mariglow**, **skygrove**, and **figma**. Pass color names as strings:

```python
ql.line(cs, x=x, y=y, color="blue")
ql.line(cs, x=x, y=y2, color="red")
```

## Cursor skill

quicklooks includes a companion Cursor skill that teaches AI agents how to use the package consistently. Install it once:

```python
import quicklooks as ql
ql.install_skill()
```

This copies the skill files to `~/.cursor/skills/quicklooks-viz/`. Restart Cursor and the skill will be active across all your projects.

## Acknowledgments

quicklooks is built on [matplotlib](https://matplotlib.org/), [NumPy](https://numpy.org/), [pandas](https://pandas.pydata.org/), [seaborn](https://seaborn.pydata.org/), [Open Color](https://yeun.github.io/open-color/), and [Figma's brand colors](https://www.figma.com/blog/bringing-new-life-to-figmas-brand/).
