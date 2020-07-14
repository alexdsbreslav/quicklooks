import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from .plot_func_internal import *


def build_chart_skeleton(style, size, title, ylabel, xlabel, x_min_max,
                         y_min_max, xtick_interval, ytick_interval,
                         horizontal_gridlines_on, vertical_gridlines_on):

    """chart_skeleton = quicklook.build_chart_skeleton(style = 'default', size = 'default',
    title = '',
    xlabel = '',
    ylabel = '',
    x_min_max = (0,1), y_min_max = (0,1),
    xtick_interval = 0.25, ytick_interval = 0.25,
    horizontal_gridlines_on = False,
    vertical_gridlines_on = False);

    Options
    -------
    Title, xlabel, ylabel       Add text to describe your plot. Leave as '' to leave out labels.
    style:                      ['default', 'simple_dark', 'simple_light']
    size:                       ['default', 'small']
    horizontal_gridlines_on:    [True, False]
    vertical_gridlines_on:      [True, False]
    """

    # ---- raise exceptions if things are not properly defined
    if size not in ['small', 'default']:
        raise Exception('Size not properly defind: size must be set to default or small.')

    if style not in ['default', 'simple_dark', 'simple_light']:
        raise Exception('Style not properly defined: '
                        'style must be set to default, simple_dark, or simple_light.')

    if vertical_gridlines_on not in [True, False]:
        raise Exception('Vertical gridlines is not properly defined: '
                        'vertical_gridlines_on must be set to True or False.')

    if horizontal_gridlines_on not in [True, False]:
        raise Exception('Horizontal gridlines is not properly defined: '
                        'horizontal_gridlines_on must be set to True or False.')

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

    # ---- define plot style based on style and size choice
    figsize, label_pad, title_pad, linewidth, \
    tick_pad, tick_length, color_library, \
    fonts = define_plot_style(style, size, ylabel)

    # ---- create the plot
    fig, ax = plt.subplots(nrows=1, figsize = figsize)

    # ---- add the title
    ax.set_title(title, color = color_library['labels'],
                 pad = title_pad, fontproperties = fonts['title'])

    # ---- create a patch to set the background color of the plot
    ax.patch.set_xy((-0.16, -0.14))
    ax.patch.set_height(1.2)
    ax.patch.set_width(1.28)
    ax.set_facecolor(color_library['background'])

    # ---- style the axis lines
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_linewidth(linewidth)
        ax.spines[spine].set_color(color_library['text'])
        ax.spines[spine].set_zorder(0)

    # ---- style the axis ticks
    ax.tick_params('x', colors=color_library['text'], labelsize=fonts['size'][1],
                   width = linewidth, pad = tick_pad[0], length = tick_length)

    ax.tick_params('y', colors=color_library['text'], labelsize=fonts['size'][1],
                   width = linewidth, pad = tick_pad[1], length = tick_length)

    # ---- set the axis limits and number of ticks
    ax.set_ylim(y_min_max)
    ax.set_xlim(x_min_max)

    # ---- set the number of ticks on the axes
    ax.yaxis.set_major_locator(plt.MultipleLocator(ytick_interval))
    ax.xaxis.set_major_locator(plt.MultipleLocator(xtick_interval))

    # ---- label the y axis
    ax.set_ylabel(ylabel, color=color_library['labels'],
                  rotation = 0, labelpad = label_pad[1],
                  horizontalalignment = 'center',
                  linespacing = 1.6, fontproperties = fonts['label'])

    # ---- label the x axis
    ax.set_xlabel(xlabel, color = color_library['labels'],
                  labelpad = label_pad[0], fontproperties = fonts['label'])

    # ---- add grid lines if necessary
    if horizontal_gridlines_on == True:
        ax.yaxis.grid(which='major', linestyle='-',
        linewidth = '0.3', color = '0.5')

    if vertical_gridlines_on == True:
        ax.xaxis.grid(which='major', linestyle='-',
        linewidth = '0.3', color = '0.5')

    ax.set_axisbelow(True)
    plt.tight_layout()
    chart_skeleton = {'fig': fig, 'ax': ax, 'color_library': color_library,
                      'size': size, 'fonts': fonts, 'x_min_max': x_min_max,
                      'y_min_max': y_min_max}

    return chart_skeleton

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Plot lines

