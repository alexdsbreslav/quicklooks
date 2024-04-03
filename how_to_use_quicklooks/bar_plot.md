# quicklooks.bar_plot
To add a bar to your chart, you will use the code:
```python
bar = ql.bar_plot(chart_skeleton,
xlabels = ,
y = ,
yerror = None, #If no values, None
bars_per_xlabel = 1,
bar_index = 0,
color = chart_skeleton.color_library.default,
opacity = 1,
label = '',
layer_order = 1)
```

**Always copy and paste!** quicklooks is designed as a copy-and-paste package. Once you've typed `ql.bar_plot` into your notebook, you can hit `shift-tab` to view and copy/paste the Docstring.
## Parameters
Parameters are the aspects of the line plot that you can change. Each parameter only accepts certain values.
- **xlabels**: list of strings; labels for each category of bars
- **y**: 1-dimensional array or iterable; this is height on each bar
    - Recommended: pandas [series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html), pandas [index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html), or numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
    - Advanced: this can take any iterable (e.g., range, list, tuple etc.)
- **yerror**: 1-dimensional array or iterable; default `None`
    - Recommended: pandas [series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html), pandas [index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html), or numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
    - Advanced: this can take any iterable (e.g., range, list, tuple etc.)
- **bars_per_xlabel**: integer; default `1`
    - This is the number of bars per category (xlabel)
- **bar_index**: integer; default `0`
    - This is the order that the bars are drawn in within each category (from left = 0 to right)
- **color**: this is defined by the chart_skeleton's color library; delete `default` and hit `tab` to see available colors in the color library
- **opacity**: float; default `1`
    - 0 is invisible, 1 is entirely opaque
- **label**: string;
    - This is the label for the line which can shown in the plot and/or the legend
- **layer_order**: integer; default `1`
    - This dictates what is drawn 1st, 2nd, 3rd etc.
    - Higher numbered plots will be drawn on top of lower numbered plots; if `layer_order = 1` for all plots, plots will be drawn in the order that they appear in the code.
## Returns
These are values that are stored in the `bar` object once you've run the code. **You will rarely ever need these,** but you can use these objects for advanced features like animating your plot into a gif.
- **bar_obj**: returns mean line; [matploblib.container.BarContainer](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer)
## Examples
