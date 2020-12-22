## Add a distribution plot to your chart skeleton
To add a line to your chart, we will use the function:
```python
quicklook.add_distribution_plot
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. You should always copy the default code into your notebook from the documentation.
For tips on how to easily copy-and-paste quicklook code into your notebook, [click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md). 

## Basic Example
### Step 1: Quickly create a distribution plot using `override_chart_skeleton`
The `override_chart_skeleton` option will help you understand the shape and limits of your data. This is a great first step the first time you look at the distribution of a variable.

1. Make sure that quicklook is imported into your notebook.
2. Get your data! Here, I'll create some arbitrary data and save it as `variable1`.
3. Create your chart skeleton. 
    - [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
    - When you're using `override_chart_skeleton`, you can ignore the `x_min_max`, `y_min_max`, `xtick_interval`, and `ytick_interval`. We'll come back and fix those later.
4. Plot the distribution of your variable using `quicklook.add_distribution_plot` and `override_chart_skeleton = True`

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

When you use `override_chart_skeleton` you'll get a printout that looks something like:  
```
override_chart_skeleton is on.
Look at the automatic settings weve generated and update your code above with appropriate settings.
We highly recommend turning override_chart_skeleton off after updating your code.

Your build_chart_skeleton settings are automatically being set as:
- x_min_max = (-19.0, 27.0)
- y_min_max = (0.0, 19.0) 
- xtick_interval = 8.0
- ytick_interval = 4.0

Your add_distribution_plot settings are automatically being set as:
- distribution_min_max = (-19.0, 27.0)
- bin_interval = 4
```
At this point, we want to update all of our settings to create a neat, shareable, distribution plot. We'll set `override_chart_skeleton = False` and update all six settings listed above.

### Step 2: Clean up your distribution plot
```python
# ---- create arbitrary data
rng = np.random.RandomState(1)
variable1 = rng.normal(5, 10, size=100)

# ---- create chart skeleton
chart_skeleton = quicklook.build_chart_skeleton(size = 'default',
title = 'Plotting a Variable\'s Distribution',
xlabel = 'Value',
ylabel = 'Count',
x_min_max = (-30,30), y_min_max = (0,25),
xtick_interval = 5, ytick_interval = 5,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add distribution plot for blue variable
quicklook.add_distribution_plot(chart_skeleton,
data = variable1,
override_chart_skeleton = False,
distribution_min_max = (-30,30),
bin_interval = 5,
plot_as_density = False,
color_name = 'blue', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['default', 'light', 'dark']
opacity = 1,
label_for_legend = '',
layer_order = 1)
```
![basic_example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/histogram/simple.png)

Notice that the distribution looks slightly different than above. This is because we changed the `bin_interval` from 4 to 5 (because I thought intervals of 5 was more intuitive). 

## Complete Example
Let's compare the distribution of `variable1` to another variable. To accurately compare variables, I **strongly recommend**:
- Using the same `distribution_min_max` for both variables
- Using the same `bin_interval` for both variables
- Setting `plot_as_density == True` (density refers to a probability density; read through "Summarize Density With a Histogram
" in [this article](https://machinelearningmastery.com/probability-density-estimation/) by Jason Brownlee for more info)
- Setting `opacity = 0.5` so you can see overlapping parts

```python
# ---- create arbitrary data
rng = np.random.RandomState(1)
variable1 = rng.normal(5, 10, size=100)
variable2 = abs(rng.normal(25, 15, size=1000))

# ---- create chart skeleton
chart_skeleton = quicklook.build_chart_skeleton(size = 'default',
title = 'Compare Variables\' Distributions',
xlabel = 'Value',
ylabel = 'Density',
x_min_max = (-30,30), y_min_max = (0,0.05),
xtick_interval = 5, ytick_interval = 0.01,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add distribution plot for blue variable
quicklook.add_distribution_plot(chart_skeleton,
data = variable1,
override_chart_skeleton = False,
distribution_min_max = (-30,30),
bin_interval = 5,
plot_as_density = True,
color_name = 'blue', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['default', 'light', 'dark']
opacity = 0.5,
label_for_legend = 'Blue Variable',
layer_order = 1)

# ---- add distribution plot for orange variable
quicklook.add_distribution_plot(chart_skeleton,
data = variable2,
override_chart_skeleton = False,
distribution_min_max = (-30,30),
bin_interval = 5,
plot_as_density = True,
color_name = 'orange', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['default', 'light', 'dark']
opacity = 0.5,
label_for_legend = 'Orange Variable',
layer_order = 2)

# ---- add legend
quicklook.add_reference_legend(chart_skeleton,
legend_location = 'best', frame_around_legend=False);

# ---- save plot
quicklook.save_chart_to_computer(chart_name = 'compare',
                     path_to_folder_to_save_chart_in = fp.join(fp.abspath('images'), 'plots', 'histogram'),
                     print_confirmation=True);
```
![complete_example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/histogram/compare.png)

## Style options
- `color_name` can be 'gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange'
- `color_brightness` can be 'default', 'light', or 'dark'
- `opacity` can be any number between 0 and 1
- `label_for_legend` is the name of the line; this will show up in the legend when you add one.
- `layer_order` can be any number. Layers are drawn from low to high numbers; this means that a line with `layer_order = 2` will be drawn on top of `layer_order = 1`. If you leave `layer_order = 1` for all lines, the lines will be drawn in the order that they show up in your code.
