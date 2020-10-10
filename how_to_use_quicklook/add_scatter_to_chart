## Add a scatter to your chart
To add a line to your chart, we will use the function:
```python
quicklook.add_scatter_to_chart
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
# ---- create arbtrary data
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
quicklook.add_scatter_to_chart(chart_skeleton,
x = x_values,
y = y_values,
color_name = 'blue',
color_brightness = 'default',
marker_shape = 'o',
opacity = 1,
label_for_legend = '',
layer_order = 1)
```
![basic_example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/scatter/basic_example.png)
## Style options
- `color_name` can be 'gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange'
- `color_brightness` can be 'default', 'light', or 'dark'
- `marker_shape` can be 'o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x' ([click here](https://matplotlib.org/api/markers_api.html) to see an example of each marker shape)
- `opacity` can be any number between 0 and 1
- `label_for_legend` is the name of the line; this will show up in the legend when you add one.
- `layer_order` can be any number. Layers are drawn from low to high numbers; this means that a line with `layer_order = 2` will be drawn on top of `layer_order = 1`. If you leave `layer_order = 1` for all lines, the lines will be drawn in the order that they show up in your code.

## Complete Example:
1. Make sure that quicklook is imported into your notebook.
2. Get your data! Here, I'll create some arbitrary data.
3. Create your chart skeleton. [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
4. Add multiple scatters using `quicklook.add_scatter_to_chart` and adjust the style options.
5. Add a legend.
6. Save the chart to a folder on my computer.

```python
import pandas as pd
import numpy as np
import os
import quicklook
```
```python
# ---- create arbtrary data
rng = np.random.RandomState(4)
x_values = np.linspace(0,10,20)
blue_y_values = [i**2+rng.randint(-10,10) for i in x_values]
orange_y_values = [abs(i-5)**3+rng.randint(-10,10) for i in x_values]

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
quicklook.add_scatter_to_chart(chart_skeleton,
x = x_values,
y = blue_y_values,
color_name = 'blue',
color_brightness = 'default',
marker_shape = 'o',
opacity = 1,
label_for_legend = 'Blue Circles',
layer_order = 1)

# ---- add light orange squares; make them slightly transparent so that blue dots show through
quicklook.add_scatter_to_chart(chart_skeleton,
x = x_values,
y = orange_y_values,
color_name = 'orange',
color_brightness = 'dark',
marker_shape = 's',
opacity = 0.5,
label_for_legend = 'Orange Squares',
layer_order = 2)

# ---- add legend
quicklook.add_legend(chart_skeleton,
legend_location = 'best', frame_around_legend=True);

# ---- save plot
quicklook.save_chart(chart_name = 'complete_example', 
                     path_to_folder_to_save_chart_in = fp.join(fp.abspath('images'), 'plots', 'scatter'),
                     print_confirmation=False);
```
![complete_example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/scatter/complete_example.png)
