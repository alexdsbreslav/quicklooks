# quicklook.scatter_plot
To add a scatter plot to your chart, you will use the code:
```python
scatter = ql.scatter_plot(chart_skeleton,
x = ,
y = ,
x_error = None, #If no values, None
y_error = None, #If no values, None
color = chart_skeleton.color_library.default,
marker_shape = 'o', #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x', '']
opacity = 1,
label = '',
layer_order = 1)
```
**Always copy and paste!** quicklook is designed as a copy-and-paste package. Once you've typed `ql.scatter_plot` into your notebook, you can hit `shift-tab` to view and copy/paste the Docstring.
## Parameters
- **x**: 1-dimensional array or iterable
    - Recommended: pandas [series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html), pandas [index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html), or numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
    - Advanced: this can take any iterable (e.g., range, list, tuple etc.)
- **y**: 1-dimensional array or iterable
    - Recommended: pandas [series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html), pandas [index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html), or numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
    - Advanced: this can take any iterable (e.g., range, list, tuple etc.)
- **xerror**: 1-dimensional array or iterable; default `None`
    - Recommended: pandas [series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html), pandas [index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html), or numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
    - Advanced: this can take any iterable (e.g., range, list, tuple etc.)
- **yerror**: 1-dimensional array or iterable; default `None`
    - Recommended: pandas [series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html), pandas [index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html), or numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
    - Advanced: this can take any iterable (e.g., range, list, tuple etc.)
- **color**: this is defined by the chart_skeleton's color library; delete `default` and hit `tab` to see available colors in the color library
- **marker_shape**: string; default `None`
    - Recommended: one of ['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
    - Advanced: can take any matplotlib [marker](https://matplotlib.org/stable/api/markers_api.html)
- **opacity**: float; default `1`
    - 0 is invisible, 1 is entirely opaque
- **label**: string;
    - This is the label for the line which can shown in the plot and/or the legend
- **layer_order**: integer; default `1`
    - This dictates what is drawn 1st, 2nd, 3rd etc.
    - Higher numbered plots will be drawn on top of lower numbered plots; if `layer_order = 1` for all plots, plots will be drawn in the order that they appear in the code.
## Returns
- **scatter_obj**: returns points; [matploblib.lines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D)
- **error_obj**:
  - given x *or* y error, returns [matploblib.container.ErrobarContainer](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.ErrorbarContainer)
  - given x *and* y error, returns a dictionary with keys `fill` and `outline`, that provide lists of [matplotlib.patches.Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html)
## Examples
