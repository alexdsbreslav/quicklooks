## Save chart to your computer
To add a legend to your chart, we will use the function:
```python
quicklook.save_chart
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. You should always copy the default code into your notebook from the documentation.
For tips on how to easily copy-and-paste quicklook code into your notebook, [click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md). 

To save your chart to your computer, you'll need to do two things:
1. Add the `chart_name` (e.g. `example_chart_name`)
2. Add the `path_to_folder_to_save_chart_in` this is a filepath that dicates which folder on your computer the file will be created. (e.g. `/Users/alex/Documents`)
3. Set `print_confirmation` to True or False. If True, your code will print where exactly the image file was saved. (e.g. `example_chart_name was save in the folder: /Users/alex/Documents`. I would recommend setting this to True.

I strongly recommend writing `path_to_folder_to_save_chart_in` as a relative filepath using the package `os`. [Click here]() for a brief introduction on relative filepaths.

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
chart_skeleton = quicklook.build_chart_skeleton(size = 'default',
title = 'Example Title',
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
layer_order = 2)

# ---- save plot
quicklook.save_chart(chart_name = 'example_chart_name', 
                     path_to_folder_to_save_chart_in = os.path.abspath('charts'),
                     print_confirmation=True);
```
