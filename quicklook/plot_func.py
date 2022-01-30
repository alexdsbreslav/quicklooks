import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from .plot_func_internal import *
import os
import pandas as pd
import seaborn as sns
import warnings
import matplotlib.ticker as ticker


def build_chart_skeleton(size, title, ylabel, xlabel, x_min_max,
                         y_min_max, xtick_interval, ytick_interval,
                         xtick_labels, ytick_labels,
                         horizontal_gridlines_on, vertical_gridlines_on,
                         font_file='default'):

    """chart_skeleton = quicklook.build_chart_skeleton(
    size = 'half_slide', #['print', 'half_slide', 'full_slide']
    title = '',
    xlabel = '',
    ylabel = '',
    x_min_max = (0,1), y_min_max = (0,1),
    xtick_interval = 0.25, ytick_interval = 0.25,
    xtick_labels = 'default', #['default', 'percents', list]
    ytick_labels = 'default', #['default', 'percents', list]
    horizontal_gridlines_on = False,
    vertical_gridlines_on = False);
    """

    # ---- check size
    if size not in ['print', 'half_slide', 'full_slide']:
        raise Exception('Size not properly add_reference_lined: size must be set to print, half_slide, or full_slide.')
    # ---- check x and y tick labels
    if type(xtick_labels) not in [str, list]:
        raise Exception('xtick_labels not properly defined: xtick_labels must be set to default, percents, or defined as a list of strings.')

    if type(xtick_labels) is str and xtick_labels not in ['default', 'percents']:
        raise Exception('xtick_labels not properly defined: xtick_labels must be set to default, percents, or defined as a list of strings.')

    if type(ytick_labels) not in [str, list]:
        raise Exception('ytick_labels not properly defined: ytick_labels must be set to default, percents, or defined as a list of strings.')

    if type(ytick_labels) is str and ytick_labels not in ['default', 'percents']:
        raise Exception('ytick_labels not properly defined: ytick_labels must be set to default, percents, or defined as a list of strings.')
    # ---- check gridlines
    if vertical_gridlines_on not in [True, False]:
        raise Exception('Vertical gridlines is not properly defined: '
                        'vertical_gridlines_on must be set to True or False.')

    if horizontal_gridlines_on not in [True, False]:
        raise Exception('Horizontal gridlines is not properly defined: '
                        'horizontal_gridlines_on must be set to True or False.')

    # ---- check xtick and ytick intervals
    if xtick_interval > x_min_max[1] - x_min_max[0]:
        raise Exception('xtick_interval is not properly defined: ' \
                        'xtick_interval should be greater than x_max minus x_min. \n'
                        'Imagine the x-axis as a number line from x_min to x_max. xtick_interval'
                        'is the increment that you want to mark off on the number line.\n'
                        'For example, if x_min = 1, x_max = 3, and xtick_interval = 0.5 your x-axis'
                        'would have 1, 1.5, 2, 2.5, and 3 marked on it.')

    if ytick_interval > y_min_max[1] - y_min_max[0]:
        raise Exception('ytick_interval is not properly defined: ' \
                        'ytick_interval should be greater than y_max minus y_min. \n'
                        'Imagine the y-axis as a number line from y_min to y_max. ytick_interval'
                        'is the increment that you want to mark off on the number line.\n'
                        'For example, if y_min = 1, y_max = 3, and ytick_interval = 0.5 your y-axis'
                        'would have 1, 1.5, 2, 2.5, and 3 marked on it.')

    if (x_min_max[1]-x_min_max[0])/xtick_interval > 50:
        raise RuntimeError('quicklook is trying to plot too many xticks; increase the x_tick_interval')
    if (y_min_max[1]-y_min_max[0])/ytick_interval > 50:
        raise RuntimeError('quicklook is trying to plot too many yticks; increase the y_tick_interval')

    # ---- define plot style based on style and size choice
    figsize, label_pad, title_pad, linewidth, \
    tick_pad, tick_length, color_library, \
    fonts = define_plot_style(size, ylabel, font_file=font_file)

    # ---- create the plot
    fig, ax = plt.subplots(nrows=1, figsize = figsize)

    # ---- add the title
    ax.set_title(title, color = color_library['properties']['text'],
                 pad = title_pad, fontproperties = fonts['title'])

    # ---- create a patch to set the background color of the plot
    ax.patch.set_xy((-0.16, -0.14))
    ax.patch.set_height(1.2)
    ax.patch.set_width(1.28)
    ax.set_facecolor(color_library['properties']['background'])

    # ---- set facecolor of fig (around ax face)
    fig.set_facecolor(color_library['properties']['background'])

    # ---- add grid lines if necessary
    if horizontal_gridlines_on == True:
        ax.yaxis.grid(which='major', linestyle=':',
        linewidth = linewidth, color = '0.8', zorder=1)

    if vertical_gridlines_on == True:
        ax.xaxis.grid(which='major', linestyle=':',
        linewidth = linewidth, color = '0.8', zorder=1)

    # ---- style the axis lines
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_linewidth(linewidth)
        ax.spines[spine].set_color(color_library['properties']['text'])
        ax.spines[spine].set_zorder(2)

    # ---- style the axis ticks
    ax.tick_params('x', colors=color_library['properties']['text'],
                   width = linewidth, pad = tick_pad[0], length = tick_length)

    ax.tick_params('y', colors=color_library['properties']['text'],
                   width = linewidth, pad = tick_pad[1], length = tick_length)

    for tick in ax.get_xticklabels():
        tick.set_font_properties(fonts['label'])
    for tick in ax.get_yticklabels():
        tick.set_font_properties(fonts['label'])

    # ---- set the axis limits and number of ticks
    ax.set_ylim(y_min_max)
    ax.set_xlim(x_min_max)

    # ---- set the number of ticks on the axes
    ax.yaxis.set_major_locator(plt.MultipleLocator(ytick_interval))
    ax.xaxis.set_major_locator(plt.MultipleLocator(xtick_interval))

    # ---- label the y axis
    ax.set_ylabel(ylabel, color=color_library['properties']['text'],
                  rotation = 0, labelpad = label_pad[1],
                  horizontalalignment = 'center',
                  linespacing = 1.6, fontproperties = fonts['label'])

    # ---- label the x axis
    ax.set_xlabel(xlabel, color = color_library['properties']['text'],
                  labelpad = label_pad[0], fontproperties = fonts['label'])

    # ---- set the x tick labels
    if xtick_labels == 'default':
        pass
    elif xtick_labels == 'percents':
        ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=x_min_max[1]))
    elif type(xtick_labels) is list:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')

            # ---- get label positions and determine which are displayed
            label_position = [i.get_position()[0] for i in ax.get_xticklabels()]
            displayed_labels = label_position[1:-1]

            # ---- check length of list of xtick_labels
            if len(xtick_labels) != len(displayed_labels):
                raise Exception('Expected {} new labels; {} are defined.'.format(len(displayed_labels), len(xtick_labels)))
            # ---- create a new list of labels
            new_labels = [None] + [i for i in xtick_labels] + [None]
            # ---- update with new labels
            ax.set_xticklabels(new_labels)

    # ---- set the y tick labels
    if ytick_labels == 'default':
        pass
    elif ytick_labels == 'percents':
        ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=y_min_max[1]))
    elif type(ytick_labels) is list:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')

            # ---- get label positions and determine which are displayed
            label_position = [i.get_position()[1] for i in ax.get_yticklabels()]
            displayed_labels = label_position[1:-1]

            # ---- check length of list of xtick_labels
            if len(ytick_labels) != len(displayed_labels):
                raise Exception('Expected {} new labels; {} are defined.'.format(len(displayed_labels), len(xtick_labels)))
            # ---- create a new list of labels
            new_labels = [None] + [i for i in xtick_labels] + [None]
            # ---- update with new labels
            ax.set_yticklabels(new_labels)

    plt.tight_layout()
    chart_skeleton = {'fig': fig, 'ax': ax, 'color_library': color_library,
                      'size': size, 'fonts': fonts, 'x_min_max': x_min_max,
                      'y_min_max': y_min_max}

    return chart_skeleton

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Plot Bar
def add_bar_plot(chart_skeleton, x_labels, y, y_error,
                 bars_at_each_xlabel, bar_index, color_name,
                 color_brightness,opacity, label_for_legend, layer_order):

    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    if type(x_labels) in [str, int, float, bool]:
        raise TypeError('x is not properly defined. x should be a 1 dimensional array of values.')
    if type(y) in [str, int, float, bool]:
        raise TypeError('y is not properly defined. y should be a 1 dimensional array of values.')
    if type(y_error) in [str, int, float, bool]:
        raise TypeError('y_error is not properly defined. If you do not need error represented on your line plot, set y_error = None.\n'
                        'If you need y_error on your line plot, ensure that it is a 1 dimensional array of values.')
    if type(bar_index) is not int:
        raise TypeError('bar_index is not properly defined. It must be an integer between 0 and bars_at_each_xlabel')

    if type(bars_at_each_xlabel) is not int or bars_at_each_xlabel < 1:
        raise TypeError('bars_at_each_xlabel is not properly defined. It must be an integer >= 1')

    if bar_index >= bars_at_each_xlabel:
        raise IndexError('bar_index is not properly defined. It must be an integer between 0 and bars_at_each_xlabel-1')

    # ---- check data shapes
    if np.shape(np.shape(x_labels))[0] != 1:
        raise ValueError('x is not properly defined.; it is a {} x {} array. x must be 1-dimensional array.'.format(np.shape(x_labels)[0], np.shape(x_labels)[1]))
    if np.shape(np.shape(y))[0] != 1:
        raise ValueError('y is not properly defined.; it is a {} x {} array. y must be 1-dimensional array.'.format(np.shape(y)[0], np.shape(y)[1]))
    if np.shape(x_labels) != np.shape(y):
        raise ValueError('x and y are not the same shape. x has {} values and y has {} values'.format(np.shape(x_labels)[0], np.shape(y)[0]))

    xlim = (-0.5,len(x_labels)-0.5)
    plt.xlim(xlim[0], xlim[1]);
    plt.xticks(ticks=range(len(x_labels)), labels=x_labels);
    label_to_x = dict(zip(x_labels, chart_skeleton['ax'].get_xticks()))

    # ---- adjust for number of xlabels
    width = 0.8 if len(x_labels) <= 2 else 0.8-(len(x_labels)*0.01)
    # ---- adjust for number of bars at xlabel
    width = width/bars_at_each_xlabel

    # --- get offsets based on number of bars at xlabel
    idx = [i for i in range(bars_at_each_xlabel)]
    bar_offsets = [(i - np.median(idx))*1.1 for i in idx]
    offset = bar_offsets[bar_index]*width

    # ---- get x and y locs
    ylim = chart_skeleton['ax'].get_ylim()
    x_loc = [label_to_x[i]+offset for i in x_labels]
    bottom = np.array([(i/abs(i)) * ((ylim[1]-ylim[0])*0.001) for i in y])
    height = y-bottom
    zorder = 1

    line, fill, edge = define_colors(chart_skeleton, color_name, color_brightness)

    bar = chart_skeleton['ax'].bar(x=x_loc, width=width,
                             height=height, bottom=bottom,
                             color=fill,
                             edgecolor=edge,
                             linewidth=3,
                             joinstyle='round',
                             alpha=opacity,
                             label=label_for_legend,
                             zorder = layer_order + 2)

    if y_error is not None:
        error = chart_skeleton['ax'].errorbar(x=x_loc, y=y, yerr=y_error,
                                      linewidth=0, elinewidth=3, color=edge,
                                      alpha=opacity,zorder = layer_order + 2+0.1,
                                      solid_capstyle='round');
    else:
        error = None

    return {'bar': bar, 'error': error, 'xlim': xlim, 'zorder': layer_order + 2}

