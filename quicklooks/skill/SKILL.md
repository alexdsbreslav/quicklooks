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
call per visual element. Every chart follows the same pattern:

1. Create a chart: `ql.chart()`
2. Add data elements: `ql.line()`, `ql.bar()`, `ql.scatter()`, `ql.dist()`
3. Annotate: `ql.legend()`, `ql.text()`, `ql.refline()`
4. Save (optional): `ql.save()`

## Agent instructions when writing quicklooks code

Follow these rules strictly when writing quicklooks code:

1. **Reproduce templates exactly.** Use the canonical code templates below
   character-for-character. Only change the data values and parameter values.
   Do NOT reformat, collapse lines, or reorder parameters.

2. **One parameter per line, always.** 4-space indent. Trailing comma after
   every parameter including the last.

3. **Always use keyword arguments.** Always include ALL parameters explicitly
   (even defaults) so the user can see and modify everything.

4. **Separate calls for each data series.** Use separate `ql.line()` /
   `ql.bar()` / `ql.scatter()` calls for each data series. Never use a loop
   unless the user explicitly asks for one.

5. **Always assign the chart to `cs`.** Not `chart`, not `chart_skeleton`.

6. **If the user pastes an error** or says something isn't working but the
   relevant code or output is not visible, ask the user to **save the notebook**
   (Cmd+S / Ctrl+S) before proceeding.

7. NEVER import other packages into the cell

## Agent instructions for determining and writing data and parameter values

### cs

1. Always write a title, xlabel, and ylabel.
2. Hard-code every min_max as a literal tuple — never use variables or expressions.
3. **Validation constraint:** every axis must have between 2 and 20 ticks.
   The code enforces `range / 20 <= tick_interval <= range`. Violating this
   raises an error. Aim for 5-10 ticks with round numbers.

4. **y_min_max and ytick_interval (all chart types):**
    1. Find the min and max y values across all series.
    2. Set y_min_max[0] to 0 (or the data min rounded down, if values go negative).
    3. Set y_min_max[1] so the data max sits at roughly 80% of the axis.
       Formula: `y_max_axis = data_max / 0.8`, then round up to the nearest
       clean number.
    4. Compute yrange = y_min_max[1] - y_min_max[0].
    5. Set ytick_interval = yrange / N where N is 5-10; pick the cleanest
       round number. Must be an integer unless the range is < 1.

5. **x_min_max and xtick_interval for NON-timeseries data:**
    1. Find the min and max x values; set x_min_max to cover the range,
       rounding to clean numbers.
    2. Compute xrange = x_min_max[1] - x_min_max[0].
    3. Set xtick_interval = xrange / N where N is 5-10; pick the cleanest
       round number. Must be an integer unless the range is < 1.

6. **x_min_max and xtick_labels for TIMESERIES data:**
    1. Hard-code x_min_max as date strings: ("YYYY-MM-DD", "YYYY-MM-DD").
    2. Compute the date range in days / months.
    3. Choose xtick_labels based on the date range (these constraints are
       enforced by validation — choosing wrong will error):
        - Under ~4 weeks: use "days" with xtick_interval that gives 5-15 ticks
        - 4 weeks to 2 months: use "weeks" with xtick_interval=1
        - 2-15 months: use "months" with xtick_interval=1
        - 9 months to 4 years: use "quarters" with xtick_interval=1
        - Over 4 years: use "years" with xtick_interval=1

7. **ytick_labels formatting:**
    - Values > 1,000,000: set ytick_labels="1m"
    - Values > 100,000: set ytick_labels="100k"
    - Values > 1,000: set ytick_labels="1k"
    - Values are percentages (0-1 or 0-100): set ytick_labels="percents"
    - Otherwise: leave as "default"

### line

Do not add a legend call if end_label=True (the labels already appear on the plot).


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
    location="outside right",
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

## Additional resources

For the complete parameter reference for every function, see
[reference.md](reference.md).