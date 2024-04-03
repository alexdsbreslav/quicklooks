# quicklooks.chart_skeleton
A chart skeleton is the background, title, axes, and axis labels. It is a skeleton (or wireframe, or background) that we will layer plots on to.
```python
chart_skeleton = ql.chart_skeleton(
size = ql.chart_size.notebook,
color_library = ql.color_libraries.skygrove,
font = ql.fonts.rubik,
title = '',
xlabel = '',
ylabel = '',
x_min_max = (0,1), y_min_max = (0,1),
xtick_interval = 0.25, ytick_interval = 0.25,
xtick_labels = ql.chart_xlabel.default,
ytick_labels = ql.chart_ylabel.default,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);
```

## Parameters
Parameters are the aspects of the chart skeleton that you can change. Each parameter only accepts certain values.
- **size**: default `notebook`; see more on plot sizes [here]()
- **color_library**: default `skygrove`; see more on color libraries [here]()
- **font**: default `rubik`; see available fonts [here]()
- **title**: string
- **xlabel**: string
- **ylabel**: string
- **x_min_max**: tuple; can take floats or dates in string format `YYYY-MM-DD`
- **y_min_max**: tuple; floats
- **xtick_interval**: float
- **ytick_interval**: float
- **xtick_labels**: `default` is floats; see more on xtick_labels [here]()
- **ytick_labels**: `default` is floats; see more on ytick_labels [here]()
- **horizontal_gridlines_on**: bool (True or False); default False
- **vertical_gridlines_on**: bool (True or False); default False

## Returns
These are values that are stored in the `chart_skeleton` object once you've run the code. **You will rarely ever need these,** but you can use this object, as well as other instances returned in the `chart_skeleton` to add custom matplotlib layers to your chart.
- **ax**: [matploblin.axes class](https://matplotlib.org/stable/api/axes_api.html)

## Examples
```python
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
```
![cs_example_1](https://github.com/alexdsbreslav/quicklooks/assets/21344372/2148ba7f-ccf4-4fc4-ac90-1e3a273de488)

```python
chart_skeleton = ql.chart_skeleton(
size = ql.chart_size.notebook,
color_library = ql.color_libraries.mariglow,
font = ql.fonts.oswald,
title = 'Montly Active Users',
xlabel = 'Quarter',
ylabel = 'MAU',
x_min_max = ('2023-01-01','2024-02-15'), y_min_max = (0,10e6),
xtick_interval = 3, ytick_interval = 1e6,
xtick_labels = ql.chart_xlabel.quarters,
ytick_labels = ql.chart_ylabel.millions,
horizontal_gridlines_on = True,
vertical_gridlines_on = True);
```
![cs_example_2](https://github.com/alexdsbreslav/quicklooks/assets/21344372/82720ebd-8aa1-4d9a-a910-f6f66329e589)

## Next steps...
Now you have a chart skeleton! The next step is to visualize your data using plots (e.g. line plots, bar plots, scatter plots, histograms) on top of your chart skeleton. [Click here](https://github.com/alexdsbreslav/quicklooks/tree/master/how_to_use_quicklooks) to go to the directory of plots that you can add.
