---
name: quicklooks-viz
description: >-
  Create presentation-ready charts in Jupyter notebooks using the quicklooks
  package. Use when the user asks to visualize data, create charts, plot data,
  or mentions quicklooks, ql.chart, ql.line, ql.bar, ql.scatter, ql.dist,
  or any quicklooks function.
---

# quicklooks

quicklooks creates presentation-ready charts in Jupyter notebooks. One function
call per visual element. Every chart follows the same pattern:

1. Create a chart: `ql.chart()`
2. Add data elements: `ql.line()`, `ql.bar()`, `ql.scatter()`, `ql.dist()`
3. Annotate: `ql.legend()`, `ql.text()`, `ql.refline()`
4. Save (optional): `ql.save()`

## Agent instructions

Follow these rules strictly when writing quicklooks code:

1. **Markdown reference cell (one-time per notebook):** Before writing any
   quicklooks code into a notebook, check whether a cell containing
   "quicklooks options" already exists. If it does NOT exist, write the
   markdown cell shown below directly above your first code cell. If it
   already exists, do NOT write another one.

2. **Reproduce templates exactly.** Use the canonical code templates below
   character-for-character. Only change the data values and parameter values.
   Do NOT reformat, collapse lines, or reorder parameters.

3. **One parameter per line, always.** 4-space indent. Trailing comma after
   every parameter including the last.

4. **Always use keyword arguments.** Always include ALL parameters explicitly
   (even defaults) so the user can see and modify everything.

5. **Separate calls for each data series.** Use separate `ql.line()` /
   `ql.bar()` / `ql.scatter()` calls for each data series. Never use a loop
   unless the user explicitly asks for one.

6. **Always assign the chart to `cs`.** Not `chart`, not `chart_skeleton`.

7. **If the user pastes an error** or says something isn't working but the
   relevant code or output is not visible, ask the user to **save the notebook**
   (Cmd+S / Ctrl+S) before proceeding.

## Markdown reference cell

Write this cell once per notebook, above the first quicklooks code cell:

```markdown
## quicklooks options
| Parameter | Options |
|-----------|---------|
| size | "notebook", "half_slide", "full_slide" |
| colors | "extended", "neon", "gouache", "bloom", "hockney" |
| font | "rubik", "lato", "montserrat", "oswald", "roboto", "source_sans", "work_sans" |
| color | depends on library (see below) |
| linestyle | "solid", "dashed", "dotted", "dashdot" |
| marker | None, "o", "v", "^", "s", "d", "x", "D", "X" |
| xtick_labels | "default", "percents", "years", "quarters", "months", "weeks", "days" |
| ytick_labels | "default", "percents", "1k", "100k", "1m" |
| legend location | "best", "upper right", "upper left", "lower left", "lower right", "outside right", "below" |

**Colors by library:**
- **extended:** blue, red, green, orange, yellow, violet, indigo, cyan, teal, lime, pink, grape (plus light_/dark_ variants, gray, black, white)
- **neon:** blue, slate, teal, indigo, green, purple, orange, pink (plus gray, black, white)
- **gouache:** red, green, yellow, blue, pink, orange, lavender, teal (plus gray, black, white)
- **bloom:** blue, purple, periwinkle, cornflower, yellow, green, coral, red (plus gray, black, white)
- **hockney:** cobalt (default), turquoise, pink, navy, scarlet, cognac, cream, golden (plus gray, black, white)
```

## Canonical code templates

### Chart

```python
cs = ql.chart(
    title="",
    xlabel="",
    ylabel="",
    x_min_max=(0, 1),
    y_min_max=(0, 1),
    xtick_interval=0.25,
    ytick_interval=0.25,
    size="notebook",
    colors="extended",
    font="rubik",
    xtick_labels="default",
    ytick_labels="default",
    horizontal_gridlines=False,
    vertical_gridlines=False,
)
```

### Line

```python
ql.line(cs,
    x=x,
    y=y,
    color="blue",
    yerror=None,
    linewidth=3,
    linestyle="solid",
    marker=None,
    opacity=1,
    label="",
    end_label=True,
    layer_order=1,
)
```

### Bar

