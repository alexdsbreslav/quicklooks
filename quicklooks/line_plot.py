import numpy as np
import matplotlib.pyplot as plt
from .plot_and_text_styling import define_markersize
import pandas as pd
from datetime import timedelta

class line_plot:
    """
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
    """

    def __init__(self, chart_skeleton, x, y, yerror, linewidth, linestyle,
    color, marker_shape, opacity, label, plot_label, layer_order):

        if not chart_skeleton.ax:
            raise Exception('''The chart skeleton has not been built. \
            You must build a chart skeleton for each new plot that you \
            want to create.''')
        # ---- check data types
        if type(x) in [str, int, float, bool]:
            raise TypeError('''x is not properly defined. x should be a \
            1 dimensional array of values.''')
        if type(y) in [str, int, float, bool]:
            raise TypeError('''y is not properly defined. y should be a \
            1 dimensional array of values.''')
        if type(yerror) in [str, int, float, bool]:
            raise TypeError('''yerror is not properly defined. If you do not need \
            error represented on your line plot, set yerror = None.\n'
            'If you need yerror on your line plot, ensure that it is a \
            1 dimensional array of values.''')

        # ---- check data shapes
        if np.shape(np.shape(x))[0] != 1:
            raise ValueError('x is not properly defined.; it is a {} x {} array.\
             x must be 1-dimensional array.'.format(np.shape(x)[0],
                                                    np.shape(x)[1]))
        if np.shape(np.shape(y))[0] != 1:
            raise ValueError('y is not properly defined.; it is a {} x {} array.\
             y must be 1-dimensional array.'.format(np.shape(y)[0],
                                                    np.shape(y)[1]))
        if np.shape(x) != np.shape(y):
            raise ValueError('x and y are not the same shape. x has {} values \
            and y has {} values'.format(np.shape(x)[0], np.shape(y)[0]))

        # ---- define shades of color
        line = color[1]
        fill = color[0]
        edge = color[2]

        # ---- define markersize
        markersize, markeredgewidth = define_markersize(chart_skeleton.size,
                                                        marker_shape)

        # ---- plot y error as fill between
        if yerror is not None:
            fill = chart_skeleton.ax.fill_between(
                                  x,
                                  y - yerror,
                                  y + yerror,
                                  color = fill,
                                  label = None,
                                  alpha = 0.6 if fill == '#000000' else 0.8,
                                  zorder = layer_order + 2);

        else:
            fill = None
        # ---- plot mean line
        mean = chart_skeleton.ax.plot(
                    x,
                    y,
                    linewidth = linewidth,
                    linestyle = linestyle,
                    color = line,
                    marker = marker_shape,
                    markersize = markersize,
                    markeredgecolor = edge,
                    markeredgewidth = markeredgewidth,
                    alpha = opacity,
                    label = label,
                    solid_capstyle='round',
                    zorder = layer_order + 2);

        # ---- outline fill between
        if yerror is not None:
            ub = chart_skeleton.ax.plot(
                        x,
                        y + yerror,
                        linewidth = 0.5,
                        color = edge,
                        label = None,
                        zorder = layer_order + 2);
            lb = chart_skeleton.ax.plot(
                        x,
                        y - yerror,
                        linewidth = 0.5,
                        color = edge,
                        label = None,
                        zorder = layer_order + 2);
        else:
            ub = None
            lb = None

        if plot_label:
            if type(x) is pd.core.series.Series:
                x_end = x.iloc[-1]
            else:
                x_end = x[-1]

            if type(y) is pd.core.series.Series:
                y_end = y.iloc[-1]
            else:
                y_end = y[-1]

            if chart_skeleton.xaxis_type == 'timeseries':
                x_loc = x_end + timedelta(chart_skeleton.xrange*0.01)
            else:
                x_loc = x_end + (chart_skeleton.xrange)*0.01

            text = chart_skeleton.ax.text(
                    x_loc,
                    y_end,
                    label,
                    fontproperties=chart_skeleton.font_style.label,
                    horizontalalignment = 'left',
                    verticalalignment = 'center',
                    size = chart_skeleton.font_style.size.l,
                    color = line,
                    zorder = layer_order + 2);

        self.line_obj = mean
        self.yerr_fill = fill
        self.yerr_ub = ub
        self.yerr_lb = lb
