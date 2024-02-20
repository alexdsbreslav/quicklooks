# quicklook.line_plot
To add a line to your chart, you will use the code:
```python
line = ql.line_plot(chart_skeleton,
x = ,
y = ,
yerror = None, #If no values, None
color = chart_skeleton.color_library.default,
linewidth = 5,
linestyle = '-', #['-', '--', ':', '-.']
marker_shape = None, #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label_for_legend = '',
plot_label = True,
layer_order = 1)
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. Once you've typed `ql.line_plot` into your notebook, you can hit `shift-tab` to view and copy/paste the Docstring.
## Parameters
Parameters are the aspects of the line plot that you can change. Each parameter only accepts certain values.
- **x**: 1-dimensional array or iterable
    - Recommended: pandas [series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html), pandas [index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html), or numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
    - Advanced: this can take any iterable (e.g., range, list, tuple etc.)
    - Note that if `xtick_labels` is a timeseries (i.e., `days`, `months`, `quarters`, or `years`), x must be an array of dates or datetimes; see more on this type of data [here](https://docs.python.org/3/library/datetime.html).
- **y**: 1-dimensional array or iterable
    - Recommended: pandas [series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html), pandas [index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html), or numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
    - Advanced: this can take any iterable (e.g., range, list, tuple etc.)
- **yerror**: 1-dimensional array or iterable; default `None`
    - Recommended: pandas [series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html), pandas [index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html), or numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
    - Advanced: this can take any iterable (e.g., range, list, tuple etc.)
- **linewidth**: integer; default `3`
    - Recommended: values between 1-10
- **linestyle**: string; default `'solid'`
    - Recommended: one of ['solid', 'dotted', 'dashed', 'dashdot']
    - Advanced: can take any matplotlib [LineStyle](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)
- **marker_shape**: string; default `None`
    - Recommended: one of ['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
    - Advanced: can take any matplotlib [marker](https://matplotlib.org/stable/api/markers_api.html)
- **opacity**: float; default `1`
    - 0 is invisible, 1 is entirely opaque
- **label**: string;
    - This is the label for the line which can shown in the plot and/or the legend
- **plot_label**: bool (True or False); default `True`
    - This dictates whether the label is plotted at the end of the line
    - If `False`, strongly recommended that you add a legend to your plot using `ql.legend`
    - Recommend `False` for plots intended for half slides (i.e., when `size = 'half_slide`)
- **layer_order**: integer; default `1`
    - This dictates what is drawn 1st, 2nd, 3rd etc.
    - Higher numbered plots will be drawn on top of lower numbered plots; if `layer_order = 1` for all plots, plots will be drawn in the order that they appear in the code.
## Returns
These are values that are stored in the `line` object once you've run the code. **You will rarely ever need these,** but you can use these objects for advanced features like animating your plot into a gif.
- **line_obj**: returns mean line; [matploblib.lines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D)
- **yerr_fill**: given error, returns fill between upper and lower bound as a [matploblib.collections.PolyCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection)
- **y_ub**: given error, returns upper bound line as [matploblib.lines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D)
- **y_lb**: given error, returns lower bound line as [matploblib.lines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D)

## Examples
```python
import pandas as pd
import numpy as np
import quicklook as ql
```
```python
# ---- make up some random data
x = np.linspace(0,30,30)
mobile = np.linspace(0,0.7,30)**(1/2)
web = np.linspace(0,0.8,30)**(1/3)

# ---- create the chart skeleton
chart_skeleton = ql.chart_skeleton(
size = ql.chart_size.notebook,
color_library = ql.color_libraries.skygrove,
font = ql.fonts.rubik,
title = 'Version Uptake Since Launch',
xlabel = 'Days Since Launch',
ylabel = 'Users',
x_min_max = (0,30), y_min_max = (0,1),
xtick_interval = 3, ytick_interval = 0.1,
xtick_labels = ql.chart_xlabel.default,
ytick_labels = ql.chart_ylabel.percents,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add two lines
line = ql.line_plot(chart_skeleton,
x = x,
y = mobile,
yerror = None, #If no values, None
color = chart_skeleton.color_library.default,
linewidth = 3,
linestyle = 'solid', #['solid', 'dashed', 'dotted', 'dashdot']
marker_shape = None, #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label = 'Mobile',
plot_label = True,
layer_order = 1)

line = ql.line_plot(chart_skeleton,
x = x,
y = web,
yerror = None, #If no values, None
color = chart_skeleton.color_library.periwinkle,
linewidth = 3,
linestyle = 'solid', #['solid', 'dashed', 'dotted', 'dashdot']
marker_shape = None, #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label = 'Web',
plot_label = True,
layer_order = 1)
```
![download-3](https://github.com/alexdsbreslav/quicklook/assets/21344372/d09cd806-5603-4710-ac3f-480b1ab9d400)

```python
# ---- make up some arbitrary data
rng = np.random.RandomState(1)
baseline = 7e6
activate = np.round(rng.normal(10e3,100e3,411))
lapse = np.round(rng.normal(9.5e3,100e3,411))
mau = baseline + (activate - lapse).cumsum()

df = pd.DataFrame({'mau':mau}, index=pd.date_range('2023-01-01', '2024-02-15'))

# ---- create the chart skeleton
chart_skeleton = ql.chart_skeleton(
size = ql.chart_size.notebook,
color_library = ql.color_libraries.mariglow,
font = ql.fonts.oswald,
title = 'Montly Active Users',
xlabel = 'Quarter',
ylabel = 'MAU',
x_min_max = ('2023-01-01','2024-02-15'), y_min_max = (5.5e6,9.5e6),
xtick_interval = 3, ytick_interval = 0.5e6,
xtick_labels = ql.chart_xlabel.quarters,
ytick_labels = ql.chart_ylabel.millions,
horizontal_gridlines_on = False,
vertical_gridlines_on = True);

# ---- add daily numbers
line = ql.line_plot(chart_skeleton,
x = df.index,
y = df.mau,
yerror = None, #If no values, None
color = chart_skeleton.color_library.light_gray,
linewidth = 2,
linestyle = 'solid', #['solid', 'dashed', 'dotted', 'dashdot']
marker_shape = None, #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label = 'Daily',
plot_label = False,
layer_order = 1)

# ---- add rolling average
line = ql.line_plot(chart_skeleton,
x = df.index,
y = df.mau.rolling(30, center=True).mean(),
yerror = df.mau.rolling(30, center=True).sem(), #If no values, None
color = chart_skeleton.color_library.default,
linewidth = 3,
linestyle = 'solid', #['solid', 'dashed', 'dotted', 'dashdot']
marker_shape = None, #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label = '30d Avg',
plot_label = False,
layer_order = 2)

legend = ql.legend(chart_skeleton,
legend_location = ql.legend.loc.best, frame=False);
```
![download-4](https://github.com/alexdsbreslav/quicklook/assets/21344372/d73e1039-67a1-4090-981b-7fac5e647aee)