```python
ql.bar(cs,
    xlabels=xlabels,
    y=y,
    color="blue",
    yerror=None,
    bars_per_group=1,
    bar_index=0,
    opacity=1,
    label="",
    layer_order=1,
)
```

### Scatter

```python
ql.scatter(cs,
    x=x,
    y=y,
    color="blue",
    x_error=None,
    y_error=None,
    marker="o",
    opacity=1,
    label="",
    layer_order=1,
)
```

### Distribution

```python
ql.dist(cs,
    data=data,
    color="blue",
    dist_type="binned_counts",
    auto_fit=True,
    distribution_min_max=(None, None),
    bin_interval=None,
    opacity=1,
    label="",
    layer_order=1,
)
```

### Reference line

```python
ql.refline(cs,
    direction="horizontal",
    location=0,
    color="gray",
    linewidth=2,
    linestyle="dashed",
    marker=None,
    opacity=1,
    label="",
    layer_order=1,
)
```

### Legend

```python
ql.legend(cs,
    location="best",
    frame=False,
)
```

### Text

```python
ql.text(cs,
    text="",
    x=0,
    y=0,
    size="m",
    color="black",
    horizontal_align="center",
    vertical_align="center",
    rotation=0,
    box=False,
    layer_order=1,
)
```

### Save

```python
ql.save(cs,
    name="chart",
    folder="./",
    format="png",
)
```

## Full chart examples

### Line chart (multiple lines)

```python
import quicklooks as ql

cs = ql.chart(
    title="Revenue by Quarter",
    xlabel="Quarter",
    ylabel="Revenue",
    x_min_max=(0, 10),
    y_min_max=(0, 100),
    xtick_interval=2,
    ytick_interval=20,
    size="notebook",
    colors="extended",
    font="rubik",
    xtick_labels="default",
    ytick_labels="default",
    horizontal_gridlines=False,
    vertical_gridlines=False,
)

ql.line(cs,
    x=x,
    y=y_product_a,
    color="blue",
    yerror=None,
    linewidth=3,
    linestyle="solid",
    marker=None,
    opacity=1,
    label="Product A",
    end_label=True,
    layer_order=1,
)

ql.line(cs,
    x=x,
    y=y_product_b,
    color="red",
    yerror=None,
    linewidth=3,
    linestyle="solid",
    marker=None,
    opacity=1,
    label="Product B",
    end_label=True,
    layer_order=1,
)
```

### Grouped bar chart

```python
import quicklooks as ql

xlabels = ["Q1", "Q2", "Q3", "Q4"]

cs = ql.chart(
    title="Sales by Region",
    xlabel="",
    ylabel="Sales ($)",
    x_min_max=(0, 1),
    y_min_max=(0, 500),
    xtick_interval=0.25,
    ytick_interval=100,
    size="notebook",
    colors="extended",
    font="rubik",
    xtick_labels="default",
    ytick_labels="default",
    horizontal_gridlines=False,
    vertical_gridlines=False,
)

ql.bar(cs,
    xlabels=xlabels,
    y=y_east,
    color="blue",
    yerror=None,
    bars_per_group=2,
    bar_index=0,
    opacity=1,
    label="East",
    layer_order=1,
)

ql.bar(cs,
    xlabels=xlabels,
    y=y_west,
    color="orange",
    yerror=None,
    bars_per_group=2,
    bar_index=1,
    opacity=1,
    label="West",
    layer_order=1,
)

ql.legend(cs,
    location="upper right",
    frame=False,
)
```

### Timeseries

```python
import quicklooks as ql

cs = ql.chart(
    title="Daily Active Users",
    xlabel="",
    ylabel="Users",
    x_min_max=("2025-01-01", "2025-03-31"),
    y_min_max=(0, 1000),
    xtick_interval=14,
    ytick_interval=200,
    size="notebook",
    colors="extended",
    font="rubik",
    xtick_labels="days",
    ytick_labels="default",
    horizontal_gridlines=False,
    vertical_gridlines=False,
)

ql.line(cs,
    x=dates,
    y=dau,
    color="blue",
    yerror=None,
    linewidth=3,
    linestyle="solid",
    marker=None,
    opacity=1,
    label="DAU",
    end_label=True,
    layer_order=1,
)
```

## Additional resources

For the complete parameter reference for every function, see
[reference.md](reference.md).