def add_line_to_chart(chart_skeleton, x, y, linewidth, linestyle,
              color_name, color_brightness, marker_shape,
              opacity, label_for_legend, layer_order):
    """
    quicklook.add_line_to_chart(chart_skeleton,
    x = ,
    y = ,
    color_name = '',
    color_brightness = 'default',
    linewidth = 3,
    linestyle = '-',
    marker_shape = 'o',
    opacity = 1,
    label_for_legend = '',
    layer_order = 1)

    Options
    -------
    color_name:         Options depend on the style.
                        Run quicklook.show_color_library(chart_skeleton)
    color_brightness:   ['light', 'default', 'dark'] (only works for default color library)
    marker_shape:       ['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x'] or ''
    linestyle:          ['-', '--', ':', '-.']
    """
    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    line, fill, edge = define_colors(chart_skeleton, color_name, color_brightness)
    markersize = define_markersize(chart_skeleton['size'], marker_shape)

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
            mew = 2,
            alpha = opacity,
            label = label_for_legend,
            zorder = layer_order);
    return


def add_line_with_error_to_chart(chart_skeleton, x, y_mean, y_error, linewidth,
                         linestyle, color_name, color_brightness, marker_shape,
                         label_for_legend, layer_order):
    """
    quicklook.add_line_with_error_to_chart(chart_skeleton,
    x = ,
    y_mean = ,
    y_error = ,
    color_name = '',
    color_brightness = 'default',
    linewidth = 3,
    linestyle = '-',
    marker_shape = 'o',
    label_for_legend = '',
    layer_order = 1)

    Options
    -------
    color_name:         Options depend on the style.
                        Run quicklook.show_color_library(chart_skeleton)
    color_brightness:   ['light', 'default', 'dark'] (only works for default color library)
    marker_shape:       ['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
    linestyle:          ['-', '--', ':', '-.']
    """

    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    line, fill, edge = define_colors(chart_skeleton, color_name, color_brightness)
    markersize = define_markersize(chart_skeleton['size'], marker_shape)

    fill = chart_skeleton['ax'].fill_between(
                          x,
                          y_mean - y_error,
                          y_mean + y_error,
                          color = fill,
                          label = None,
                          alpha = 0.2,
                          zorder = layer_order);
    mean = chart_skeleton['ax'].plot(
                x,
                y_mean,
                linewidth = linewidth,
                linestyle = linestyle,
                color = line,
                marker = marker_shape,
                markersize = markersize,
                label = label_for_legend,
                zorder = layer_order);
    ub = chart_skeleton['ax'].plot(
                x,
                y_mean + y_error,
                linewidth = 0.5,
                color = edge,
                label = None,
                zorder = layer_order);
    lb = chart_skeleton['ax'].plot(
                x,
                y_mean - y_error,
                linewidth = 0.5,
                color = edge,
                label = None,
                zorder = layer_order);
    return


def add_vertical_line_to_chart(chart_skeleton, x, linewidth, linestyle,
                       color_name, color_brightness, marker_shape,
                       opacity, label_for_legend, layer_order):
    """
    quicklook.add_vertical_line_to_chart(chart_skeleton,
    x = ,
    color_name = '',
    color_brightness = 'default',
    linewidth = 3,
    linestyle = '-',
    marker_shape = 'None',
    opacity = 1,
    label_for_legend = '',
    layer_order = 1)

    Options
    -------
    color_name:         Options depend on the style.
                        Run quicklook.show_color_library(chart_skeleton)
    color_brightness:   ['light', 'default', 'dark'] (only works for default color library)
    marker_shape:       ['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x'] or ''
    linestyle:          ['-', '--', ':', '-.']
    """
    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    line, fill, edge = define_colors(chart_skeleton, color_name, color_brightness)
    markersize = define_markersize(chart_skeleton['size'], marker_shape)

    line = chart_skeleton['ax'].plot(
            np.full(100,x),
            np.linspace(chart_skeleton['y_min_max'][0],chart_skeleton['y_min_max'][1],100),
            linewidth = linewidth,
            linestyle = linestyle,
            color = line,
            marker = marker_shape,
            markersize = markersize,
            mec = edge,
            mfc = fill,
            mew = 2,
            alpha = opacity,
            label = label_for_legend,
            zorder = layer_order);
    return


