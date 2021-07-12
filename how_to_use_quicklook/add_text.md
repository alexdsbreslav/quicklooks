# Add text to your chart skeleton
To add text to your chart, we will use the function:
```python
quicklook.add_text
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. You should always copy the default code into your notebook from the documentation.
For tips on how to easily copy-and-paste quicklook code into your notebook, [click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md).

## Example:
1. Make sure that quicklook is imported into your notebook.
2. Create your chart skeleton. [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
3. Plot some data.
4. Add text using `quicklook.add_text`

```python
import pandas as pd
import numpy as np
import os
import quicklook
```
```python
# ---- create the chart skeleton
chart_skeleton = quicklook.build_chart_skeleton(size = 'half_slide',
title = 'Add a Legend to My Chart',
xlabel = 'X Values',
ylabel = 'Y\nValues',
x_min_max = (0,10), y_min_max = (-15,100),
xtick_interval = 1, ytick_interval = 10,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- plot some data...
# ---- this code has been removed for simplicity ----

# ---- add text
quicklook.add_text(chart_skeleton,
text = '$\leftarrow$ This point is\n     important',
color_name = 'blue', #['default','gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange']
text_location_on_x_axis = 5.5,
text_location_on_y_axis = 15.5,
horizontal_align = 'left',
vertical_align = 'center',
box_around_text = False,
layer_order = 1)

# ---- add legend
# ---- this code has been removed for simplicity ----
```
![example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/legend/text.png)

Notice that you can use:
- Plain text, where "\n" represents a line break (e.g. "This point is\n important")
- LaTEX (e.g. $\leftarrow$)
- or a combination!

## Style options
- `color_name` can be 'gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange'
- `horizontal_align` can be 'left', 'right', or 'center'
- `vertical_align` can be 'top', 'bottom', or 'center'
- `box_around_text` can be True or False
