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
# ---- create arbtrary data
rng = np.random.RandomState(1)
x_values = np.linspace(0,10,20)
blue_y_values = [i**2+rng.randint(-10,10) for i in x_values]
line_y_values = [i**2 for i in x_values]

# ---- create the chart skeleton
chart_skeleton = quicklook.build_chart_skeleton(
size = 'half_slide', #['print', 'half_slide', 'full_slide']
title = '',
xlabel = '',
ylabel = '',
x_min_max = (0,10), y_min_max = (-15,100),
xtick_interval = 1, ytick_interval = 10,
xtick_labels = 'default', #['default', 'percents', list]
ytick_labels = 'default', #['default', 'percents', list]
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# --- add horizontal reference line
ref_line = quicklook.add_reference_line(chart_skeleton,
line_type = 'horizontal', #['horizontal','vertical','diagonal_up','diagonal_down']
location = 0, #If diagonal_up or diagonal_down, None
color_name = 'text', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['light', 'default', 'dark']
linewidth = 3,
linestyle = ':', #['-', '--', ':', '-.']
marker_shape = 'None', #['None', 'o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label_for_legend = '',
layer_order = 1)

# --- add diagonal reference line
ref_line = quicklook.add_reference_line(chart_skeleton,
line_type = 'diagonal_up', #['horizontal','vertical','diagonal_up','diagonal_down']
location = None, #If diagonal_up or diagonal_down, None
color_name = 'text', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['light', 'default', 'dark']
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

## Note
- Extend across the entire plot automatically
- If `line_type` is 'diagonal_up' or 'diagonal_down', `location` is ignored
- If `line_type` is 'horizontal' or 'vertical', `location` is where the line is located on the appropriate axis
