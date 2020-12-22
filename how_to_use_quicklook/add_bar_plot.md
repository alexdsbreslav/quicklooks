# Add a bar plot to your chart skeleton
To add a bar to your chart, we will use the function:
```python
quicklook.add_bar_plot
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. You should always copy the default code into your notebook from the documentation.
For tips on how to easily copy-and-paste quicklook code into your notebook, [click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md). 

## Basic Example:
1. Make sure that quicklook is imported into your notebook.
2. Get your data! Here, I'll create some arbitrary data and save it as `x_values` and `y_values`.
3. Create your chart skeleton. 
    - [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
4. Add your bars using `quicklook.add_bar_plot`

```python
import pandas as pd
import numpy as np
import os
import quicklook
```
```python
# ---- create arbitrary data
rng = np.random.RandomState(1)
x_labels = ['Category {}'.format(i) for i in range(4)]
y_values = rng.rand(4)

chart_skeleton = quicklook.build_chart_skeleton(size = 'default',
title = 'Making a Bar Plot',
xlabel = 'Categories',
ylabel = 'Y\nValues',
x_min_max = (0,4), y_min_max = (0,1),
xtick_interval = 1, ytick_interval = 0.25,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add a bar plot
quicklook.add_bar_plot(chart_skeleton,
x_labels = x_labels,
y = y_values,
y_error = None, #If no values, None
bars_at_each_xlabel = 1,
bar_index = 0,
color_name = 'blue', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['default', 'light', 'dark']
opacity = 1,
label_for_legend = '',
layer_order = 1)
```
![basic_example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/bar/basic_example.png)

## Complete Example:
1. Make sure that quicklook is imported into your notebook.
2. Get your data! Here, I'll create some arbitrary data.
3. Create your chart skeleton. 
   - [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
4. Add multiple bar plots using `quicklook.add_bar_plot` and adjust the style options.
5. Add a legend.
   - [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/add_legend.md) for more details on adding a legend to your chart
6. Save the chart to your computer.
    - [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/save_chart_to_your_computer.md) for more details on how to save your chart to your computer.
```python
import pandas as pd
import numpy as np
import os
import quicklook
```
```python
# ---- create arbitrary data
rng = np.random.RandomState(1)
x_labels = ['Category {}'.format(i) for i in range(4)]
blue_y_values = rng.rand(4)
grape_group_y_values = pd.DataFrame(rng.rand(4,10))

chart_skeleton = quicklook.build_chart_skeleton(size = 'default',
title = 'Making a Bar Plot',
xlabel = 'Categories',
ylabel = 'Y\nValues',
x_min_max = (0,4), y_min_max = (0,1),
xtick_interval = 1, ytick_interval = 0.25,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add a blue bar plot
quicklook.add_bar_plot(chart_skeleton,
x_labels = x_labels,
y = blue_y_values,
y_error = None, #If no values, None
bars_at_each_xlabel = 2,
bar_index = 0,
color_name = 'blue', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['default', 'light', 'dark']
opacity = 1,
label_for_legend = 'Blue Bars',
layer_order = 1)

# ---- add a green bar plot
# ---- these bars are the means of a group, so we'll also show the standard error
quicklook.add_bar_plot(chart_skeleton,
x_labels = x_labels,
y = grape_group_y_values.mean(1),
y_error = grape_group_y_values.sem(1), #If no values, None
bars_at_each_xlabel = 2,
bar_index = 1,
color_name = 'green', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['default', 'light', 'dark']
opacity = 1,
label_for_legend = 'Green Bars',
layer_order = 1)

# ---- add legend
quicklook.add_legend(chart_skeleton,
legend_location = 'best', frame_around_legend=False);

# ---- save chart to computer
quicklook.save_chart_to_computer(chart_name = 'complete_example', 
                                 path_to_folder_to_save_chart_in = os.path.join(os.path.abspath('images'), 'plots', 'bar'),
                                 print_confirmation=False);
```
![complete_example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/bar/complete_example.png)

Notice that:
- To add multiple bars, I set `bars_at_each_xlabel = 2`
- For the blue bars, I set `bar_index = 0`; this means that they will be created at the left most index 0.
- For the green bars, I set `bar_index = 1`; this means that they will be created at the right-most index 1<sup>*</sup>.
- If I wanted 3 bars at each x label: I would set `bars_at_each_xlabel = 3` and `bar_index = 0` would be the left, `bar_index = 1` would be in the middle, and `bar_index = 2` would be on the right.

<sup>*</sup>Remember that Python uses 0 index. This means that if there are two positions the bars can be in (left or right), there corresponding indices are 0 and 1.

## Style options
- `color_name` can be 'gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange'
- `color_brightness` can be 'default', 'light', or 'dark'
- `opacity` can be any number between 0 and 1
- `label_for_legend` is the name of the line; this will show up in the legend when you add one.
- `layer_order` can be any number. Layers are drawn from low to high numbers; this means that a line with `layer_order = 2` will be drawn on top of `layer_order = 1`. If you leave `layer_order = 1` for all lines, the lines will be drawn in the order that they show up in your code.
