# Build a chart skeleton
A chart skeleton is the background, title, axes, and axis labels. It is a skeleton (or wireframe, or background) that we will layer plots onto. Plots are various ways that we can visualize data like line plots, bar plots, histograms, scatter plots etc.
## Default code copied from `Docstring`
Always copy the default code into your notebook first. For tips on how to easily copy-and-paste quicklook code into your notebook, [click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md).
```python
chart_skeleton = quicklook.build_chart_skeleton(style = 'default', size = 'default',
title = '',
xlabel = '',
ylabel = '',
x_min_max = (0,1), y_min_max = (0,1),
xtick_interval = 0.25, ytick_interval = 0.25,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);
```
![default](https://github.com/alexdsbreslav/quicklook/blob/master/images/build_chart_skeleton/default.png)


## Add a title, x-axis label, and y-axis label
Simply add text in between the quotation marks! Notice the `\n` in the ylabel. This is how you indicate a line break.
```python
chart_skeleton = quicklook.build_chart_skeleton(style = 'default', size = 'default',
title = 'Chart Skeleton Example',
xlabel = 'X-Axis Label',
ylabel = 'Y-Axis\nLabel',
x_min_max = (0,1), y_min_max = (0,1),
xtick_interval = 0.25, ytick_interval = 0.25,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);
```
![titles](https://github.com/alexdsbreslav/quicklook/blob/master/images/build_chart_skeleton/titles.png)

## Change the X and Y Axis
There are two settings you can change on each axis:
1. The range of values that your axes cover.
  - `x_min_max` and `y_min_max` indicate the minimum and maximum values on your axes. `x_min_max` and `y_min_max` need to be formatted as a tuple where the first number is the min and the second number is the max `(min number on axis, max number on axis)`. 
2. How often there are tick marks on your axis.
  - `xtick_interval` and `ytick_interval` indicate the increment that you want to mark off on axis. For example, if `x_min_max = (1,3)` and `xtick_interval = 0.5` your x-axis would have 1, 1.5, 2, 2.5, and 3 marked on it.

```python
chart_skeleton = quicklook.build_chart_skeleton(style = 'default', size = 'default',
title = 'Chart Skeleton Example',
xlabel = 'X-Axis Label',
ylabel = 'Y-Axis\nLabel',
x_min_max = (0,10), y_min_max = (50,100),
xtick_interval = 1, ytick_interval = 10,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);
```
![axes](https://github.com/alexdsbreslav/quicklook/blob/master/images/build_chart_skeleton/axes.png)

## Add gridlines
Gridlines are light grey lines that extend across your plot. These can be turned on and off using the `horizontal_gridlines_on` and the `vertical_gridlines_on` arguments. If these are set to `True`, the gridlines will be shown; if these are set to `False`, the gridlines will not be shown.
```python
chart_skeleton = quicklook.build_chart_skeleton(style = 'default', size = 'default',
title = 'Chart Skeleton Example',
xlabel = 'X-Axis Label',
ylabel = 'Y-Axis\nLabel',
x_min_max = (0,10), y_min_max = (50,100),
xtick_interval = 1, ytick_interval = 10,
horizontal_gridlines_on = True,
vertical_gridlines_on = True);
```
![gridlines](https://github.com/alexdsbreslav/quicklook/blob/master/images/build_chart_skeleton/gridlines.png)

## Change the size - `'default'` or `'small'`
If you prefer, you can change the size to small.
```python
chart_skeleton = quicklook.build_chart_skeleton(style = 'default', size = 'small',
title = 'Chart Skeleton Example',
xlabel = 'X-Axis Label',
ylabel = 'Y-Axis\nLabel',
x_min_max = (0,10), y_min_max = (50,100),
xtick_interval = 1, ytick_interval = 10,
horizontal_gridlines_on = True,
vertical_gridlines_on = True);
```
![small](https://github.com/alexdsbreslav/quicklook/blob/master/images/build_chart_skeleton/small.png)

## Advanced topics
- **Style:** Style defines the background and text of your chart skeleton. It also defines the colors that you will have available to you for plotting your data. [Click here]() for more information about styling in quicklook.
- The **chart_skeleton** variable: Notice that when you create your plot, it is set equalt to `chart_skeleton`. `chart_skeleton` is a variable that holds a lot of useful information. If you want to use matplotlib to create custom plots on top of a quicklook chart skeleton, you can use the `chart_skeleton` variable to get important details. If you are proficient in matplotlib already, [click here]() for more information on how to use the `chart_skeleton` variable for custom plotting outside of quicklook.