# ---- set doc string
add_bar_plot.__doc__ = \
    """
    bar = quicklook.add_bar_plot(chart_skeleton,
    x_labels = ,
    y = ,
    y_error = None, #If no values, None
    bars_at_each_xlabel = 1,
    bar_index = 0,
    color_name = '{}', #{}
    color_brightness = 'default', #{}
    opacity = 1,
    label_for_legend = '',
    layer_order = 1)
    """.format(color_library['properties']['default_color'],
               list(color_library['colors'].keys()),
               list(color_library['properties']['brightness'].keys()))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Plot Line
def add_line_plot(chart_skeleton, x, y, y_error, linewidth,
              linestyle, color_name, color_brightness, marker_shape,
              opacity, label_for_legend, layer_order):

    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')
    # ---- check data types
    if type(x) in [str, int, float, bool]:
        raise TypeError('x is not properly defined. x should be a 1 dimensional array of values.')
    if type(y) in [str, int, float, bool]:
        raise TypeError('y is not properly defined. y should be a 1 dimensional array of values.')
    if type(y_error) in [str, int, float, bool]:
        raise TypeError('y_error is not properly defined. If you do not need error represented on your line plot, set y_error = None.\n'
                        'If you need y_error on your line plot, ensure that it is a 1 dimensional array of values.')
    # ---- check data shapes
    if np.shape(np.shape(x))[0] != 1:
        raise ValueError('x is not properly defined.; it is a {} x {} array. x must be 1-dimensional array.'.format(np.shape(x)[0], np.shape(x)[1]))
    if np.shape(np.shape(y))[0] != 1:
        raise ValueError('y is not properly defined.; it is a {} x {} array. y must be 1-dimensional array.'.format(np.shape(y)[0], np.shape(y)[1]))
    if np.shape(x) != np.shape(y):
        raise ValueError('x and y are not the same shape. x has {} values and y has {} values'.format(np.shape(x)[0], np.shape(y)[0]))

    line, fill, edge = define_colors(chart_skeleton, color_name, color_brightness)
    markersize, markeredgewidth = define_markersize(chart_skeleton['size'], marker_shape)

    # ---- plot y error as fill between
    if y_error is not None:
        fill = chart_skeleton['ax'].fill_between(
                              x,
                              y - y_error,
                              y + y_error,
                              color = fill,
                              label = None,
                              alpha = 0.2,
                              zorder = layer_order + 2);

    else:
        fill = None
    # ---- plot mean line
    mean = chart_skeleton['ax'].plot(
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
                label = label_for_legend,
                solid_capstyle='round',
                zorder = layer_order + 2);

    # ---- outline fill between
    if y_error is not None:
        ub = chart_skeleton['ax'].plot(
                    x,
                    y + y_error,
                    linewidth = 0.5,
                    color = edge,
                    label = None,
                    zorder = layer_order + 2);
        lb = chart_skeleton['ax'].plot(
                    x,
                    y - y_error,
                    linewidth = 0.5,
                    color = edge,
                    label = None,
                    zorder = layer_order + 2);
    else:
        ub = None
        lb = None

    return {'line': mean, 'y_err_fill': fill, 'y_err_ub': ub, 'y_err_lb': lb}

