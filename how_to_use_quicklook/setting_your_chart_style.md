# Setting your chart style
When you build your chart skeleton (see [build a chart skeleton](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for directions), there is a `style` argument. `Style` can be set as:
- `default`
- `simple_dark`
- `simple_light`

The style argument sets up two things:
1. It determines the text, background, and axis color for your chart skeleton.
2. It creates a color library. You will use the colors in the color library when you create plots on top of your chart skeleton.

## This is the `default` style.
**The `default` style has a white background, black text, and black axes.**


```python
# ---- create a chart skeleton in the default style
chart_skeleton = quicklook.build_chart_skeleton(style = 'default', size = 'default',
title = 'default style',
xlabel = 'X-Axis Label',
ylabel = 'Y-Axis\nLabel',
x_min_max = (0,1), y_min_max = (0,1),
xtick_interval = 0.5, ytick_interval = 0.5,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- plot blue dots
# ---- x and y are sets of 50 numbers randomly generated between 0 and 1
quicklook.add_scatter_to_chart(chart_skeleton,
x = np.random.rand(50),
y = np.random.rand(50),
color_name = 'blue',
color_brightness = 'default',
marker_shape = 'o',
opacity = 1,
label_for_legend = 'blue dots',
layer_order = 1)

# ---- plot yellow diamonds
# ---- x and y are sets of 50 numbers randomly generated between 0 and 1
quicklook.add_scatter_to_chart(chart_skeleton,
x = np.random.rand(50),
y = np.random.rand(50),
color_name = 'yellow',
color_brightness = 'default',
marker_shape = 'D',
opacity = 1,
label_for_legend = 'yellow diamonds',
layer_order = 2)

# ---- add a legend
quicklook.add_legend(chart_skeleton,
legend_location = 'lower right', frame_around_legend=True,
size_of_marker_in_legend = 1);
```


![default_plot](https://github.com/alexdsbreslav/quicklook/blob/master/images/setting_your_chart_style/default_plot.png)


This is the **color library for the `default` style.**  If you ever forget the colors that you have available to you, you can use the function below to see the color library in your notebook. The default color library uses [open-color](https://yeun.github.io/open-color/).


```python
quicklook.show_color_library(chart_skeleton)
```


![default_clib](https://github.com/alexdsbreslav/quicklook/blob/master/images/setting_your_chart_style/default_clib.png)


## This is the `simple_dark` style.
**The `simple_dark` style has a dark background, gray text, and gray axes.**


```python
# ---- create a chart skeleton in the simple_dark style
chart_skeleton = quicklook.build_chart_skeleton(style = 'simple_dark', size = 'default',
title = 'simple_dark style',
xlabel = 'X-Axis Label',
ylabel = 'Y-Axis\nLabel',
x_min_max = (0,1), y_min_max = (0,1),
xtick_interval = 0.5, ytick_interval = 0.5,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- plot blue circles
# ---- x and y are sets of 50 numbers randomly generated between 0 and 1
quicklook.add_scatter_to_chart(chart_skeleton,
x = np.random.rand(50),
y = np.random.rand(50),
color_name = 'blue',
color_brightness = 'default',
marker_shape = 'o',
opacity = 1,
label_for_legend = 'blue dots',
layer_order = 1)

# ---- plot yellow diamonds
# ---- x and y are sets of 50 numbers randomly generated between 0 and 1
quicklook.add_scatter_to_chart(chart_skeleton,
x = np.random.rand(50),
y = np.random.rand(50),
color_name = 'yellow',
color_brightness = 'default',
marker_shape = 'D',
opacity = 1,
label_for_legend = 'yellow diamonds',
layer_order = 2)

# ---- add a legend
quicklook.add_legend(chart_skeleton,
legend_location = 'lower right', frame_around_legend=True,
size_of_marker_in_legend = 1);
```


![simpledark_plot](https://github.com/alexdsbreslav/quicklook/blob/master/images/setting_your_chart_style/simpledark_plot.png)


This is the **color library for the `simple_dark` style.**  If you ever forget the colors that you have available to you, you can use the function below to see the color library in your notebook.


```python
quicklook.show_color_library(chart_skeleton)
```


![simpledark_clib](https://github.com/alexdsbreslav/quicklook/blob/master/images/setting_your_chart_style/simpledark_clib.png)


## This is the `simple_light` style.
**The `simple_light` style has a gray background, dark gray text, and dark gray axes.**


```python
# ---- create a chart skeleton in the simple_light style
chart_skeleton = quicklook.build_chart_skeleton(style = 'simple_light', size = 'default',
title = 'simple_light style',
xlabel = 'X-Axis Label',
ylabel = 'Y-Axis\nLabel',
x_min_max = (0,1), y_min_max = (0,1),
xtick_interval = 0.5, ytick_interval = 0.5,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- plot blue circles
# ---- x and y are sets of 50 numbers randomly generated between 0 and 1
quicklook.add_scatter_to_chart(chart_skeleton,
x = np.random.rand(50),
y = np.random.rand(50),
color_name = 'blue',
color_brightness = 'default',
marker_shape = 'o',
opacity = 1,
label_for_legend = 'blue dots',
layer_order = 1)

# ---- plot yellow diamonds
# ---- x and y are sets of 50 numbers randomly generated between 0 and 1
quicklook.add_scatter_to_chart(chart_skeleton,
x = np.random.rand(50),
y = np.random.rand(50),
color_name = 'yellow',
color_brightness = 'default',
marker_shape = 'D',
opacity = 1,
label_for_legend = 'yellow diamonds',
layer_order = 2)

# ---- add a legend
quicklook.add_legend(chart_skeleton,
legend_location = 'lower right', frame_around_legend=True,
size_of_marker_in_legend = 1);
```


![simplelight_plot](https://github.com/alexdsbreslav/quicklook/blob/master/images/setting_your_chart_style/simplelight_plot.png)


This is the **color library for the `simple_light` style.**  If you ever forget the colors that you have available to you, you can use the function below to see the color library in your notebook.


```python
quicklook.show_color_library(chart_skeleton)
```


![simplelight_clib](https://github.com/alexdsbreslav/quicklook/blob/master/images/setting_your_chart_style/simplelight_clib.png)
