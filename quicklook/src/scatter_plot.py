import matplotlib.pyplot as plt
import matplotlib.patches as patch
import numpy as np
from .plot_and_text_styling import define_markersize

class scatter_plot:
    '''
    scatter = ql.scatter_plot(chart_skeleton,
    x = ,
    y = ,
    x_error = None, #If no values, None
    y_error = None, #If no values, None
    color = chart_skeleton.color_library.default,
    marker_shape = 'o', #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x', '']
    opacity = 1,
    label = '',
    layer_order = 1)
    '''
    def __init__(self, chart_skeleton, x, y, x_error, y_error,
    color, marker_shape, opacity, label, layer_order):

        if not chart_skeleton.ax:
            raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                            'Run quicklook.build_chart_skeleton to build a chart skeleton.')

        if chart_skeleton.xaxis_type == 'timeseries':
            raise Exception('''The chart skeleton xtick_label is set to a timeseries (e.g., months, days).
                               This is not compatible with a scatter plot.''')
        # ---- check data types
        if type(x) in [str, int, float, bool]:
            raise TypeError('x is not properly defined. x should be a 1 dimensional array of values.')
        if type(y) in [str, int, float, bool]:
            raise TypeError('y is not properly defined. y should be a 1 dimensional array of values.')
        if type(x_error) in [str, float, int, bool]:
            raise TypeError('y_error is not properly defined. If you do not need error represented on your line plot, set y_error = None.\n'
                            'If you need y_error on your line plot, ensure that it is a 1 dimensional array of values.')
        if type(y_error) in [str, float, int, bool]:
            raise TypeError('y_error is not properly defined. If you do not need error represented on your line plot, set y_error = None.\n'
                            'If you need y_error on your line plot, ensure that it is a 1 dimensional array of values.')
        # ---- check data shapes
        if np.shape(np.shape(x))[0] != 1:
            raise ValueError('x is not properly defined.; it is a {} x {} array. x must be 1-dimensional array.'.format(np.shape(x)[0], np.shape(x)[1]))
        if np.shape(np.shape(y))[0] != 1:
            raise ValueError('y is not properly defined.; it is a {} x {} array. y must be 1-dimensional array.'.format(np.shape(y)[0], np.shape(y)[1]))
        if np.shape(x) != np.shape(y):
            raise ValueError('x and y are not the same shape. x has {} values and y has {} values'.format(np.shape(x)[0], np.shape(y)[0]))

        # ---- colors
        line = color[1]
        fill = color[0]
        edge = color[2]

        # ---- markers
        markersize, markeredgewidth = define_markersize(chart_skeleton.size, marker_shape)

        # ---- If X and Y Error, plot clouds
        if x_error is not None and y_error is not None:
            shape = [np.shape(i) for i in [x,y,x_error,y_error]]
            if not shape[0] == shape[1] == shape[2] == shape[3]:
                raise ValueError('x, y, x_error, and y_error are not the same length. All four inputs must have the same number of items in them.')

            if not shape[0]:
                x = [x]
                y = [y]
                x_error = [x_error]
                y_error = [y_error]

            coord = tuple(zip(x,y))
            err = tuple(zip(x_error,y_error))

            error = {'fill': [], 'outline': []}
            for pt in range(len(coord)):
                err_fill = chart_skeleton.ax.add_patch(patch.Ellipse((coord[pt][0],coord[pt][1]), err[pt][0] * 2, err[pt][1] * 2,
                                                        facecolor = fill, alpha = .8, zorder = layer_order + 2))
                err_outline = chart_skeleton.ax.add_patch(patch.Ellipse((coord[pt][0],coord[pt][1]), err[pt][0] * 2, err[pt][1] * 2,
                                                        facecolor = 'none', edgecolor = edge, alpha = 1, linewidth = 0.5, zorder = layer_order + 2))
                # ---- collect artists to output
                error['fill'].append(err_fill)
                error['outline'].append(err_outline)

        # Just x error, plot error bars
        elif x_error is not None and y_error is None:
            error = chart_skeleton.ax.errorbar(x,y,xerr=x_error,linestyle='',
            ecolor=edge, elinewidth=markeredgewidth, capsize=2, capthick=2, zorder = layer_order + 2)

        # Just y error, plot error bars
        elif x_error is None and y_error is not None:
            error = chart_skeleton.ax.errorbar(x,y,yerr=y_error,linestyle='',
            ecolor=edge, elinewidth=markeredgewidth, capsize=2, zorder = layer_order + 2)
        else:
            error = None

        # ---- plot points
        scatter = chart_skeleton.ax.plot(
                x,
                y,
                linewidth = 0,
                marker = marker_shape,
                markersize = markersize,
                mec = None if x_error is not None and y_error is not None else edge,
                mfc = line,
                mew = 0 if x_error is not None and y_error is not None else markeredgewidth,
                label = label,
                alpha = opacity,
                zorder = layer_order + 2);

        self.scatter_obj = scatter
        self.error_obj = error
