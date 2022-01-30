## Save chart to your computer
To add a legend to your chart, we will use the function:
```python
quicklook.save_chart
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. You should always copy the default code into your notebook from the documentation.
For tips on how to easily copy-and-paste quicklook code into your notebook, [click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md).

To save your chart to your computer, you'll need to do four things:
1. Add the `chart_name` (e.g. `example_chart_name`)
2. Add the `path_to_folder_to_save_chart_in`. This is a filepath that dicates which folder on your computer the file save your chart in(e.g. `/Users/alex/Documents`).
3. Set `print_confirmation` to True or False. If True, your code will print where exactly the image file was saved. (e.g. `example_chart_name was save in the folder: /Users/alex/Documents`. I would recommend setting this to True.

I strongly recommend writing `path_to_folder_to_save_chart_in` as a relative filepath using the package `os`. [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/creating_relative_filepaths.md) for a brief introduction to relative filepaths.

## Example:
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
layer_order = 1)

# ---- save plot
current_directory = os.path.abspath('')
quicklook.save_chart_to_computer(chart_skeleton,
                     chart_name = 'example',
                     path_to_folder_to_save_chart_in = os.path.join(current_directory, 'charts'),
                     print_confirmation=False);
```