# ---- set doc string
add_line_plot.__doc__ = \
    """
    line = quicklook.add_line_plot(chart_skeleton,
    x = ,
    y = ,
    y_error = None, #If no values, None
    color_name = '{}', #{}
    color_brightness = 'default', #{}
    linewidth = 7,
    linestyle = '-', #['-', '--', ':', '-.']
    marker_shape = '.', #['None', 'o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
    opacity = 1,
    label_for_legend = '',
    layer_order = 1)
    """.format(color_library['properties']['default_color'],
               list(color_library['colors'].keys()),
               list(color_library['properties']['brightness'].keys()))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Plot scatter
def add_scatter_plot(chart_skeleton, x, y, x_error, y_error,
                 color_name, color_brightness, marker_shape,
                 opacity, label_for_legend, layer_order):

    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')
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

    line, fill, edge = define_colors(chart_skeleton, color_name, color_brightness)
    markersize, markeredgewidth = define_markersize(chart_skeleton['size'], marker_shape)

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
            err_fill = chart_skeleton['ax'].add_patch(patch.Ellipse((coord[pt][0],coord[pt][1]), err[pt][0] * 2, err[pt][1] * 2,
                                                    facecolor = fill, alpha = .8, zorder = layer_order + 2))
            err_outline = chart_skeleton['ax'].add_patch(patch.Ellipse((coord[pt][0],coord[pt][1]), err[pt][0] * 2, err[pt][1] * 2,
                                                    facecolor = 'none', edgecolor = edge, alpha = 0.3, linewidth = 2, zorder = layer_order + 2))
            # ---- collect artists to output
            error['fill'].append(err_fill)
            error['outline'].append(err_outline)

    # Just x error, plot error bars
    elif x_error is not None and y_error is None:
        error = chart_skeleton['ax'].errorbar(x,y,xerr=x_error,linestyle='',
        ecolor=edge, elinewidth=markeredgewidth, capsize=2, capthick=2, zorder = layer_order + 2)

    # Just y error, plot error bars
    elif x_error is None and y_error is not None:
        error = chart_skeleton['ax'].errorbar(x,y,yerr=y_error,linestyle='',
        ecolor=edge, elinewidth=markeredgewidth, capsize=2, zorder = layer_order + 2)
    else:
        error = None

    # ---- plot points
    scatter = chart_skeleton['ax'].plot(
            x,
            y,
            linewidth = 0,
            color = line,
            marker = marker_shape,
            markersize = markersize,
            mec = edge,
            mfc = fill,
            mew = markeredgewidth,
            label = label_for_legend,
            alpha = opacity,
            zorder = layer_order + 2);

    return {'scatter': scatter, 'error': error}

