class templates:
    '''
    print(ql.templates.REPLACE_WITH_TEMPLATE_NAME)
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
