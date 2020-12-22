## Add a distribution plot to your chart skeleton
To add a line to your chart, we will use the function:
```python
quicklook.add_distribution_plot
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. You should always copy the default code into your notebook from the documentation.
For tips on how to easily copy-and-paste quicklook code into your notebook, [click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md). 

## Using `autofit` as a first step:
The `autofit` option will help you understand the shape and limits of your data. This is a great first step the first time you look at the distribution of a variable.

1. Make sure that quicklook is imported into your notebook.
2. Get your data! Here, I'll create some arbitrary data and save it as `variable1`.
3. Create your chart skeleton. 
    - [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
    - When you're using `autofit`, you can ignore the `x_min_max`, `y_min_max`, `xtick_interval`, and `ytick_interval`. We'll come back and fix those later.
4. Plot the distribution of your variable using `quicklook.add_distribution_plot` and `autofit = True`

```python
import pandas as pd
import numpy as np
import os
import quicklook
```
```python
# ---- create arbitrary data
rng = np.random.RandomState(1)
variable1 = rng.normal(5, 10, size=100)

# ---- create chart skeleton
chart_skeleton = quicklook.build_chart_skeleton(size = 'default',
title = '',
xlabel = '',
ylabel = '',
x_min_max = (0,1), y_min_max = (0,1),
xtick_interval = 0.25, ytick_interval = 0.25,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add distribution plot for blue variable using override_chart_skeleton
quicklook.add_distribution_plot(chart_skeleton,
data = variable1,
override_chart_skeleton = True,
distribution_min_max = (None,None),
bin_interval = None,
plot_as_pdf = False,
color_name = 'blue', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['default', 'light', 'dark']
opacity = 1,
label_for_legend = '',
layer_order = 1)
```
![override_chart_skeleton](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/histogram/override_chart_skeleton.png)

## Style options
- `color_name` can be 'gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange'
- `color_brightness` can be 'default', 'light', or 'dark'
- `opacity` can be any number between 0 and 1
- `label_for_legend` is the name of the line; this will show up in the legend when you add one.
- `layer_order` can be any number. Layers are drawn from low to high numbers; this means that a line with `layer_order = 2` will be drawn on top of `layer_order = 1`. If you leave `layer_order = 1` for all lines, the lines will be drawn in the order that they show up in your code.