# ---- set doc string
add_scatter_plot.__doc__ = \
    """
    scatter = quicklook.add_scatter_plot(chart_skeleton,
    x = ,
    y = ,
    x_error = None, #If no values, None
    y_error = None, #If no values, None
    color_name = '{}', #{}
    color_brightness = 'default', #{}
    marker_shape = 'o', #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x', '']
    opacity = 1,
    label_for_legend = '',
    layer_order = 1)
    """.format(color_library['properties']['default_color'],
               list(color_library['colors'].keys()),
               list(color_library['properties']['brightness'].keys()))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Plot distribution
def add_distribution_plot(chart_skeleton, data, override_chart_skeleton,
                      distribution_min_max, bin_interval,
                      dist_type,
                      color_name, color_brightness, opacity,
                      label_for_legend, layer_order):

    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')
    # ---- check data types
    if type(data) in [str, int, float, bool]:
        raise TypeError('x is not properly defined. x should be a 1 dimensional array of values.')
    # ---- check data shape and turn into series
    if np.shape(np.shape(data))[0] != 1:
        raise TypeError('data is not properly defined.; it is a {} x {} array. data must be 1-dimensional array.'.format(np.shape(data)[0], np.shape(data)[1]))
    data = pd.Series(data)


    # ---- auto set bins to integers between min and max
    if override_chart_skeleton:
        print('override_chart_skeleton is on.\n'
        'Look at the automatic settings we''ve generated and update your code above with appropriate settings.\n'
        'We highly recommend turning override_chart_skeleton off after updating your code.\n')
        # ---- get the data range
        data_range = np.max(data) - np.min(data)

        # ---- set the bins
        # ---- if the range is big, work it down until it has < 15 bins
        if data_range >= 10:

            # ---- set xlim to data min and max
            plt.xlim(np.floor(np.min(data)), np.ceil(np.max(data)));
            interval = 1
            bins = np.arange(np.floor(np.min(data)), np.ceil(np.max(data))+1, interval)
            while np.shape(bins)[0] >= 15:
                interval += 1
                bins = np.arange(np.floor(np.min(data)), np.ceil(np.max(data))+1, interval)
        # ---- if the range is small, work it up until it has >= 10 bins
        else:
            i = 0
            intervals = [0.5, 0.25, 0.2, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.00001]
            interval = intervals[i]
            decimals = [2,2,2,2,2,3,3,4,4]
            bins = np.arange(np.floor(np.min(data) * 10**decimals[i]) / 10**decimals[i],
                             (np.ceil(np.max(data) * 10**decimals[i]) / 10**decimals[i])+interval,
                             interval)
            while np.shape(bins)[0] < 10:
                i += 1
                interval = intervals[i]
                bins = np.arange(np.floor(np.min(data) * 10**decimals[i]) / 10**decimals[i],
                             (np.ceil(np.max(data) * 10**decimals[i]) / 10**decimals[i])+interval,
                             interval)

            # ---- set xlim to data min and max
            plt.xlim(np.floor(np.min(data) * 10**decimals[i]) / 10**decimals[i],
                             (np.ceil(np.max(data) * 10**decimals[i]) / 10**decimals[i])+interval);

        # ---- set ylim to 0 and max in bin
        binned_data = pd.cut(data, bins=bins).value_counts()
        if dist_type in ['binned_density', 'smooth_density']:
            plt.ylim(0, binned_data.max()/(binned_data.sum()*interval));
        elif dist_type == 'binned_counts':
            plt.ylim(0, np.ceil(binned_data.max()));
        else:
            raise KeyError('dist_type is not properly defined; it must be binned_counts, binned_density, or smooth_density')

        # ---- set the xticks to be on the bin edges
        xticks = bins
        plt.xticks(xticks)
        # ---- if that creates too many ticks, only plot every nth tick
        i = 1
        while chart_skeleton['ax'].get_xticks().shape[0] > 10:
            i += 1
            plt.xticks(xticks[::i])

        # ---- set the yticks to a max of 10 ticks
        chart_skeleton['ax'].yaxis.set_major_locator(plt.MaxNLocator(5))

    # ---- set bins manually if override_chart_skeleton is not on
    elif dist_type in ['binned_density', 'binned_counts']:
        bins = np.arange(distribution_min_max[0], distribution_min_max[1]+bin_interval, bin_interval)

    # ---- check for too many ticks
    if chart_skeleton['ax'].get_xticks().shape[0] > 20:
        raise RuntimeError('quicklook is trying to plot too many xticks; increase the x_tick_interval')
    if chart_skeleton['ax'].get_yticks().shape[0] > 20:
        raise RuntimeError('quicklook is trying to plot too many yticks; increase the y_tick_interval')

    # ---- get colors
    line, fill, edge = define_colors(chart_skeleton, color_name, color_brightness)

    if dist_type == 'smooth_density':
        dist = sns.kdeplot(data, fill=True, linewidth=0, color=fill,
                           clip= chart_skeleton['ax'].get_xlim() if override_chart_skeleton else distribution_min_max,
                           alpha=opacity, ax=chart_skeleton['ax'],
                           zorder=3, label=label_for_legend);

    else:
        # ---- plot distribution
        dist = chart_skeleton['ax'].hist(data, bins=bins, alpha=opacity,
                                  rwidth=0.85, color=fill, density= dist_type == 'binned_density',
                                  linewidth=0, label=label_for_legend,
                                  zorder = 3, joinstyle='round');
    if override_chart_skeleton:
        print('Your build_chart_skeleton settings are automatically being set as:\n'
              '- x_min_max = {}\n'
              '- y_min_max = {} \n'
              '- xtick_interval = {}\n'
              '- ytick_interval = {}\n\n'
              'Your add_distribution_plot settings are automatically being set as:\n'
              '- distribution_min_max = {}\n'
              '- bin_interval = {} \n'.format(chart_skeleton['ax'].get_xlim(),
                                              chart_skeleton['ax'].get_ylim(),
                                              chart_skeleton['ax'].get_xticks()[1]-chart_skeleton['ax'].get_xticks()[0],
                                              chart_skeleton['ax'].get_yticks()[1],
                                              chart_skeleton['ax'].get_xlim(),
                                              interval))
    return {'distribution': dist}

