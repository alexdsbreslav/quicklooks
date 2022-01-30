# Add a legend to your chart skeleton
To add a legend to your chart, we will use the function:
```python
quicklook.add_legend
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. You should always copy the default code into your notebook from the documentation.
For tips on how to easily copy-and-paste quicklook code into your notebook, [click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md).

## Prerequisites for adding a legend to your chart
The add_legend function looks for plots that you've added to your chart skeleton and **labeled** and then puts those plots and labels into a legend.
1. You must have a chart skeleton.
2. Your chart skeleton must have one or more plots added to it.
3. Those plots must be labeled!
4. The code `quicklook.add_legend` must come after your chart skeleton and plots.

## Example:
1. Make sure that quicklook is imported into your notebook.
2. Create your chart skeleton. [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
3. Plot and label your data.
4. Add the legend using `quicklook.add_legend`

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

# --- add blue circles
scatter = quicklook.add_scatter_plot(chart_skeleton,
x = x_values,
y = blue_y_values,
x_error = None, #If no values, None
y_error = None, #If no values, None
color_name = 'blue', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['light', 'default', 'dark']
marker_shape = 'o', #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x', '']
opacity = 1,
label_for_legend = 'Blue Circles',
layer_order = 2)

# --- add orange line
line = quicklook.add_line_plot(chart_skeleton,
x = x_values,
y = line_y_values,
y_error = None, #If no values, None
color_name = 'orange', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['light', 'default', 'dark']
linewidth = 7,
linestyle = '-', #['-', '--', ':', '-.']
marker_shape = '', #['None', 'o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 0.5,
label_for_legend = 'Orange Line',
layer_order = 1)

# --- add legend
legend = quicklook.add_legend(chart_skeleton,
legend_location = 'best', frame_around_legend=False);
```
![example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/legend/example.png)
## Style options
- `legend_location` can be 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
- `frame_around_legend` can be True or False