def add_horizontal_line_to_chart(chart_skeleton, y, linewidth, linestyle,
                         color_name, color_brightness, marker_shape,
                         opacity, label_for_legend, layer_order):
    """
    quicklook.add_vertical_line_to_chart(chart_skeleton,
    y = ,
    color_name = '',
    color_brightness = 'default',
    linewidth = 3,
    linestyle = '-',
    marker_shape = 'None',
    opacity = 1,
    label_for_legend = '',
    layer_order = 1)

    Options
    -------
    color_name:         Options depend on the style.
                        Run quicklook.show_color_library(chart_skeleton)
    color_brightness:   ['light', 'default', 'dark'] (only works for default color library)
    marker_shape:       ['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x'] or ''
    linestyle:          ['-', '--', ':', '-.']
    """
    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    line, fill, edge = define_colors(chart_skeleton, color_name, color_brightness)
    markersize = define_markersize(chart_skeleton['size'], marker_shape)

    line = chart_skeleton['ax'].plot(
            np.linspace(chart_skeleton['x_min_max'][0],chart_skeleton['x_min_max'][1],100),
            np.full(100,y),
            linewidth = linewidth,
            linestyle = linestyle,
            color = line,
            marker = marker_shape,
            markersize = markersize,
            mec = edge,
            mfc = fill,
            mew = 2,
            alpha = opacity,
            label = label_for_legend,
            zorder = layer_order);
    return

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Plot scatter
def add_scatter_to_chart(chart_skeleton, x, y,
              color_name, color_brightness, marker_shape,
              opacity, label_for_legend, layer_order):
    """
    quicklook.add_scatter_to_chart(chart_skeleton,
    x = ,
    y = ,
    color_name = '',
    color_brightness = 'default',
    marker_shape = 'o',
    opacity = 1,
    label_for_legend = '',
    layer_order = 1)

    Options
    -------
    color_name:         Options depend on the style.
                        Run quicklook.show_color_library(chart_skeleton)
    color_brightness:   ['light', 'default', 'dark'] (only works for default color library)
    marker_shape:       ['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x'] or ''
    """
    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    line, fill, edge = define_colors(chart_skeleton, color_name, color_brightness)
    markersize = define_markersize(chart_skeleton['size'], marker_shape)

    scatter = chart_skeleton['ax'].plot(
            x,
            y,
            linewidth = 0,
            color = line,
            marker = marker_shape,
            markersize = markersize,
            mec = edge,
            mfc = fill,
            mew = 2,
            alpha = opacity,
            label = label_for_legend,
            zorder = layer_order);
    return


def add_scatter_with_error_to_chart(chart_skeleton, x, y, x_error, y_error,
              color_name, color_brightness, marker_shape,
              label_for_legend, layer_order):
    """
    quicklook.add_scatter_with_error_to_chart(chart_skeleton,
    x = ,
    y = ,
    x_error = ,
    y_error = ,
    color_name = '',
    color_brightness = 'default',
    marker_shape = 'o',
    label_for_legend = '',
    layer_order = 1)

    Options
    -------
    color_name:         Options depend on the style.
                        Run quicklook.show_color_library(chart_skeleton)
    color_brightness:   ['light', 'default', 'dark'] (only works for default color library)
    marker_shape:       ['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x'] or ''
    """
    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    shape = [np.shape(i) for i in [x,y,x_error,y_error]]
    if not shape[0] == shape[1] == shape[2] == shape[3]:
        raise Exception('x, y, x_error, and y_error are not the same length. All four inputs must have the same number of items in them.')

    if not shape[0]:
        x = [x]
        y = [y]
        x_error = [x_error]
        y_error = [y_error]

    line, fill, edge = define_colors(chart_skeleton, color_name, color_brightness)
    markersize = define_markersize(chart_skeleton['size'], marker_shape)

    scatter = chart_skeleton['ax'].plot(
            x,
            y,
            linewidth = 0,
            color = line,
            marker = marker_shape,
            markersize = markersize,
            mec = edge,
            mfc = fill,
            mew = 2,
            label = label_for_legend,
            zorder = layer_order+0.5);

    coord = tuple(zip(x,y))
    err = tuple(zip(x_error,y_error))

    for pt in range(len(coord)):
        err_fill = chart_skeleton['ax'].add_patch(patch.Ellipse((coord[pt][0],coord[pt][1]), err[pt][0] * 2, err[pt][1] * 2,
                                                facecolor = fill, alpha = .8, zorder = layer_order))
        err_outline = chart_skeleton['ax'].add_patch(patch.Ellipse((coord[pt][0],coord[pt][1]), err[pt][0] * 2, err[pt][1] * 2,
                                                facecolor = 'none', edgecolor = edge, alpha = 0.3, linewidth = 2, zorder = layer_order))

    return

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Other

