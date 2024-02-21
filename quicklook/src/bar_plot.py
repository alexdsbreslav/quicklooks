import numpy as np
import matplotlib.pyplot as plt

class bar_plot:
    """
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
    """

    def __init__(self, chart_skeleton, xlabels, y, yerror, bars_per_xlabel,
                 bar_index, color, opacity, label, layer_order):

        if not chart_skeleton.ax:
            raise Exception('''The chart skeleton has not been built.
            You must build a chart skeleton for each new plot that you want \
            to create.''')

        if chart_skeleton.xaxis_type == 'timeseries':
            raise Exception('''The chart skeleton xtick_label is set to a
                               timeseries (e.g., months, days). This is not
                               compatible with a scatter plot.''')

        if type(xlabels) in [str, int, float, bool]:
            raise TypeError('''x is not properly defined.
            x should be a 1 dimensional array of values.''')

        if type(y) in [str, int, float, bool]:
            raise TypeError('''y is not properly defined.
            y should be a 1 dimensional array of values.''')

        if type(yerror) in [str, int, float, bool]:
            raise TypeError('''yerror is not properly defined. If you do not
            need error represented on your line plot, set yerror = None.\n'
            'If you need yerror on your line plot,
            ensure that it is a 1 dimensional array of values.''')

        if type(bar_index) is not int:
            raise TypeError('''bar_index is not properly defined.
            It must be an integer between 0 and bars_per_xlabel''')

        if type(bars_per_xlabel) is not int or bars_per_xlabel < 1:
            raise TypeError('''bars_per_xlabel is not properly defined.
            It must be an integer >= 1''')

        if bar_index >= bars_per_xlabel:
            raise IndexError('''bar_index is not properly defined.
            It must be an integer between 0 and bars_per_xlabel-1''')

        # ---- check data shapes
        if np.shape(np.shape(xlabels))[0] != 1:
            raise ValueError('''x is not properly defined.; it is a {} x {} array.
            x must be 1-dimensional array.'''.format(np.shape(xlabels)[0],
                                                   np.shape(xlabels)[1]))
        if np.shape(np.shape(y))[0] != 1:
            raise ValueError('''y is not properly defined.; it is a {} x {} array.
            y must be 1-dimensional array.'''.format(np.shape(y)[0],
                                                   np.shape(y)[1]))
        if np.shape(xlabels) != np.shape(y):
            raise ValueError('''x and y are not the same shape. x has {} values
            and y has {} values'''.format(np.shape(xlabels)[0], np.shape(y)[0]))

        xlim = (-0.5,len(xlabels)-0.5)
        plt.xlim(xlim[0], xlim[1]);
        plt.xticks(ticks=range(len(xlabels)), labels=xlabels);
        label_to_x = dict(zip(xlabels, chart_skeleton.ax.get_xticks()))

        # ---- adjust for number of xlabels
        width = 0.8 if len(xlabels) <= 2 else 0.8-(len(xlabels)*0.01)
        # ---- adjust for number of bars at xlabel
        width = width/bars_per_xlabel

        # --- get offsets based on number of bars at xlabel
        idx = [i for i in range(bars_per_xlabel)]
        bar_offsets = [(i - np.median(idx))*1.1 for i in idx]
        offset = bar_offsets[bar_index]*width

        # ---- get x and y locs
        ylim = chart_skeleton.ax.get_ylim()
        x_loc = [label_to_x[i]+offset for i in xlabels]
        bottom = np.array([(i/abs(i)) * ((ylim[1]-ylim[0])*0.002) for i in y])
        height = y-bottom
        zorder = 1

        line = color[0]
        fill = color[1]
        edge = color[2]

        bar = chart_skeleton.ax.bar(x=x_loc, width=width,
                                 height=height, bottom=bottom,
                                 color=fill,
                                 edgecolor=edge,
                                 linewidth=2,
                                 joinstyle='round',
                                 alpha=opacity,
                                 label=label,
                                 zorder = layer_order + 2)

        if yerror is not None:
            total_bars = bars_per_xlabel * len(x_loc)
            if total_bars >= 30:
                err_width = 2
            elif total_bars >= 20:
                err_width = 3
            elif total_bars >= 10:
                err_width = 4
            else:
                err_width = 5

            for i in range(len(x_loc)):
                chart_skeleton.ax.plot(np.full(10,x_loc[i]),
                np.linspace(y[i]-yerror[i], y[i]+yerror[i],10),
                linewidth=err_width, color=edge, alpha=opacity,
                zorder = layer_order + 2+0.1, solid_capstyle='round');
        else:
            error = None

        self.bar_obj = bar
        self.xlim = xlim
        self.zorder = layer_order + 2
