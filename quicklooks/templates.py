class templates:
    '''
    print(ql.templates.REPLACE_WITH_TEMPLATE_NAME)
    '''
    bar_plot = \
'''
chart_skeleton = ql.chart_skeleton(
size = ql.chart_size.notebook,
color_library = ql.color_libraries.opencolor,
font = ql.fonts.rubik,
title = '',
xlabel = '',
ylabel = '',
x_min_max = (0, 1), y_min_max = (0,1),
xtick_interval = 0.1, ytick_interval = 0.1,
xtick_labels = ql.chart_xlabel.default,
ytick_labels = ql.chart_ylabel.default,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

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
'''
    
    grouped_bar = \
'''
chart_skeleton = ql.chart_skeleton(
size = ql.chart_size.notebook,
color_library = ql.color_libraries.opencolor,
font = ql.fonts.rubik,
title = '',
xlabel = '',
ylabel = '',
x_min_max = (0, 1), y_min_max = (0,1),
xtick_interval = 0.1, ytick_interval = 0.1,
xtick_labels = ql.chart_xlabel.default,
ytick_labels = ql.chart_ylabel.default,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

xlabels = ['Group 1', 'Group 2', 'Group 3']

bar = ql.bar_plot(chart_skeleton,
xlabels = xlabels,
y = ,
yerror = None, #If no values, None
bars_per_xlabel = 2,
bar_index = 0,
color = chart_skeleton.color_library.default,
opacity = 1,
label = 'Color A',
layer_order = 1)

bar = ql.bar_plot(chart_skeleton,
xlabels = xlabels,
y = ,
yerror = None, #If no values, None
bars_per_xlabel = 2,
bar_index = 1,
color = chart_skeleton.color_library.orange,
opacity = 1,
label = 'Color B',
layer_order = 1)

legend = ql.legend(chart_skeleton,
legend_location = ql.legend.loc.best, frame=False);
'''
    
    line_plot = \
'''
chart_skeleton = ql.chart_skeleton(
size = ql.chart_size.notebook,
color_library = ql.color_libraries.opencolor,
font = ql.fonts.rubik,
title = '',
xlabel = '',
ylabel = '',
x_min_max = (0, 1), y_min_max = (0,1),
xtick_interval = 0.1, ytick_interval = 0.1,
xtick_labels = ql.chart_xlabel.default,
ytick_labels = ql.chart_ylabel.default,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# -- line #1
line = ql.line_plot(chart_skeleton,
x = ,
y = ,
yerror = None, #If no values, None
color = chart_skeleton.color_library.default,
linewidth = 3,
linestyle = 'solid', #['solid', 'dashed', 'dotted', 'dashdot']
marker_shape = None, #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label = '',
plot_label = True,
layer_order = 1)

# -- line #2
line = ql.line_plot(chart_skeleton,
x = ,
y = ,
yerror = None, #If no values, None
color = chart_skeleton.color_library.default,
linewidth = 3,
linestyle = 'solid', #['solid', 'dashed', 'dotted', 'dashdot']
marker_shape = None, #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label = '',
plot_label = True,
layer_order = 1)
'''
    timeseries = \
'''
chart_skeleton = ql.chart_skeleton(
size = ql.chart_size.notebook,
color_library = ql.color_libraries.opencolor,
font = ql.fonts.rubik,s
title = '',
xlabel = '',
ylabel = '',
x_min_max = ('YYYY-MM-DD', 'YYYY-MM-DD'), y_min_max = (0,1e3),
xtick_interval = 14, ytick_interval = 100,
xtick_labels = ql.chart_xlabel.days,
ytick_labels = ql.chart_ylabel.default,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# -- line #1
line = ql.line_plot(chart_skeleton,
x = ,
y = ,
yerror = None, #If no values, None
color = chart_skeleton.color_library.default,
linewidth = 3,
linestyle = 'solid', #['solid', 'dashed', 'dotted', 'dashdot']
marker_shape = None, #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label = '',
plot_label = True,
layer_order = 1)

# -- line #2
line = ql.line_plot(chart_skeleton,
x = ,
y = ,
yerror = None, #If no values, None
color = chart_skeleton.color_library.default,
linewidth = 3,
linestyle = 'solid', #['solid', 'dashed', 'dotted', 'dashdot']
marker_shape = None, #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label = '',
plot_label = True,
layer_order = 1)
'''
    stepwise_reveal = \
'''
for element in range(4): #insert number of elements here
    chart_skeleton = ql.chart_skeleton(
    size = ql.chart_size.half_slide,
    color_library = ql.color_libraries.mariglow,
    title = '',
    xlabel = '',
    ylabel = '',
    x_min_max = (0,1), y_min_max = (0,1),
    xtick_interval = 0.25, ytick_interval = 0.25,
    xtick_labels = ql.chart_xlabel.default,
    ytick_labels = ql.chart_ylabel.default,
    horizontal_gridlines_on = False,
    vertical_gridlines_on = False);

    # ---- first element ---------------------------------------------------
    if element >= 0:
        # ---- enter code here

    # ---- second element --------------------------------------------------
    if element >= 1:
        # ---- enter code here

    # ---- third element ---------------------------------------------------
    if element >= 2:
        # ---- enter code here

    # ---- fourth element --------------------------------------------------
    if element >= 3:
        # ---- enter code here

    legend = ql.legend(chart_skeleton,
    legend_location = ql.legend.loc.best, frame=False);
'''
