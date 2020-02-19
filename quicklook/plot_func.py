import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from .add_func_internal import define_add_style, find_text_width, \
                                define_line_colors, define_markersize


def build_chart_skeleton(style, size, title, ylabel, xlabel, x_min_max,
                         y_min_max, xtick_interval, ytick_interval,
                         horizontal_gridlines_on, vertical_gridlines_on):

    """chart_skeleton = quicklook.build_chart_skeleton(style = 'default', size = 'default',
    title = '',
    xlabel = '',
    ylabel = '',
    x_min_max = (0,1), y_min_max = (0,1),
    xtick_interval = 1, ytick_interval = 1,
    horizontal_gridlines_on = False,
    vertical_gridlines_on = False);

    Options
    -------
    style = ['default', 'simple_dark', 'simple_light']
    size = ['default', 'small']"""

    # ---- raise exceptions if things are not properly defined
    if size not in ['small', 'default']:
        raise Exception('Size not properly defind: size must be set to default or small')

    if style not in ['default', 'simple_dark', 'simple_light']:
        raise Exception('Style not properly defined: \
        style must be set to default, simple_dark, or simple_light.')

    if vertical_gridlines_on not in [True, False]:
        raise Exception('Vertical gridlines is not properly defined: \
        vertical_gridlines_on must be set to True or False')

    if horizontal_gridlines_on not in [True, False]:
        raise Exception('Horizontal gridlines is not properly defined: \
        horizontal_gridlines_on must be set to True or False')

    # ---- define plot style based on style and size choice
    figsize, label_pad, title_pad, linewidth, \
    tick_pad, tick_length, color_library, \
    fonts = define_add_style(style, size, ylabel)

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
        linewidth = '0.3', color = '0.5', zorder = 0)

    if vertical_gridlines_on == True:
        ax.xaxis.grid(which='major', linestyle='-',
        linewidth = '0.3', color = '0.5', zorder = 0)

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
              label_for_legend, layer_order):
    """
    quicklook.add_line_to_chart(chart_skeleton,
    x = ,
    y = ,
    color_name = '',
    color_brightness = 'default',
    linewidth = 3,
    linestyle = '-',
    marker_shape = 'o',
    label_for_legend = '',
    layer_order = 1)

    Options
    -------
    color_name: options depend on the style. Run quicklook.show_color_library(color_library, fonts)
    color_brightness = ['light', 'default', 'dark'] (only works for default color library)
    marker_shape = ['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x'] or ''
    linestyle = ['-', '--', ':', '-.']
    """
    if not chart_skeleton['ax']:
        raise Exception('Plot has not been initalized. Make sure to run quicklook.initialize_plot() first.')

    line, fill, edge = define_line_colors(chart_skeleton['color_library'], color_name, color_brightness)
    markersize = define_markersize(chart_skeleton['size'], marker_shape)

    line = chart_skeleton['ax'].plot(
            x,
            y,
            linewidth = linewidth,
            linestyle = linestyle,
            color = chart_skeleton['color_library'][color_name][line],
            marker = marker_shape,
            markersize = markersize,
            mec = chart_skeleton['color_library'][color_name][edge],
            mfc = chart_skeleton['color_library'][color_name][fill],
            mew = 2,
            label = label_for_legend,
            zorder = layer_order);
    return


def add_line_with_error_to_chart(chart_skeleton, x, y_mean, y_error, linewidth,
                         linestyle, color_name, color_brightness, marker_shape,
                         label_for_legend, layer_order):
    """
    quicklook.add_line_with_error_to_chart(ax, color_library, size,
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
    color_name: options depend on the style. Run quicklook.show_color_library(color_library, fonts)
    color_brightness = ['light', 'default', 'dark'] (only works for default color library)
    marker_shape = ['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
    linestyle = ['-', '--', ':', '-.']
    """

    if not chart_skeleton['ax']:
        raise Exception('Plot has not been initalized. Make sure to run quicklook.initialize_plot() first.')

    line, fill, edge = define_line_colors(chart_skeleton['color_library'], color_name, color_brightness)
    markersize = define_markersize(chart_skeleton['size'], marker_shape)

    fill = chart_skeleton['ax'].fill_between(
                          x,
                          y_mean - y_error,
                          y_mean + y_error,
                          color = chart_skeleton['color_library'][color_name][fill],
                          label = None,
                          alpha = 0.2,
                          zorder = layer_order);
    mean = chart_skeleton['ax'].plot(
                x,
                y_mean,
                linewidth = linewidth,
                linestyle = linestyle,
                color = chart_skeleton['color_library'][color_name][line],
                marker = marker_shape,
                markersize = markersize,
                label = label_for_legend,
                zorder = layer_order);
    ub = chart_skeleton['ax'].plot(
                x,
                y_mean + y_error,
                linewidth = 0.5,
                color = chart_skeleton['color_library'][color_name][edge],
                label = None,
                zorder = layer_order);
    lb = chart_skeleton['ax'].plot(
                x,
                y_mean - y_error,
                linewidth = 0.5,
                color = chart_skeleton['color_library'][color_name][edge],
                label = None,
                zorder = layer_order);
    return


