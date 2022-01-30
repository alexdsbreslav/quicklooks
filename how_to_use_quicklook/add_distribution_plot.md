# Add a distribution plot to your chart skeleton
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
chart_skeleton = quicklook.build_chart_skeleton(
size = 'half_slide', #['print', 'half_slide', 'full_slide']
title = 'Making a Distribution Plot',
xlabel = 'Values',
ylabel = 'Counts',
x_min_max = (0,1), y_min_max = (0,1),
xtick_interval = 0.25, ytick_interval = 0.25,
xtick_labels = 'default', #['default', 'percents', list]
ytick_labels = 'default', #['default', 'percents', list]
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add distribution plot for blue variable using override_chart_skeleton
dist = quicklook.add_distribution_plot(chart_skeleton,
data = variable1,
override_chart_skeleton = True,
distribution_min_max = (None,None),
bin_interval = None, #If dist_type is smooth_density, None
dist_type = 'binned_counts', #['binned_counts', 'binned_density', 'smooth_density']
color_name = 'blue', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['light', 'default', 'dark']
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
chart_skeleton = quicklook.build_chart_skeleton(
size = 'half_slide', #['print', 'half_slide', 'full_slide']
title = 'Making a Distribution Plot',
xlabel = 'Values',
ylabel = 'Counts',
x_min_max = (-30,30), y_min_max = (0,25),
xtick_interval = 5, ytick_interval = 5,
xtick_labels = 'default', #['default', 'percents', list]
ytick_labels = 'default', #['default', 'percents', list]
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add distribution plot for blue variable using override_chart_skeleton
dist = quicklook.add_distribution_plot(chart_skeleton,
data = variable1,
override_chart_skeleton = False,
distribution_min_max = (-30,30),
bin_interval = 5, #If dist_type is smooth_density, None
dist_type = 'binned_counts', #['binned_counts', 'binned_density', 'smooth_density']
color_name = 'blue', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['light', 'default', 'dark']
opacity = 1,
label_for_legend = '',
layer_order = 1)
```
![basic_example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/histogram/simple.png)

Notice that the distribution looks slightly different than above. This is because we changed the `bin_interval` from 4 to 5 (because I thought intervals of 5 was more intuitive).

## Complete Example
1. Make sure that quicklook is imported into your notebook.
2. Get your data! Here, I'll create some arbitrary data.
3. Create your chart skeleton.
   - [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
4. Add multiple distributions using `quicklook.add_distribution_plot` and adjust the style options.
5. Add a legend.
   - [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/add_legend.md) for more details on adding a legend to your chart
6. Save the chart to your computer.
    - [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/save_chart_to_your_computer.md) for more details on how to save your chart to your computer.

To accurately compare multiple distributions, I **strongly recommend**:
- Using the same `distribution_min_max` for both variables
- Using the same `bin_interval` for both variables
- Setting `dist_type = 'binned_density'` (density refers to a probability density<sup>*</sup>)
- Setting `opacity = 0.5` so you can see overlapping parts

<sup>*</sup>For more info, [right-click here](https://machinelearningmastery.com/probability-density-estimation/) to open an article by Jason Brownlee and read through "Summarize Density with a Histogram".
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
variable2 = abs(rng.normal(25, 15, size=1000))

# ---- create chart skeleton
chart_skeleton = quicklook.build_chart_skeleton(
size = 'half_slide', #['print', 'half_slide', 'full_slide']
title = 'Making a Distribution Plot',
xlabel = 'Values',
ylabel = 'Density',
x_min_max = (-30,30), y_min_max = (0,0.05),
xtick_interval = 5, ytick_interval = 0.01,
xtick_labels = 'default', #['default', 'percents', list]
ytick_labels = 'default', #['default', 'percents', list]
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add distribution plot for blue variable
dist = quicklook.add_distribution_plot(chart_skeleton,
data = variable1,
override_chart_skeleton = False,
distribution_min_max = (-30,30),
bin_interval = 5, #If dist_type is smooth_density, None
dist_type = 'binned_density', #['binned_counts', 'binned_density', 'smooth_density']
color_name = 'blue', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['light', 'default', 'dark']
opacity = 0.5,
label_for_legend = 'Blue variable',
layer_order = 1)

# ---- add distribution plot for orange variable
dist = quicklook.add_distribution_plot(chart_skeleton,
data = variable2,
override_chart_skeleton = False,
distribution_min_max = (-30,30),
bin_interval = 5, #If dist_type is smooth_density, None
dist_type = 'binned_density', #['binned_counts', 'binned_density', 'smooth_density']
color_name = 'orange', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['light', 'default', 'dark']
opacity = 0.5,
label_for_legend = 'Orange variable',
layer_order = 1)

# ---- add legend
legend = quicklook.add_legend(chart_skeleton,
legend_location = 'best', frame_around_legend=False);
# ---- save plot
quicklook.save_chart_to_computer(chart_skeleton,
                     chart_name = 'compare',
                     path_to_folder_to_save_chart_in = os.path.join(img_output, 'plots', 'histogram'),
                     print_confirmation=False)
```
![complete_example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/histogram/compare.png)

# Note
I did not show an example with `dist_type = 'smooth_density'`. This setting turns your distribution in a [kernal density estimate](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). Kernel density estimates look nice, but they obscure important information about your distribution like the true shape, minimum, and maximum. I only recommend using `dist_type = 'smooth_density'` if you need to compare multiple overlapping distributions and all that you care about is the rough shape.

If you set `dist_type = 'smooth_density'`, `bin_interval` is ignored. The distrbution is clipped/cropped using `distribution_min_max`.
