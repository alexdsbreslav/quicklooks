# quicklook.distribution_plot
To add a bar to your chart, you will use the code:
```python
dist = ql.distribution_plot(chart_skeleton,
data = ,
override_chart_skeleton = True,
distribution_min_max = (None,None),
bin_interval = None, #If dist_type is smooth_density, None
dist_type = 'binned_counts', #['binned_counts', 'binned_density', 'smooth_density']
color = chart_skeleton.color_library.default,
opacity = 1,
label = '',
layer_order = 1)
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. Once you've typed `ql.bar_plot` into your notebook, you can hit `shift-tab` to view and copy/paste the Docstring.
## Parameters
Parameters are the aspects of the distribution plot that you can change. Each parameter only accepts certain values.
- **data**: 1-dimensional array or iterable
    - Recommended: pandas [series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html), pandas [index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html), or numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
    - Advanced: this can take any iterable (e.g., range, list, tuple etc.)
    - Note that if `xtick_labels` is a timeseries (i.e., `days`, `months`, `quarters`, or `years`), x must be an array of dates or datetimes; see more on this type of data [here](https://docs.python.org/3/library/datetime.html).
- **override_chart_skeleton**: bool (True or False); default `True`
    - Highly recommend that you start with this set to True
    - When set to True, you'll see a printout that gives you the `x_min_max`, `y_min_max`, `xtick_interval`, and `ytick_interval`, `distribution_min_max` and `bin_interval`; given these, you can set your chart skeleton and distribution plot settings appropriately and set to False
- **distribution_min_max**: tuple of integers; default `(None, None)`
    - This defines the minimum and maximum values that your data are binned into
    - Recommended: Only define this once you've plotted your distribution plot with `override_chart_skeleton = True` first; once defined, set `override_chart_skeleton = False`
- **bin_interval**: integer; default `None`
    - This defines the range of values in each bin
    - Recommended: Only define this once you've plotted your distribution plot with `override_chart_skeleton = True` first; once defined, set `override_chart_skeleton = False`
- **dist_type**: string; default `'binned_counts'`
    - `binned_counts`: bar height represents raw counts of instances that fit within that bin
    - `binned_density`: bar height is a probability density; this means that the area under the histogram integrates to 1. For more detail see the density parameter of [matplotlib.pyplot.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)
    - `smooth_density`: visualize the distribution as a [kernal density estimate](https://seaborn.pydata.org/generated/seaborn.kdeplot.html).
      - Kernel density estimates look nice, but they obscure important information about your distribution like the true shape, minimum, and maximum.
      - I only recommend using `dist_type = 'smooth_density'` if you need to compare multiple overlapping distributions and all that you care about is the rough shape.
      - When using this type: `bin_interval` is ignored; the distrbution is clipped/cropped using `distribution_min_max`.
- **color**: this is defined by the chart_skeleton's color library; delete `default` and hit `tab` to see available colors in the color library
- **opacity**: float; default `1`
    - 0 is invisible, 1 is entirely opaque
- **label**: string;
    - This is the label for the line which can shown in the plot and/or the legend
- **layer_order**: integer; default `1`
    - This dictates what is drawn 1st, 2nd, 3rd etc.
    - Higher numbered plots will be drawn on top of lower numbered plots; if `layer_order = 1` for all plots, plots will be drawn in the order that they appear in the code.
## Returns
These are values that are stored in the `dist` object once you've run the code. **You will rarely ever need these,** but you can use these objects for advanced features like animating your plot into a gif.
- **distribution_obj**: returns histogram as a set of three objects defined within [matploblib.pyplot.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html). If `dist_type = 'smooth_density'` then returns histrogram as a `matplotlib.axes.Axes` object as outlined within [seaborn.kdeplot](https://seaborn.pydata.org/generated/seaborn.kdeplot.html).
## Examples
## Note
To accurately compare multiple distributions, I **strongly recommend**:
- Using the same `distribution_min_max` for both variables
- Using the same `bin_interval` for both variables
- Setting `dist_type = 'binned_density'`
- Setting `opacity = 0.5` so you can see overlapping parts

<sup>*</sup>For more info, [right-click here](https://machinelearningmastery.com/probability-density-estimation/) to open an article by Jason Brownlee and read through "Summarize Density with a Histogram".
