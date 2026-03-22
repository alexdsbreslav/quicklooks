# quicklooks parameter reference

Complete reference for every quicklooks function. All parameters shown with
their default values.

## ql.chart()

Creates the chart skeleton. Returns a `Chart` object to pass to all other functions.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| title | str | "" | Chart title |
| xlabel | str | "" | X-axis label |
| ylabel | str | "" | Y-axis label |
| x_min_max | tuple | (0, 1) | X-axis range. For timeseries: ("YYYY-MM-DD", "YYYY-MM-DD") |
| y_min_max | tuple | (0, 1) | Y-axis range |
| xtick_interval | int/float | 0.25 | Spacing between x-axis ticks |
| ytick_interval | int/float | 0.25 | Spacing between y-axis ticks |
| size | str | "notebook" | "notebook", "half_slide", "full_slide" |
| colors | str | "extended" | "extended", "neon", "gouache", "bloom", "hockney" |
| font | str | "rubik" | "rubik", "lato", "montserrat", "oswald", "roboto", "source_sans", "work_sans" |
| xtick_labels | str/list | "default" | "default", "percents", "years", "quarters", "months", "weeks", "days", or list of strings |
| ytick_labels | str/list | "default" | "default", "percents", "1k", "100k", "1m", or list of strings |
| horizontal_gridlines | bool | False | Show horizontal grid lines |
| vertical_gridlines | bool | False | Show vertical grid lines |

## ql.line()

Adds a line to the chart.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| chart | Chart | required | Chart object (positional) |
| x | array | required | 1D array of x values |
| y | array | required | 1D array of y values |
| color | str/tuple | "default" | Color name or (fill, line, edge) tuple |
| yerror | array/None | None | 1D array of y-error magnitudes |
| linewidth | int/float | 3 | Line width |
| linestyle | str | "solid" | "solid", "dashed", "dotted", "dashdot" |
| marker | str/None | None | None, "o", "v", "^", "s", "d", "x", "D", "X" |
| opacity | float | 1 | Transparency (0-1) |
| label | str | "" | Legend and end-label text |
| end_label | bool | True | Draw label at end of line |
| layer_order | int | 1 | Z-order (higher = on top) |

## ql.bar()

Adds bars to the chart. Call once per group in a grouped bar chart.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| chart | Chart | required | Chart object (positional) |
| xlabels | array | required | 1D array of category labels |
| y | array | required | 1D array of bar heights |
| color | str/tuple | "default" | Color name or (fill, line, edge) tuple |
| yerror | array/None | None | 1D array of y-error magnitudes |
| bars_per_group | int | 1 | Total bars at each x-label |
| bar_index | int | 0 | This bar's index (0 to bars_per_group-1) |
| opacity | float | 1 | Transparency (0-1) |
| label | str | "" | Legend text |
| layer_order | int | 1 | Z-order (higher = on top) |

## ql.scatter()

Adds a scatter plot. Error display depends on which error arrays are provided.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| chart | Chart | required | Chart object (positional) |
| x | array | required | 1D array of x values |
| y | array | required | 1D array of y values |
| color | str/tuple | "default" | Color name or (fill, line, edge) tuple |
| x_error | array/None | None | 1D array of x-error magnitudes |
| y_error | array/None | None | 1D array of y-error magnitudes |
| marker | str | "o" | "o", "v", "^", "s", "d", "x", "D", "X" |
| opacity | float | 1 | Transparency (0-1) |
| label | str | "" | Legend text |
| layer_order | int | 1 | Z-order (higher = on top) |

Error behavior:
- Both x_error + y_error: error ellipses
- Only x_error: horizontal error bars
- Only y_error: vertical error bars

## ql.dist()

Adds a distribution (histogram or density) plot.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| chart | Chart | required | Chart object (positional) |
| data | array | required | 1D array of values |
| color | str/tuple | "default" | Color name or (fill, line, edge) tuple |
| dist_type | str | "binned_counts" | "binned_counts", "binned_density", "smooth_density" |
| auto_fit | bool | True | Auto-compute axis limits and bins |
| distribution_min_max | tuple | (None, None) | Manual bin range (when auto_fit=False) |
| bin_interval | float/None | None | Manual bin width (when auto_fit=False) |
| opacity | float | 1 | Transparency (0-1) |
| label | str | "" | Legend text |
| layer_order | int | 1 | Z-order (higher = on top) |

## ql.refline()

Adds a reference line (horizontal, vertical, or diagonal).

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| chart | Chart | required | Chart object (positional) |
| direction | str | "horizontal" | "horizontal", "vertical", "diagonal_up", "diagonal_down" |
| location | number/str | 0 | Position on axis. Ignored for diagonal. For timeseries: "YYYY-MM-DD" |
| color | str/tuple | "gray" | Color name or (fill, line, edge) tuple |
| linewidth | int/float | 2 | Line width |
| linestyle | str | "dashed" | "solid", "dashed", "dotted", "dashdot" |
| marker | str/None | None | None, "o", "v", "^", "s", "d", "x", "D", "X" |
| opacity | float | 1 | Transparency (0-1) |
| label | str | "" | Legend text |
| layer_order | int | 1 | Z-order (higher = on top) |

## ql.legend()

Adds a legend to the chart.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| chart | Chart | required | Chart object (positional) |
| location | str | "best" | "best", "upper right", "upper left", "lower left", "lower right", "right", "center left", "center right", "lower center", "upper center", "center", "outside right", "below" |
| frame | bool | False | Draw border around legend |

## ql.text()

Adds text annotation to the chart.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| chart | Chart | required | Chart object (positional) |
| text | str | "" | Text to display |
| x | number/str | 0 | X position. For timeseries: "YYYY-MM-DD" |
| y | number | 0 | Y position |
| size | str/number | "m" | "xl", "l", "m", "s", or numeric point size |
| color | str/tuple | "black" | Color name or (fill, line, edge) tuple |
| horizontal_align | str | "center" | "center", "left", "right" |
| vertical_align | str | "center" | "center", "top", "bottom" |
| rotation | int/float | 0 | Rotation in degrees |
| box | bool | False | Draw box around text |
| layer_order | int | 1 | Z-order (higher = on top) |

## ql.save()

Saves the chart to disk.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| chart | Chart | required | Chart object (positional) |
| name | str | "chart" | File name (without extension) |
| folder | str | "./" | Directory to save into |
| format | str | "png" | "png", "pdf", "svg", "jpg" |

## Color libraries

### extended
blue, red, green, orange, yellow, violet, indigo, cyan, teal, lime, pink, grape

Each has light_ and dark_ variants: light_blue, dark_blue, etc.

Utility colors: light_gray, gray, dark_gray, black, white

### neon
blue (default), slate, teal, indigo, green, purple, orange, pink

Utility colors: light_gray, gray, dark_gray, black, white

### gouache
red (default), green, yellow, blue, pink, orange, lavender, teal

Utility colors: light_gray, gray, dark_gray, black, white

### bloom
blue (default), purple, periwinkle, cornflower, yellow, green, coral, red

Utility colors: light_gray, gray, dark_gray, black, white

### hockney
cobalt (default), turquoise, pink, navy, scarlet, cognac, cream, golden

Utility colors: light_gray, gray, dark_gray, black, white