def add_text(chart_skeleton, text, text_color, text_location_on_x_axis,
             text_location_on_y_axis, horizontal_align, vertical_align,
             box_around_text, layer_order):
    """
    quicklook.add_text(chart_skeleton,
    text = '',
    text_color = 'default',
    text_location_on_x_axis = ,
    text_location_on_y_axis = ,
    horizontal_align = 'center',
    vertical_align = 'center',
    box_around_text = True,
    layer_order = 1)

    Options
    -------
    text_color:         Defaults to same color as text in the plot.
                        You can swap out 'default' with another color
                        Color options depend on the style.
                        Run quicklook.show_color_library(chart_skeleton)
    horizontal_align:   ['center', 'left', 'right']
    vertical_align:     ['center', 'top', 'bottom']
    frame_around_text:  [True, False],
    """

    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    if text_color == 'default':
        text_color = chart_skeleton['color_library']['text']
    else:
        text_color, _, _ = define_colors(chart_skeleton, color_name, color_brightness)
        del _

    if box_around_text:
        text = chart_skeleton['ax'].text(
                text_location_on_x_axis,
                text_location_on_y_axis,
                text,
                horizontalalignment=horizontal_align,
                verticalalignment=vertical_align,
                size = chart_skeleton['fonts']['size'][1],
                color = text_color,
                bbox = dict(facecolor = chart_skeleton['color_library']['background'],
                edgecolor = chart_skeleton['color_library']['text'],
                boxstyle = 'round, pad = 0.5',
                alpha = 1,
                linewidth = 0.5,
                zorder = layer_order));
    else:
        text = chart_skeleton['ax'].text(
                text_location_on_x_axis,
                text_location_on_y_axis,
                text,
                horizontalalignment = horizontal_align,
                verticalalignment = vertical_align,
                size = chart_skeleton['fonts']['size'][1],
                color = text_color,
                zorder = layer_order);

    return


def add_legend(chart_skeleton, legend_location, frame_around_legend,
                size_of_marker_in_legend):
    """
    quicklook.add_legend(chart_skeleton,
    legend_location = 'best', frame_around_legend=False,
    size_of_marker_in_legend = 1);
    """
    if not chart_skeleton['ax']:
        raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                        'Run quicklook.build_chart_skeleton to build a chart skeleton.')

    legend = chart_skeleton['ax'].legend(
                        loc = legend_location,
                        prop = chart_skeleton['fonts']['label'],
                        frameon = frame_around_legend,
                        fancybox = True,
                        markerscale = size_of_marker_in_legend,
                        facecolor = chart_skeleton['color_library']['background'],
                        framealpha = 1);
    for text in legend.get_texts():
        text.set_color(chart_skeleton['color_library']['text'])
    return


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

    ax.set_facecolor(chart_skeleton['color_library']['background'])
    fig.set_facecolor(chart_skeleton['color_library']['background'])

    ax.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False)
    color_strs = list(chart_skeleton['color_library'].keys())[4:]
    ncols = len(chart_skeleton['color_library'][color_strs[0]])
    x_loc = np.linspace(0.2,0.8,ncols)
    nrows = len(color_strs)
    y_loc = np.linspace(0.9,0.1,nrows)
    for row in range(nrows):
        ax.text(0.85, y_loc[row], color_strs[row],
                    horizontalalignment='left', verticalalignment='center',
                    size = chart_skeleton['fonts']['size'][1], color=chart_skeleton['color_library']['text'],
                    bbox = dict(facecolor = chart_skeleton['color_library']['background'], edgecolor = 'none',
                    boxstyle = 'round, pad = 0.5', alpha = 1, linewidth = 0.5, zorder = 1));

        for col in range(ncols):
            ax.add_patch(patch.Ellipse((x_loc[col],y_loc[row]), 0.075, 0.1, color=chart_skeleton['color_library'][color_strs[row]][col]));

    return
