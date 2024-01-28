def add_text(chart_skeleton, text, color_name, color_brightness,
             text_location_on_x_axis,
             text_location_on_y_axis, horizontal_align, vertical_align,
             box_around_text, layer_order, font_size='default'):

    if not chart_skeleton.ax:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    if font_size == 'default':
        font_size = chart_skeleton['fonts']['size'][1]

    line,_,_ = define_colors(chart_skeleton, color_name, color_brightness)

    if box_around_text:d
        text = chart_skeleton.ax.text(
                text_location_on_x_axis,
                text_location_on_y_axis,
                text,
                fontproperties=chart_skeleton['fonts']['label'],
                horizontalalignment=horizontal_align,
                verticalalignment=vertical_align,
                size = font_size,
                color = line,
                bbox = dict(facecolor = chart_skeleton['color_library']['properties']['background'],
                edgecolor = line,
                boxstyle = 'round, pad = 0.5',
                alpha = 1,
                linewidth = 0.5,
                zorder = layer_order + 2));
    else:
        text = chart_skeleton.ax.text(
                text_location_on_x_axis,
                text_location_on_y_axis,
                text,
                fontproperties=chart_skeleton['fonts']['label'],
                horizontalalignment = horizontal_align,
                verticalalignment = vertical_align,
                size = chart_skeleton['fonts']['size'][1],
                color = line,
                zorder = layer_order + 2);

    return {'text': text}

add_text.__doc__ = \
    """
    text = quicklook.add_text(chart_skeleton,
    text = '',
    color_name = '{}', #{}
    color_brightness = 'default', #{}
    text_location_on_x_axis = ,
    text_location_on_y_axis = ,
    horizontal_align = 'center', #['center', 'left', 'right']
    vertical_align = 'center', #['center', 'top', 'bottom']
    box_around_text = False,
    layer_order = 1)
    """.format('text',
               list(color_library['colors'].keys()),
               list(color_library['properties']['brightness'].keys()))
