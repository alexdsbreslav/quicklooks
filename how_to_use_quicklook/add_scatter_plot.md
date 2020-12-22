# Add a scatter plot to your chart skeleton
To add a line to your chart, we will use the function:
```python
quicklook.add_scatter_plot
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. You should always copy the default code into your notebook from the documentation.
For tips on how to easily copy-and-paste quicklook code into your notebook, [click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md). 

## Basic Example:
1. Make sure that quicklook is imported into your notebook.
2. Get your data! Here, I'll create some arbitrary data and save it as `x_values` and `y_values`.
3. Create your chart skeleton. [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
4. Add your scatter using `quicklook.add_scatter_to_chart`

```python
import pandas as pd
import numpy as np
import os
import quicklook
```
```python
# ---- create arbitrary data
rng = np.random.RandomState(1)
x_values = np.linspace(0,10,20)
y_values = [i**2+rng.randint(-10,10) for i in x_values]

# ---- create the chart skeleton
chart_skeleton = quicklook.build_chart_skeleton(size = 'default',
title = 'Making a Scatter Plot',
xlabel = 'X Values',
ylabel = 'Y\nValues',
x_min_max = (0,10), y_min_max = (-10,100),
xtick_interval = 1, ytick_interval = 10,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add scatter plot
quicklook.add_scatter_plot(chart_skeleton,
x = x_values,
y = y_values,
x_error = None, #If no values, None
y_error = None, #If no values, None
color_name = 'blue', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['default', 'light', 'dark']
marker_shape = 'o', #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label_for_legend = '',
layer_order = 1)
```
![basic_example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/scatter/basic_example.png)

## Complete Example:
1. Make sure that quicklook is imported into your notebook.
2. Get your data! Here, I'll create some arbitrary data.
3. Create your chart skeleton.
    - [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
4. Add multiple scatters using `quicklook.add_scatter_to_chart` and adjust the style options.
5. Add a legend.
    - [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/add_legend.md) for more details on how to add a legend to your chart
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
rng = np.random.RandomState(4)
x_values = np.linspace(0,10,20)
blue_y_values = [i**2+rng.randint(-10,10) for i in x_values]
rng = np.random.RandomState(1)
orange_group_x_values = pd.DataFrame([np.linspace(0,10,20)+rng.uniform(-2,2,20) for i in range(10)])
orange_group_y_values = pd.DataFrame([[abs(i-5)**3+rng.randint(-10,10) for i in x_values]+rng.uniform(-20,20,20) for i in range(10)])

# ---- create the chart skeleton
chart_skeleton = quicklook.build_chart_skeleton(size = 'default',
title = 'Making a Scatter Plot',
xlabel = 'X Values',
ylabel = 'Y\nValues',
x_min_max = (0,10), y_min_max = (-15,100),
xtick_interval = 1, ytick_interval = 10,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add blue circles
quicklook.add_scatter_plot(chart_skeleton,
x = x_values,
y = y_values,
x_error = None, #If no values, None
y_error = None, #If no values, None
color_name = 'blue', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['default', 'light', 'dark']
marker_shape = 'o', #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label_for_legend = 'Blue Circles',
layer_order = 1)

# ---- add light orange squares
# ---- this scatter plot represents group means for x and y values
# ---- accordinlying, we show standard error on the x axis and y axis using the clouds around each square
quicklook.add_scatter_plot(chart_skeleton,
x = orange_group_x_values.mean(),
y = orange_group_y_values.mean(),
x_error = orange_group_x_values.sem(), #If no values, None
y_error = orange_group_y_values.sem(), #If no values, None
color_name = 'orange', #['gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
color_brightness = 'default', #['default', 'light', 'dark']
marker_shape = 's', #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label_for_legend = 'Orange Squares',
layer_order = 2)

# ---- add legend
quicklook.add_legend(chart_skeleton,
legend_location = 'best', frame_around_legend=True);

# ---- save plot
quicklook.save_chart_to_computer(chart_name = 'complete_example', 
                                 path_to_folder_to_save_chart_in = os.path.join(os.path.abspath('images'), 'plots', 'scatter'),
                                 print_confirmation=False);
```
![complete_example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/scatter/complete_example.png)

## Style options
- `color_name` can be 'gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange'
- `color_brightness` can be 'default', 'light', or 'dark'
- `marker_shape` can be 'o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x' ([click here](https://matplotlib.org/api/markers_api.html) to see an example of each marker shape)
- `opacity` can be any number between 0 and 1
- `label_for_legend` is the name of the line; this will show up in the legend when you add one.
- `layer_order` can be any number. Layers are drawn from low to high numbers; this means that a line with `layer_order = 2` will be drawn on top of `layer_order = 1`. If you leave `layer_order = 1` for all lines, the lines will be drawn in the order that they show up in your code.
