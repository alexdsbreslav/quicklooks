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
call per visual element. Follow the step-by-step procedure below to write a
quicklooks cell.

## Ground rules

These apply to every quicklooks call you write:

- Copy the templates below exactly — only change data and parameter values.
  Do NOT reformat, collapse lines, or reorder parameters.
- One parameter per line, 4-space indent, trailing comma after every parameter
  including the last.
- Always use keyword arguments. Always include ALL parameters explicitly
  (even defaults) so the user can see and modify everything.
- End every call with a semi-colon: `ql.line(...);`
- NEVER import other packages into the cell.
- If the user pastes an error but the relevant code or output is not visible,
  ask the user to save the notebook (Cmd+S / Ctrl+S) before proceeding.

## Step 1 — Reference link comment

The first line of every quicklooks code cell must be:

```python
# https://github.com/alexdsbreslav/quicklooks/blob/main/quicklooks/skill/reference.md
```

## Step 2 — Create the chart skeleton with `ql.chart()`

Copy this template and fill in the parameter values:
`
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
);
```

### How to choose chart parameter values

1. Always write a title, xlabel, and ylabel.
2. Hard-code every min_max as a literal tuple — never use variables or expressions.
3. **Validation constraint:** every axis must have between 2 and 20 ticks.
   The code enforces `range / 20 <= tick_interval <= range`. Violating this
   raises an error. Aim for 5-10 ticks with round numbers.
4. **Before choosing y_min_max, determine the actual range of each individual
   series that will be plotted.** Read the data-generation code carefully.
   y_min_max must cover the range of the *single* series with the largest
   values — NOT the sum or aggregate across all series. For example, if
   4 regions each have values 0-700, y_min_max should be based on 700, not
   2800. Getting this wrong makes the chart unreadable.
5. **y_min_max and ytick_interval:**
    1. Use the per-series min and max y values determined above.
    2. Set y_min_max[0] to 0 (or the data min rounded down, if values go negative).
    3. Pick ytick_interval first: choose a clean round number that would give
       5-10 ticks for the data range. Must be an integer unless the range is < 1.
    4. Set y_min_max[1] so the data max sits at roughly 90% of the axis AND
       y_min_max[1] is evenly divisible by ytick_interval (no partial tick at
       the top). Round up to the next multiple of ytick_interval if needed.
6. **x_min_max and xtick_interval for NON-timeseries data:**
    1. Find the min and max x values; set x_min_max to cover the range,
       rounding to clean numbers.
    2. Compute xrange = x_min_max[1] - x_min_max[0].
    3. Set xtick_interval = xrange / N where N is 5-10; pick the cleanest
       round number. Must be an integer unless the range is < 1.
7. **x_min_max and xtick_labels for TIMESERIES data:**
    1. Hard-code x_min_max as date strings: ("YYYY-MM-DD", "YYYY-MM-DD").
    2. Compute the date range in days / months.
    3. Choose xtick_labels based on the date range (these constraints are
       enforced by validation — choosing wrong will error):
        - Under ~4 weeks: use "days" with xtick_interval that gives 5-15 ticks
        - 4 weeks to 2 months: use "weeks" with xtick_interval=1
        - 2-15 months: use "months" with xtick_interval=1
        - 9 months to 4 years: use "quarters" with xtick_interval=1
        - Over 4 years: use "years" with xtick_interval=1
8. **ytick_labels formatting:**
    - Values > 1,000,000: set ytick_labels="1m"
    - Values > 100,000: set ytick_labels="100k"
    - Values > 1,000: set ytick_labels="1k"
    - Values are percentages (0-1 or 0-100): set ytick_labels="percents"
    - Otherwise: leave as "default"

## Step 3 — Add data elements

Pick the template that matches the chart type the user wants. Copy it exactly
and fill in the data and parameter values.

For 1-2 series, write separate calls. For 3 or more series of the same type,
use a `for` loop with `enumerate` over the columns. Define an array of color
names before the loop and index into it with the loop counter. Use the column
name as the `label`. The color names in the array must exist in the color
library set in `ql.chart()` — check reference.md for available names per library.

### `ql.line()`

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
);
```

**Choosing line parameter values:**

- Prefer end_label=True — it places the series name at the end of each line,
  which is cleaner than a separate legend.
- If end labels would overlap (multiple lines ending at similar y values),
  set end_label=False on every line and add a `ql.legend()` call instead.
- Never combine end labels and a legend on the same chart.
- For timeseries lines, always pass the date object (e.g. a datetime Series
  or DatetimeIndex) as x — never pass date strings.

### `ql.bar()`

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
);
```

**Choosing bar parameter values:**

- xlabels can take any series, they do not need to be strings (e.g. a datetime Series
  or DatetimeIndex)

### `ql.scatter()`

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
);
```

### `ql.dist()`

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
    color="gray",
    linewidth=2,
    linestyle="dashed",
    marker=None,
    opacity=1,
    label="",
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

After writing the cell, run the built-in validator to catch template
deviations. Add a new cell below with:

```python
ql.validate_cell(In[-2])
```

`In[-2]` grabs the source of the cell you just wrote (the one before this
validation cell). If the list is empty, the cell passes. If violations are
returned, go back and fix every one before proceeding. Delete the validation
cell when the output is clean.

## Additional resources

For the complete parameter reference for every function, see
[reference.md](reference.md).