# ---- set doc string
add_distribution_plot.__doc__ = \
    """
    dist = quicklook.add_distribution_plot(chart_skeleton,
    data = ,
    override_chart_skeleton = True,
    distribution_min_max = (None,None),
    bin_interval = None, #If dist_type is smooth_density, None
    dist_type = 'binned_counts', #['binned_counts', 'binned_density', 'smooth_density']
    color_name = '{}', #{}
    color_brightness = 'default', #{}
    opacity = 1,
    label_for_legend = '',
    layer_order = 1)
    """.format(color_library['properties']['default_color'],
               list(color_library['colors'].keys()),
               list(color_library['properties']['brightness'].keys()))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# add reference features
def add_reference_line(chart_skeleton, line_type, location, linewidth, linestyle,
                                color_name, color_brightness, marker_shape,
                                opacity, label_for_legend, layer_order):

    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    line, fill, edge = define_colors(chart_skeleton, color_name, color_brightness)
    markersize, markeredgewidth = define_markersize(chart_skeleton['size'], marker_shape)

    if line_type == 'horizontal':
        x = np.linspace(chart_skeleton['x_min_max'][0],chart_skeleton['x_min_max'][1],10)
        y = np.full(10,location)
    elif line_type == 'vertical':
        x = np.full(10,location)
        y = np.linspace(chart_skeleton['y_min_max'][0],chart_skeleton['y_min_max'][1],10)
    elif line_type == 'diagonal_up':
        x = np.linspace(chart_skeleton['x_min_max'][0],chart_skeleton['x_min_max'][1],10)
        y = np.linspace(chart_skeleton['y_min_max'][0],chart_skeleton['y_min_max'][1],10)
    elif line_type == 'diagonal_down':
        x = np.linspace(chart_skeleton['x_min_max'][0],chart_skeleton['x_min_max'][1],10)
        y = np.linspace(chart_skeleton['y_min_max'][1],chart_skeleton['y_min_max'][0],10)
    else:
        raise Exception('type is not properly defined. type must be defined as horizontal, vertical, diagonal_up, or diagonal_down')

    line = chart_skeleton['ax'].plot(
            x,
            y,
            linewidth = linewidth,
            linestyle = linestyle,
            color = line,
            marker = marker_shape,
            markersize = markersize,
            mec = edge,
            mfc = fill,
            mew = markeredgewidth,
            alpha = opacity,
            label = label_for_legend,
            zorder = layer_order + 2);
    return {'ref_line': line}

