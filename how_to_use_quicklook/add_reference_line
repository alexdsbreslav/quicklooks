# Add a reference line to your chart skeleton
To add a reference line to your chart, we will use the function:
```python
quicklook.add_reference_line
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. You should always copy the default code into your notebook from the documentation.
For tips on how to easily copy-and-paste quicklook code into your notebook, [click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md). 

## Example:
1. Make sure that quicklook is imported into your notebook.
2. Create your chart skeleton. [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
3. Plot some data.
4. Add a reference line using `quicklook.add_reference_line`

```python
import pandas as pd
import numpy as np
import os
import quicklook
```
```python
# ---- create the chart skeleton
chart_skeleton = quicklook.build_chart_skeleton(size = 'default',
title = 'Add a Legend to My Chart',
xlabel = 'X Values',
ylabel = 'Y\nValues',
x_min_max = (0,10), y_min_max = (-15,100),
xtick_interval = 1, ytick_interval = 10,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add a horizontal reference line
quicklook.add_reference_line(chart_skeleton,
line_type = 'horizontal', #['horizontal','vertical','diagonal_up','diagonal_down']
location = 0,
color_name = 'gray', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'dark', #['default', 'light', 'dark']
linewidth = 3,
linestyle = ':', #['-', '--', ':', '-.']
marker_shape = 'None', #['None', 'o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label_for_legend = '',
layer_order = 1)

# ---- add a diagonal reference line
quicklook.add_reference_line(chart_skeleton,
line_type = 'diagonal_up', #['horizontal','vertical','diagonal_up','diagonal_down']
location = None,
color_name = 'gray', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'dark', #['default', 'light', 'dark']
linewidth = 3,
linestyle = ':', #['-', '--', ':', '-.']
marker_shape = 'None', #['None', 'o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label_for_legend = '',
layer_order = 1)

# ---- plot some data...
# ---- this code has been removed for simplicity ----

# ---- add legend
# ---- this code has been removed for simplicity ----
```
![example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/legend/ref_line.png)

Notice that reference lines:
- Extend across the entire plot automatically
- If `line_type` is 'diagonal_up' or 'diagonal_down', `location` is ignored
- If `line_type` is 'horizontal' or 'vertical', `location` is where the line is located on the appropriate axis

## Style options
- `color_name` can be 'gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange'
- `color_brightness` can be 'default', 'light', or 'dark'
- `linewidth` can be any number
- `linestyle` can be '-', '--', ':', '-.' ([click here](https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html) to see an example of each line style)
- `marker_shape` can be 'o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x' ([click here](https://matplotlib.org/api/markers_api.html) to see an example of each marker shape)
  - If you set marker_shape to '', there will not be any markers, just the line.
- `opacity` can be any number between 0 and 1
- `label_for_legend` is the name of the line; this will show up in the legend when you add one.
- `layer_order` can be any number. Layers are drawn from low to high numbers; this means that a line with `layer_order = 2` will be drawn on top of `layer_order = 1`. If you leave `layer_order = 1` for all lines, the lines will be drawn in the order that they show up in your code.
