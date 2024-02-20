import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from .plot_and_text_styling import define_markersize
from datetime import datetime

class reference_line:
    """
    ref_line = ql.reference_line(chart_skeleton,
    line_type = 'h', #['h' (hor), 'v' (vert), 'du' (diag-up), 'dd' (diag-down)]
    location = , #If diag-up or diag-down, None
    color = chart_skeleton.color_library.text,
    linewidth = 2,
    linestyle = '--', #['-', '--', ':', '-.']
    marker_shape = None, #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
    opacity = 1,
    label = '',
    layer_order = 1)
    """

    def __init__(self, chart_skeleton, line_type, location, color, linewidth,
    linestyle, marker_shape, opacity, label, layer_order):

        if not chart_skeleton.ax:
            raise Exception('The chart skeleton has not been built. \
            You must build a chart skeleton for each new plot that you \
            want to create.')

        # ---- define shades of color
        line = color[1]
        edge = color[2]

        markersize, markeredgewidth = define_markersize(chart_skeleton.size, marker_shape)

        if line_type == 'h':
            if chart_skeleton.xaxis_type == 'timeseries':
                x = pd.date_range(chart_skeleton.x_min_max[0],
                                  chart_skeleton.x_min_max[1],
                                  periods=10)
            else:
                x = np.linspace(chart_skeleton.x_min_max[0],
                                chart_skeleton.x_min_max[1],10)
            y = np.full(10,location)

        elif line_type == 'v':
            if chart_skeleton.xaxis_type == 'timeseries' and type(location) is str:
                location = datetime.strptime(location,'%Y-%m-%d')
            elif chart_skeleton.xaxis_type == 'timeseries' and type(location) is not str:
                raise TypeError('''If xtick_label is set to timeseries,
                location must be a string in the format YYYY-MM-DD''')

            x = np.full(10,location)
            y = np.linspace(chart_skeleton.y_min_max[0],
                            chart_skeleton.y_min_max[1],10)

        elif line_type == 'du':
            x = np.linspace(chart_skeleton.x_min_max[0],
                            chart_skeleton.x_min_max[1],10)
            y = np.linspace(chart_skeleton.y_min_max[0],
                            chart_skeleton.y_min_max[1],10)

            if location:
                print('location of ref_line ignored because line_type is diag-up')

        elif line_type == 'dd':
            x = np.linspace(chart_skeleton.x_min_max[0],
                            chart_skeleton.x_min_max[1],10)
            y = np.linspace(chart_skeleton.y_min_max[1],
                            chart_skeleton.y_min_max[0],10)

            if location:
                print('location of ref_line ignored because line_type is diag-down')
        else:
            raise Exception('''type is not properly defined. \
            type must be defined as h, v, du, dd''')

        line = chart_skeleton.ax.plot(
                x,
                y,
                linewidth = linewidth,
                linestyle = linestyle,
                color = line,
                marker = marker_shape,
                markersize = markersize,
                mec = edge,
                mew = markeredgewidth,
                alpha = opacity,
                label = label,
                zorder = layer_order + 2);

        self.line_obj = line