# ---- set doc string
add_reference_line.__doc__ = \
    """
    ref_line = quicklook.add_reference_line(chart_skeleton,
    line_type = , #['horizontal','vertical','diagonal_up','diagonal_down']
    location = , #If diagonal_up or diagonal_down, None
    color_name = '{}', #{}
    color_brightness = 'default', #{}
    linewidth = 3,
    linestyle = ':', #['-', '--', ':', '-.']
    marker_shape = 'None', #['None', 'o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
    opacity = 1,
    label_for_legend = '',
    layer_order = 1)
    """.format('text',
               list(color_library['colors'].keys()),
               list(color_library['properties']['brightness'].keys()))


def add_text(chart_skeleton, text, color_name, color_brightness,
             text_location_on_x_axis,
             text_location_on_y_axis, horizontal_align, vertical_align,
             box_around_text, layer_order, font_size='default'):

    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    if font_size == 'default':
        font_size = chart_skeleton['fonts']['size'][1]

    line,_,_ = define_colors(chart_skeleton, color_name, color_brightness)

    if box_around_text:
        text = chart_skeleton['ax'].text(
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
        text = chart_skeleton['ax'].text(
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

# ---- set doc string
add_text.__doc__ = \
    """
    text = quicklook.add_text(chart_skeleton,
    text = '',
    color_name = '{}', #{}
    color_brightness = 'default' #{}
    text_location_on_x_axis = ,
    text_location_on_y_axis = ,
    horizontal_align = 'center', #['center', 'left', 'right']
    vertical_align = 'center', #['center', 'top', 'bottom']
    box_around_text = False,
    layer_order = 1)
    """.format('text',
               list(color_library['colors'].keys()),
               list(color_library['properties']['brightness'].keys()))


def add_legend(chart_skeleton, legend_location, frame_around_legend):
    """
    legend = quicklook.add_legend(chart_skeleton,
    legend_location = 'best', frame_around_legend=False);

    Options
    -------
    legend_location:      ['best', 'upper right', 'upper left', 'lower left',
                           'lower right', 'right', 'center left', 'center right',
                           'lower center', 'upper center', 'center']
    frame_around_legend:  [True, False]
    """
    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    legend = chart_skeleton['ax'].legend(
                        loc = legend_location,
                        prop = chart_skeleton['fonts']['legend'],
                        frameon = frame_around_legend,
                        fancybox = True,
                        facecolor = chart_skeleton['color_library']['properties']['background'],
                        framealpha = 1);

    _, markeredgewidth = define_markersize(chart_skeleton['size'], 'o')
    legend.get_frame().set_linewidth(markeredgewidth)

    for text in legend.get_texts():
        text.set_color(chart_skeleton['color_library']['properties']['text'])

    return {'legend': legend}

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# see colors
def show_color_library(chart_skeleton):
    """
    quicklook.show_color_library(chart_skeleton)
    """
    fig, ax = plt.subplots(nrows=1, figsize = (18,12))

    # hide spines
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_facecolor(chart_skeleton['color_library']['properties']['background'])
    fig.set_facecolor(chart_skeleton['color_library']['properties']['background'])

    ax.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False)
    color_strs = list(chart_skeleton['color_library'].keys())[4:]
    ncols = len(chart_skeleton['color_library'][color_strs[0]])
    x_loc = np.linspace(0.2,0.8,ncols)
    nrows = len(color_strs)
    y_loc = np.linspace(0.9,0.1,nrows)
    for row in range(nrows):
        ax.text(0.85, y_loc[row], color_strs[row],
                    horizontalalignment='left', verticalalignment='center',
                    size = chart_skeleton['fonts']['size'][1], color=chart_skeleton['color_library']['properties']['text'],
                    bbox = dict(facecolor = chart_skeleton['color_library']['properties']['background'], edgecolor = 'none',
                    boxstyle = 'round, pad = 0.5', alpha = 1, linewidth = 0.5, zorder = 1));

        for col in range(ncols):
            ax.add_patch(patch.Ellipse((x_loc[col],y_loc[row]), 0.075, 0.1, color=chart_skeleton['color_library']['colors'][color_strs[row]][col]));

    return

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# save chart
def save_chart_to_computer(chart_skeleton,
                        chart_name,
                        path_to_folder_to_save_chart_in,
                        print_confirmation=True,
                        format='png'):
    """
    quicklook.save_chart_to_computer(chart_skeleton,
                         chart_name = '',
                         path_to_folder_to_save_chart_in = '',
                         print_confirmation=True)
    """

    dpi = {'print': 300, 'full_slide': 72, 'half_slide': 72}
    plt.savefig(os.path.join(path_to_folder_to_save_chart_in, chart_name+'.{}'.format(format)), format=format, dpi=dpi[chart_skeleton['size']]);
    if print_confirmation:
        print('{} saved in the folder: {}'.format(chart_name, path_to_folder_to_save_chart_in));
    return()
