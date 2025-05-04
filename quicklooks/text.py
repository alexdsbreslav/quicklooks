from datetime import datetime

class text:
    """
    text = ql.text(chart_skeleton,
    text = '',
    text_size = chart_skeleton.font_style.size.m,
    color = chart_skeleton.color_library.text,
    text_location_on_x_axis = ,
    text_location_on_y_axis = ,
    horizontal_align = 'center', #['center', 'left', 'right']
    vertical_align = 'center', #['center', 'top', 'bottom']
    rotation = 0,
    box_around_text = False,
    layer_order = 1)
    """

    def __init__(self,chart_skeleton, text, text_size, color,
                 text_location_on_x_axis, text_location_on_y_axis,
                 horizontal_align, vertical_align, rotation,
                 box_around_text, layer_order):

        if not chart_skeleton.ax:
            raise Exception('''The chart skeleton has not been built. \
            You must build a chart skeleton for each new plot that you \
            want to create.''')

        if chart_skeleton.xaxis_type == 'timeseries' and type(text_location_on_x_axis) is str:
            text_location_on_x_axis = datetime.strptime(text_location_on_x_axis,'%Y-%m-%d')
        elif chart_skeleton.xaxis_type == 'timeseries' and type(text_location_on_x_axis) is not str:
            raise TypeError('''If xtick_label is set to timeseries,
            location must be a string in the format YYYY-MM-DD''')

        if box_around_text:
            text = chart_skeleton.ax.text(
                    text_location_on_x_axis,
                    text_location_on_y_axis,
                    text,
                    fontproperties=chart_skeleton.font_style.label,
                    horizontalalignment=horizontal_align,
                    verticalalignment=vertical_align,
                    size = text_size,
                    color = color if type(color) is str else color[1],
                    bbox = dict(facecolor = chart_skeleton.color_library.background,
                    edgecolor = chart_skeleton.color_library.text,
                    boxstyle = 'round, pad = 0.5',
                    rotation = rotation,
                    alpha = 1,
                    linewidth = 0.5,
                    zorder = layer_order + 2));
        else:
            text = chart_skeleton.ax.text(
                    text_location_on_x_axis,
                    text_location_on_y_axis,
                    text,
                    fontproperties=chart_skeleton.font_style.label,
                    horizontalalignment = horizontal_align,
                    verticalalignment = vertical_align,
                    size = text_size,
                    color = color if type(color) is str else color[1],
                    rotation = rotation,
                    zorder = layer_order + 2);

        self.text_obj = text