def add_vertical_line_to_chart(chart_skeleton, x, linewidth, linestyle,
                       color_name, color_brightness, marker_shape,
                       label_for_legend, layer_order):
    """
    quicklook.add_vertical_line_to_chart(chart_skeleton,
    x = ,
    color_name = '',
    color_brightness = 'default',
    linewidth = 3,
    linestyle = '-',
    marker_shape = 'None',
    label_for_legend = '',
    layer_order = 1)

    Options
    -------
    color_name: options depend on the style. Run quicklook.show_color_library(color_library, fonts)
    color_brightness = ['light', 'default', 'dark'] (only works for default color library)
    marker_shape = ['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x'] or ''
    linestyle = ['-', '--', ':', '-.']
    """
    if not chart_skeleton['ax']:
        raise Exception('Plot has not been initalized. Make sure to run quicklook.initialize_plot() first.')

    line, fill, edge = define_line_colors(chart_skeleton['color_library'], color_name, color_brightness)
    markersize = define_markersize(chart_skeleton['size'], marker_shape)

    line = chart_skeleton['ax'].plot(
            np.full(100,x),
            np.linspace(chart_skeleton['y_min_max'][0],chart_skeleton['y_min_max'][1],100),
            linewidth = linewidth,
            linestyle = linestyle,
            color = chart_skeleton['color_library'][color_name][line],
            marker = marker_shape,
            markersize = markersize,
            mec = chart_skeleton['color_library'][color_name][edge],
            mfc = chart_skeleton['color_library'][color_name][fill],
            mew = 2,
            label = label_for_legend,
            zorder = layer_order);
    return


def add_horizontal_line_to_chart(chart_skeleton, y, linewidth, linestyle,
                         color_name, color_brightness, marker_shape,
                         label_for_legend, layer_order):
    """
    quicklook.add_vertical_line_to_chart(ax, color_library, size,
    y = ,
    color_name = '',
    color_brightness = 'default',
    linewidth = 3,
    linestyle = '-',
    marker_shape = 'None',
    label_for_legend = '',
    layer_order = 1)

    Options
    -------
    color_name: options depend on the style. Run quicklook.show_color_library(color_library, fonts)
    color_brightness = ['light', 'default', 'dark'] (only works for default color library)
    marker_shape = ['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x'] or ''
    linestyle = ['-', '--', ':', '-.']
    """
    if not chart_skeleton['ax']:
        raise Exception('Plot has not been initalized. Make sure to run quicklook.initialize_plot() first.')

    line, fill, edge = define_line_colors(chart_skeleton['color_library'], color_name, color_brightness)
    markersize = define_markersize(chart_skeleton['size'], marker_shape)

    line = chart_skeleton['ax'].plot(
            np.linspace(chart_skeleton['x_min_max'][0],chart_skeleton['x_min_max'][1],100),
            np.full(100,y),
            linewidth = linewidth,
            linestyle = linestyle,
            color = chart_skeleton['color_library'][color_name][line],
            marker = marker_shape,
            markersize = markersize,
            mec = chart_skeleton['color_library'][color_name][edge],
            mfc = chart_skeleton['color_library'][color_name][fill],
            mew = 2,
            label = label_for_legend,
            zorder = layer_order);
    return

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Plot scatter
def add_scatter(ax, color_library, size, x, y, color_str, zorder, label):
    """
    quicklook.add_scatter(ax, color_library, size,
    x = ,
    y = ,
    color_str = ,
    zorder = 1,
    label = '')
    """

    # size of scatter points and edge width
    if type(size) is str:
        markersize = {'small':50, 'default':120, 'poster':50, 'poster_small':30}
        edge_width = {'small':1, 'default':2, 'poster':3, 'poster_small':2}

        markersize = markersize[size]
        edge_width = edge_width[size]
    else:
        markersize = size
        edge_width = 1

    #light style
    if color_library['background'] == '#fafbfc':
        fill = 0
        edge = 2
    #dark style
    elif color_library['background'] == '#292d34':
        fill = 0
        edge = 1

    scatter = ax.scatter(x = x, y = y, color = color_library[color_str][fill], edgecolor = color_library[color_str][edge],
               s = markersize, label = label, zorder = zorder, linewidths=edge_width);
    return(scatter)


