## Build a chart skeleton
To build a chart skeleton, we will use the function:
```python
quicklook.build_chart_skeleton
```

A chart skeleton is the background, title, axes, and axis labels. It is a skeleton (or wireframe, or background) that we will layer plots on to. Plots are various ways that we can visualize data like line plots, bar plots, histograms, scatter plots etc.

**Every time you want to create a new plot with quicklook, you need to build a chart skeleton.**
## Before you start...
Make sure that quicklook is imported into your notebook. At the top of every one of my notebooks, I import quicklook along with several other key packages:
```python
import pandas as pd
import numpy as np
import os
import quicklook
```
## Step 1: Copy-and-paste the default code from the Docstring.
Always copy the default code into your notebook first. For tips on how to easily copy-and-paste quicklook code into your notebook, [click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md). Notice that our plot doesn't have a title or labels on the x-axis or y-axis. This is because the `title`, `xlabel`, and `ylabel` options are all set to `= ''`.
```python
chart_skeleton = quicklook.build_chart_skeleton(
size = 'half_slide', #['print', 'half_slide', 'full_slide']
title = '',
xlabel = '',
ylabel = '',
x_min_max = (0,1), y_min_max = (0,1),
xtick_interval = 0.25, ytick_interval = 0.25,
xtick_labels = 'default', #['default', 'percents', list]
ytick_labels = 'default', #['default', 'percents', list]
horizontal_gridlines_on = False,
vertical_gridlines_on = False);
```
![default](https://github.com/alexdsbreslav/quicklook/blob/master/images/build_chart_skeleton/default.png)


## Step 2: Add a title, x-axis label, and y-axis label.
Simply add text in between the quotation marks! Notice the `\n` in the ylabel. This is how you indicate a line break.
```python
chart_skeleton = quicklook.build_chart_skeleton(
size = 'half_slide', #['print', 'half_slide', 'full_slide']
title = 'Chart Skeleton Example',
xlabel = 'X-Axis Label',
ylabel = 'Y-Axis\nLabel',
x_min_max = (0,1), y_min_max = (0,1),
xtick_interval = 0.25, ytick_interval = 0.25,
xtick_labels = 'default', #['default', 'percents', list]
ytick_labels = 'default', #['default', 'percents', list]
horizontal_gridlines_on = False,
vertical_gridlines_on = False);
```
![titles](https://github.com/alexdsbreslav/quicklook/blob/master/images/build_chart_skeleton/titles.png)

## Step 3: Change the X and Y Axis.
There are two settings that you will need to change on each axis:

### The range of values that your axes cover.
  - `x_min_max` and `y_min_max` indicate the minimum and maximum values on your axes. `x_min_max` and `y_min_max` need to be formatted as a [tuple](https://www.w3schools.com/python/python_tuples.asp) where the first number is the min and the second number is the max `(min number on axis, max number on axis)`.

### How often there are tick marks on your axis.
  - `xtick_interval` and `ytick_interval` indicate the increment that you want to mark off on axis. For example, if `x_min_max = (1,3)` and `xtick_interval = 0.5` your x-axis would have 1, 1.5, 2, 2.5, and 3 marked on it.

```python
chart_skeleton = quicklook.build_chart_skeleton(size = 'half_slide',
title = 'Chart Skeleton Example',
xlabel = 'X-Axis Label',
ylabel = 'Y-Axis\nLabel',
x_min_max = (0,10), y_min_max = (50,100),
xtick_interval = 1, ytick_interval = 10,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);
```
![axes](https://github.com/alexdsbreslav/quicklook/blob/master/images/build_chart_skeleton/axes.png)

## Step 4: Adjust optional settings.
### Change the size of the plot - `'full_slide'`, `'half_slide'`, or `'print'`.
If you prefer, you can change the size to `'full_slide'` (takes up the entire slide in a deck) or `'print'`. Print will appear very small inside JupyterLab, but will be the ideal size to save to your computer and place in a Word or Google document.
```python
chart_skeleton = quicklook.build_chart_skeleton(
size = 'print', #['print', 'half_slide', 'full_slide']
title = 'Chart Skeleton Example',
xlabel = 'X-Axis Label',
ylabel = 'Y-Axis\nLabel',
x_min_max = (0,10), y_min_max = (50,100),
xtick_interval = 1, ytick_interval = 10,
xtick_labels = 'default', #['default', 'percents', list]
ytick_labels = 'default', #['default', 'percents', list]
horizontal_gridlines_on = False,
vertical_gridlines_on = False);
```
![small](https://github.com/alexdsbreslav/quicklook/blob/master/images/build_chart_skeleton/small.png)

### Add gridlines.
Gridlines are light grey lines that extend across your plot. These can be turned on and off using the `horizontal_gridlines_on` and the `vertical_gridlines_on` arguments. If these are set to `True`, the gridlines will be shown; if these are set to `False`, the gridlines will not be shown.
```python
chart_skeleton = quicklook.build_chart_skeleton(
size = 'print', #['print', 'half_slide', 'full_slide']
title = 'Chart Skeleton Example',
xlabel = 'X-Axis Label',
ylabel = 'Y-Axis\nLabel',
x_min_max = (0,10), y_min_max = (50,100),
xtick_interval = 1, ytick_interval = 10,
xtick_labels = 'default', #['default', 'percents', list]
ytick_labels = 'default', #['default', 'percents', list]
horizontal_gridlines_on = True,
vertical_gridlines_on = True);
```
![gridlines](https://github.com/alexdsbreslav/quicklook/blob/master/images/build_chart_skeleton/gridlines.png)

### Change the tick labels.
In step 3, you defined the range of values that your axes cover and how often there are tick marks on your axis. You also have the option to easily change your axes labels to percentages or to a custom list of labels.
```python
chart_skeleton = quicklook.build_chart_skeleton(
size = 'half_slide', #['print', 'half_slide', 'full_slide']
title = 'Chart Skeleton Example',
xlabel = 'X-Axis Label',
ylabel = 'Y-Axis\nLabel',
x_min_max = (0,5), y_min_max = (50,100),
xtick_interval = 1, ytick_interval = 10,
xtick_labels = ['top', 'middle', 'left','outside', 'top\nleft', 'middle\nright'], #['default', 'percents', list]
ytick_labels = 'percents', #['default', 'percents', list]
horizontal_gridlines_on = True,
vertical_gridlines_on = True);
```
![axis_labels](https://github.com/alexdsbreslav/quicklook/blob/master/images/build_chart_skeleton/axis_labels.png)

\*Note that this only changes how the **label is formatted**, it does not change the underlying value. We highly recommend building your plot with `xtick_labels` and `ytick_labels` set to `default` and then only changing them to `percents` or a list of custom labels at the end.

## Next steps...
Now you have a chart skeleton! The next step is to visualize your data using plots (e.g. line plots, bar plots, scatter plots, histograms) on top of your chart skeleton. [Click here](https://github.com/alexdsbreslav/quicklook/tree/master/how_to_use_quicklook) to go to the directory of plots that you can add.

## Advanced topics
The **chart_skeleton** variable: Notice that when you create your plot, it is set equalt to `chart_skeleton`. `chart_skeleton` is a variable that holds a lot of useful information. If you want to use matplotlib to create custom plots on top of a quicklook chart skeleton, you can use the `chart_skeleton` variable to get important details. If you are proficient in matplotlib already, [click here]() for more information on how to use the `chart_skeleton` variable for custom plotting outside of quicklook.
