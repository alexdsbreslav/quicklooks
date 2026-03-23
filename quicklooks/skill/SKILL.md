---
name: ql-viz
description: >-
  Create presentation-ready charts in Jupyter notebooks using the quicklooks
  package. Use when the user asks to visualize data, create charts, plot data,
  or mentions quicklooks, ql.chart, ql.line, ql.bar, ql.scatter, ql.dist,
  or any quicklooks function.
---

# quicklooks

quicklooks creates presentation-ready charts in Jupyter notebooks. One function
call per visual element. Follow the step-by-step procedure below.

## Ground rules

- Copy templates exactly — only change values. Never reformat, reorder, or collapse lines.
- One parameter per line, 4-space indent, trailing comma on every parameter including the last.
- Always use keyword arguments. Always include ALL parameters explicitly.
- End every call with a semicolon: `ql.chart(...);`
- NEVER import other packages into the cell.
- NEVER define intermediate variables for data — pass expressions directly as arguments
  (e.g. `x=df[df.region == "APAC"].value.values`, not `apac = df[...]` then `x=apac`).
- If the user pastes an error but code/output isn't visible, ask them to save (Cmd+S) first.

## Step 1 — Reference link comment

The first line of every quicklooks code cell must be:

```python
# https://github.com/alexdsbreslav/quicklooks/blob/main/quicklooks/skill/reference.md
```

## Step 2 — Create the chart skeleton with `ql.chart()`

```python
cs = ql.chart(
    title="",                    # always write a descriptive title
    xlabel="",                   # always write axis labels
    ylabel="",
    x_min_max=(0, 10),           # literal tuple only — no variables or expressions
                                 # TIMESERIES: use date strings ("YYYY-MM-DD", "YYYY-MM-DD")
                                 # NON-TIMESERIES: must be divisible by xtick_interval
    y_min_max=(0, 100),          # literal tuple only — no variables or expressions
                                 # based on SINGLE series max, NOT the sum across series
                                 # y_min_max[1] MUST be divisible by ytick_interval (no partial tick)
    xtick_interval=1,            # NON-TIMESERIES: xrange / N where N = 5–10, clean round number
                                 # x_min_max[1] must be divisible by this — round up if needed
                                 # TIMESERIES: interval that gives 5–15 ticks for "days"; 1 for all others
    ytick_interval=10,           # PICK THIS FIRST: clean round number giving 5–10 ticks for the data range
                                 # THEN set y_min_max[1] = ceil(data_max / ytick_interval) * ytick_interval
    size="notebook",             # "notebook" | "wide" | "presentation"
    colors="bloom",              # "extended" | "neon" | "sorbet" | "bloom" | "hockney"
                                 # see reference.md for the exact color names in each library
    font="rubik",                # "rubik" | "default"
    xtick_labels="default",      # NON-TIMESERIES: "default"
                                 # TIMESERIES: "days" (<4 wks) | "weeks" (4 wks–2 mo) |
                                 #             "months" (2–15 mo) | "quarters" (9 mo–4 yr) | "years" (>4 yr)
    ytick_labels="default",      # "default" | ">1k" → "1k" | ">100k" → "100k" | ">1M" → "1m" | percentages → "percents"
    horizontal_gridlines=False,
    vertical_gridlines=False,
);
```

## Step 3 — Add data elements

For 1–2 series, write separate calls. For 3+ series of the same type, use a `for` loop
with `enumerate`. Define a color array before the loop — **names must exist in the active
color library** (check reference.md). Use the column name as `label`.

### `ql.line()`

```python
ql.line(cs,
    x=x,                # TIMESERIES: pass date objects (DatetimeIndex / datetime Series), NOT strings
    y=y,
    color="blue",       # must be a valid name in the active color library — check reference.md
    yerror=None,
    linewidth=3,
    linestyle="solid",
    marker=None,
    opacity=1,
    label="",
    end_label=True,     # prefer True; if 2+ lines end near the same y value, set False on ALL
                        # lines and add ql.legend() instead — never mix end labels and a legend
    layer_order=1,
);
```

### `ql.bar()`

```python
ql.bar(cs,
    xlabels=xlabels,    # any series — strings, dates, and numbers all work
    y=y,
    color="blue",       # must be a valid name in the active color library — check reference.md
    yerror=None,
    bars_per_group=1,   # total bars at each x position (e.g. 3 for a grouped bar chart)
    bar_index=0,        # 0-indexed position of this bar within the group
    opacity=1,
    label="",
    layer_order=1,
);
```

### `ql.scatter()`

```python
ql.scatter(cs,
    x=x,
    y=y,
    color="blue",       # must be a valid name in the active color library — check reference.md
    x_error=None,
    y_error=None,
    marker="o",
    opacity=1,
    label="",
    layer_order=1,
);
```

### `ql.dist()`

```python
ql.dist(cs,
    data=data,
    color="blue",       # must be a valid name in the active color library — check reference.md
    dist_type="binned_counts",
    auto_fit=True,
    distribution_min_max=(None, None),
    bin_interval=None,
    opacity=1,
    label="",
    layer_order=1,
);
```

## Step 4 — Annotate (if needed)

### `ql.legend()`

```python
ql.legend(cs,
    location="outside right",
    frame=False,
);
```

### `ql.text()`

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
);
```

### `ql.refline()`

```python
ql.refline(cs,
    direction="horizontal",
    location=0,
    color="black",
    linewidth=1,
    linestyle="dashed",
    marker=None,
    opacity=1,
    label="",
    end_label=False,    # True draws the label at the end of the line
    layer_order=1,
);
```

## Step 5 — Save (if requested)

```python
ql.save(cs,
    name="chart",
    folder="./",
    format="png",
);
```

## Step 6 — Validate before finishing

After writing the cell, add a new cell below with:

```python
ql.validate_cell(In[-2])
```

`In[-2]` grabs the source of the cell you just wrote. If the list is empty, the cell
passes. Fix every violation before proceeding, then delete the validation cell.

## Additional resources

For the complete parameter reference for every function, see
[reference.md](reference.md).
