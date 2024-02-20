# quicklook.line_plot
To add a line to your chart, you will use th code:
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
[PLACEHOLDER]