def add_err_scatter(ax, color_library, x, y, xerr, yerr, color_str, zorder, label):
    """
    quicklook.add_err_scatter(ax, color_library,
    x = ,
    y = ,
    xerr = ,
    yerr = ,
    color_str = ,
    zorder = 1,
    label = '')
    """
    #light style
    if color_library['background'] == '#fafbfc':
        fill = 1
    #dark style
    elif color_library['background'] == '#292d34':
        fill = 2

    scatter = ax.scatter(x = x, y = y, color = color_library[color_str][3-fill], label = label, zorder = zorder+1);

    for pt in range(len(x)):
        err_fill = ax.add_patch(patch.Ellipse((x.iloc[pt],y.iloc[pt]), xerr.iloc[pt] * 2, yerr.iloc[pt] * 2,
                                                facecolor = color_library[color_str][fill], alpha = .8, zorder = zorder))
        err_outline = ax.add_patch(patch.Ellipse((x.iloc[pt],y.iloc[pt]), xerr.iloc[pt] * 2, yerr.iloc[pt] * 2,
                                                    facecolor = 'none', edgecolor = color_library[color_str][0], alpha = 0.3, linewidth = 2, zorder = zorder))
    return(scatter, err_fill, err_outline)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Other

def add_text(ax, color_library, fonts, frame_on, text, x_loc, y_loc, hor_align, vert_align, zorder):
    """
    quicklook.add_text(ax, color_library, fonts,
    frame_on = True,
    text = '',
    x_loc = ,
    y_loc = ,
    hor_align = 'center',
    vert_align = 'center',
    zorder = 1)
    """

    if frame_on == True:
        text = ax.text(x_loc, y_loc, text,
                        horizontalalignment=hor_align, verticalalignment=vert_align,
                        size = fonts['size'][1], color=color_library['text'],
                        bbox = dict(facecolor = color_library['background'], edgecolor = color_library['text'],
                        boxstyle = 'round, pad = 0.5', alpha = 1, linewidth = 0.5, zorder = zorder));
    else:
        text = ax.text(x_loc, y_loc, text,
                        horizontalalignment=hor_align, verticalalignment=vert_align,
                        size = fonts['size'][1], color=color_library['text']);

    return(text)


def add_legend(ax, color_library, size, fonts, frame_on, loc, bbox_coord, markerscale, markercolor_str_set):
    """
    quicklook.add_legend(ax, color_library, size, fonts,
    frame_on=False, loc = 'best', bbox_coord = (1,1),
    markerscale = 1, markercolor_str_set = []);
    """
    legend = ax.legend(loc=loc, bbox_to_anchor = bbox_coord, prop = fonts['label'],
                       frameon = frame_on, fancybox = True, shadow = True,
                       markerscale = markerscale, facecolor = color_library['background']);

    for text in legend.get_texts():
        text.set_color(color_library['text'])

    # check if I've entered a list of strs for colors
    if not markercolor_str_set:
        markercolor_set = [color_library[i][0] for i in markercolor_str_set]

        for idx in range(len(markercolor_str_set)):
            legend.legendHandles[-len(markercolor_set)+idx].set_color(markercolor_set[idx])
    return(legend)


def show_color_library(color_library, fonts):
    """
    quicklook.show_color_library(color_library, fonts)
    """
    fig, ax = plt.subplots(nrows=1, figsize = (6,12))

    # hide spines
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_facecolor(color_library['background'])
    fig.set_facecolor(color_library['background'])

    ax.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False)
    color_strs = list(color_library.keys())[3:]
    nrows = len(color_strs)
    y_loc = np.linspace(0.9,0.1,nrows)
    for i in range(nrows):
        ax.add_patch(patch.Ellipse((0.2,y_loc[i]),0.4, 0.2, color=color_library[color_strs[i]][0]));
        ax.add_patch(patch.Ellipse((0.5,y_loc[i]),0.4, 0.2, color=color_library[color_strs[i]][1]));
        ax.add_patch(patch.Ellipse((0.8,y_loc[i]),0.4, 0.2, color=color_library[color_strs[i]][2]));
        ax.text(1, y_loc[i], color_strs[i],
                    horizontalalignment='left', verticalalignment='center',
                    size = fonts['size'][1], color=color_library['text'],
                    bbox = dict(facecolor = color_library['background'], edgecolor = 'none',
                    boxstyle = 'round, pad = 0.5', alpha = 1, linewidth = 0.5, zorder = 1));
    return()