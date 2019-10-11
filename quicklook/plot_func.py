import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from .plot_func_internal import find_text_width
from .plot_func_internal import def_fonts


def init_plot(style, size, title, ylabel, xlabel, xlim, ylim, xticks, yticks, ygrid_on, xgrid_on, mid_line_on, perf_corr_line_on, axes_type):
    """fig, ax, c_lib, size, style, fonts = quicklook.init_plot(style = 'dark', size = 'default',
    title = '',
    xlabel = '',
    ylabel = '',
    xlim = (0,1), ylim = (0,1), xticks = 5, yticks = 5,
    ygrid_on = False, xgrid_on = False,
    mid_line_on = False, perf_corr_line_on = False, axes_type = 0);

    style = ['dark', 'light']
    size = ['default', 'small', 'poster', 'poster_small']
    axes_type {0:'1 quadrant (L shaped)', 1:'4 quadrants (+ shaped)'}"""

    # define fonts
    fonts = def_fonts(style, size)

    # define colors
    if style == 'dark':
        c_lib = {'bg':'#292d34',
                 'text':'#abb2bf',
                 'labels':'#292d34',
                 'g':('#44c168','#69e788','#179c49'),
                 'b':('#40addf','#16d8ff','#5384b6'),
                 'y': ('#fee370', '#ffeda3', '#b19b3a'),
                 'p': ('#bd82d0', '#f9b2ff','#8456a3'),
                 'r': ('#f57970', '#ff9f95', '#e84f4e'),
                 'k':('#b4b4b4', '#cfcfcf', '#999999')}

    elif style == 'light':
        c_lib = {'bg':'#fafbfc',
                 'text':'#393b43',
                 'labels':'#393b43',
                 'g':('#179c49', '#b1d9a0', '#0e4f25'),
                 'b':('#5384b6', '#c2e0f5', '#25486a'),
                 'y': ('#fee370', '#ffeda3', '#b19b3a'),
                 'p': ('#8456a3', '#d3b3d5', '#642d90'),
                 'r': ('#e84f4e', '#f58d90', '#9c2625'),
                 'k':('#40403f', '#999999', '#000000')}

    # define preset sizes
    figsize = {'small':(9,6), 'default':(12,8), 'poster':(9,6), 'poster_small':(6,4)}
    label_pad = {'small': (25, 3*find_text_width(ylabel)[1] + 50),
                 'default': (35,3*find_text_width(ylabel)[1] + 70),
                 'poster': (40,3*find_text_width(ylabel)[1] + 50),
                 'poster_small': (30,3*find_text_width(ylabel)[1] + 40)}
    title_pad = {'small': 25, 'default': 35, 'poster':0, 'poster_small':0}
    linewidth = {'small': 1.5, 'default': 2, 'poster':3, 'poster_small':2}
    tick_pad = {'small': (2.5, 10), 'default': (5, 15), 'poster':(10, 10), 'poster_small':(10,10)}
    tick_length = {'small': 5, 'default': 10, 'poster':7.5,'poster_small':5}

    fig, ax = plt.subplots(nrows=1, figsize = figsize[size])
    ax.tick_params('x', colors=c_lib['text'], labelsize=fonts['size'][1], width = linewidth[size], pad = tick_pad[size][0], length = tick_length[size])
    ax.tick_params('y', colors=c_lib['text'], labelsize=fonts['size'][1], width = linewidth[size], pad = tick_pad[size][1], length = tick_length[size])

    if size == 'poster_small':
        ax.patch.set_xy((-0.3, -0.2))
        ax.patch.set_height(1.3)
        ax.patch.set_width(1.4)
    elif size == 'poster':
        ax.patch.set_xy((-0.16, -0.115))
        ax.patch.set_height(1.15)
        ax.patch.set_width(1.21)
    else:
        ax.patch.set_xy((-0.16, -0.14))
        ax.patch.set_height(1.2)
        ax.patch.set_width(1.28)

    ax.set_facecolor(c_lib['bg'])

    # Labels -----------------------------------------------------------------------------------------------------------------
    # y axis label
    ax.set_ylabel(ylabel,
                   color=c_lib['labels'], rotation = 0, labelpad = label_pad[size][1], horizontalalignment = 'center',
                   linespacing = 1.6, fontproperties = fonts['label'])
    # x axis label
    ax.set_xlabel(xlabel,
                   color = c_lib['labels'], labelpad = label_pad[size][0], fontproperties = fonts['label'])

    # title
    ax.set_title(title,
                  color = c_lib['labels'], pad = title_pad[size], fontproperties = fonts['title'])
    # ------------------------------------------------------------------------------------------------------------------------
    # Axes set up ------------------------------------------------------------------------------------------------------------
    ax.set_ylim(ylim)
    ax.yaxis.set_major_locator(plt.MaxNLocator(yticks))

    ax.set_xlim(xlim)
    ax.xaxis.set_major_locator(plt.MaxNLocator(xticks))

    # hide spines
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # change the spine width
    if axes_type == 0:
        ax.axhline(y = ylim[0] ,linewidth=linewidth[size], color = c_lib['text'], zorder = 0.1)
        ax.axvline(x = xlim[0], linewidth=linewidth[size], color = c_lib['text'], zorder = 0.1)
    elif axes_type == 1:
        ax.axhline(y = np.mean(ylim) ,linewidth=linewidth[size], color = c_lib['text'], zorder = 0.1)
        ax.axvline(x = np.mean(xlim), linewidth=linewidth[size], color = c_lib['text'], zorder = 0.1)
    # ------------------------------------------------------------------------------------------------------------------------
    # Context Lines ----------------------------------------------------------------------------------------------------------
    # Grid
    if ygrid_on == True:
        ax.yaxis.grid(which='major', linestyle='-', linewidth = '0.3', color = '0.5')

    if xgrid_on == True:
        ax.xaxis.grid(which='major', linestyle='-', linewidth = '0.3', color = '0.5')

    ax.set_axisbelow(True)

    # Chance
    if mid_line_on == True:
        ax.plot(np.linspace(start=xlim[0], stop=xlim[1], num=5), np.full(fill_value=np.mean(ylim), shape=5), c= c_lib['text'], linestyle = ':', label = 'Chance', zorder = 0.2)

    # Shows perfect correlation across blocks
    if perf_corr_line_on == True:
        ax.plot(np.linspace(xlim[0],xlim[1],10), np.linspace(ylim[0],ylim[1],10), c = c_lib['text'], linestyle = ':', label = 'Correlation = 1', zorder = 0.2)

    plt.tight_layout()
    return(fig, ax, c_lib, size, style, fonts)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Plot lines

def plot_line(ax, c_lib, size, x, y, linewidth, color_str, marker_on, marker_shape, label, zorder):
    """
    line = quicklook.plot_line(ax, c_lib, size,
    x = ,
    y = ,
    linewidth = 3,
    color_str = '',
    marker_on = True,
    marker_shape = 'o',
    label = '',
    zorder = 1)
    """

    markersize = {'small':8, 'default':10, 'poster':10, 'poster_small':8}

    if marker_on == True:
        markersize = markersize[size]
    else:
        markersize = 0

    #light style
    if c_lib['bg'] == '#fafbfc':
        fill = 0
        edge = 2
    #dark style
    elif c_lib['bg'] == '#292d34':
        fill = 0
        edge = 1


    line = ax.plot(
            x,
            y,
            linewidth = linewidth,
            color = c_lib[color_str][0],
            marker = marker_shape,
            markersize = markersize,
            mec = c_lib[color_str][edge],
            mfc = c_lib[color_str][fill],
            mew = 2,
            label = label,
            zorder = zorder);
    return(line)


def plot_err_line(ax, c_lib, size, x, y_mean, y_err, linewidth, color_str, marker_on, marker_shape, label, zorder):
    """
    mean, ub, lb, fill = quicklook.plot_err_line(ax, c_lib, size,
    x = ,
    y_mean = ,
    y_err = ,
    linewidth = 3,
    color_str = '',
    marker_on = True,
    marker_shape = 'o',
    label = '',
    zorder = 1)
    """

    markersize = {'small':8, 'default':10, 'poster':10, 'poster_small':8}

    if marker_on == True:
        markersize = markersize[size]
    else:
        markersize = 0

    #light style
    if c_lib['bg'] == '#fafbfc':
        fill = 1
        edge = 2
    #dark style
    elif c_lib['bg'] == '#292d34':
        fill = 2
        edge = 1

    fill = ax.fill_between(
                          x,
                          y_mean - y_err,
                          y_mean + y_err,
                          color = c_lib[color_str][fill],
                          label = None,
                          alpha = 0.2,
                          zorder = zorder);
    mean = ax.plot(
                x,
                y_mean,
                linewidth = linewidth,
                color = c_lib[color_str][0],
                marker = marker_shape,
                markersize = markersize,
                label = label,
                zorder = zorder);
    ub = ax.plot(
                x,
                y_mean + y_err,
                linewidth = 0.5,
                color = c_lib[color_str][edge],
                label = None,
                zorder = zorder);
    lb = ax.plot(
                x,
                y_mean - y_err,
                linewidth = 0.5,
                color = c_lib[color_str][edge],
                label = None,
                zorder = zorder);
    return(mean, ub, lb, fill)


def plot_vert_line(ax, c_lib, x, ylim, width, style, color, label, zorder):
    """
    vert_line = quicklook.vert_line(ax, c_lib,
    x = ,
    ylim = (,),
    width = 3,
    style = '--',
    color = c_lib[''][0],
    label = '',
    zorder = 1)
    """
    vert_line = ax.plot(np.full(100,x), np.linspace(ylim[0],ylim[1],100), linestyle = style, linewidth = width, label = label, color = color, zorder = zorder)
    return(vert_line)


def plot_hor_line(ax, c_lib, y, xlim, width, style, color, label, zorder):
    """
    hor_line = quicklook.hor_line(ax, c_lib,
    y = ,
    xlim = (,),
    width = 3,
    style = '--',
    color = c_lib[''][0],
    label = '',
    zorder = 1)
    """
    hor_line = ax.plot(np.linspace(xlim[0],xlim[1],100), np.full(100,y), linestyle = style, linewidth = width, label = label, color = color, zorder = zorder)
    return(hor_line)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Plot scatter
def plot_scatter(ax, c_lib, size, x, y, color_str, zorder, label):
    """
    scatter = quicklook.plot_scatter(ax, c_lib, size,
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
    if c_lib['bg'] == '#fafbfc':
        fill = 0
        edge = 2
    #dark style
    elif c_lib['bg'] == '#292d34':
        fill = 0
        edge = 1

    scatter = ax.scatter(x = x, y = y, color = c_lib[color_str][fill], edgecolor = c_lib[color_str][edge],
               s = markersize, label = label, zorder = zorder, linewidths=edge_width);
    return(scatter)


def plot_err_scatter(ax, c_lib, x, y, xerr, yerr, color_str, zorder, label):
    """
    scatter, err_fill, err_outline = quicklook.plot_err_scatter(ax, c_lib,
    x = ,
    y = ,
    xerr = ,
    yerr = ,
    color_str = ,
    zorder = 1,
    label = '')
    """
    #light style
    if c_lib['bg'] == '#fafbfc':
        fill = 1
    #dark style
    elif c_lib['bg'] == '#292d34':
        fill = 2

    scatter = ax.scatter(x = x, y = y, color = c_lib[color_str][3-fill], label = label, zorder = zorder+1);

    for pt in range(len(x)):
        err_fill = ax.add_patch(patch.Ellipse((x.iloc[pt],y.iloc[pt]), xerr.iloc[pt] * 2, yerr.iloc[pt] * 2,
                                                facecolor = c_lib[color_str][fill], alpha = .8, zorder = zorder))
        err_outline = ax.add_patch(patch.Ellipse((x.iloc[pt],y.iloc[pt]), xerr.iloc[pt] * 2, yerr.iloc[pt] * 2,
                                                    facecolor = 'none', edgecolor = c_lib[color_str][0], alpha = 0.3, linewidth = 2, zorder = zorder))
    return(scatter, err_fill, err_outline)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Other

def add_text(ax, c_lib, fonts, frame_on, text, x_loc, y_loc, hor_align, vert_align, zorder):
    """
    text = quicklook.add_text(ax, c_lib, fonts,
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
                        size = fonts['size'][1], color=c_lib['text'],
                        bbox = dict(facecolor = c_lib['bg'], edgecolor = c_lib['text'],
                        boxstyle = 'round, pad = 0.5', alpha = 1, linewidth = 0.5, zorder = zorder));
    else:
        text = ax.text(x_loc, y_loc, text,
                        horizontalalignment=hor_align, verticalalignment=vert_align,
                        size = fonts['size'][1], color=c_lib['text']);

    return(text)


def add_legend(ax, c_lib, size, fonts, frame_on, loc, bbox_coord, markerscale, markercolor_str_set):
    """
    legend = quicklook.add_legend(ax, c_lib, size, fonts,
    frame_on=False, loc = 'best', bbox_coord = (1,1),
    markerscale = 1, markercolor_str_set = []);
    """
    legend = ax.legend(loc=loc, bbox_to_anchor = bbox_coord, prop = fonts['label'],
                       frameon = frame_on, fancybox = True, shadow = True,
                       markerscale = markerscale, facecolor = c_lib['bg']);

    for text in legend.get_texts():
        text.set_color(c_lib['text'])

    # check if I've entered a list of strs for colors
    if not markercolor_str_set:
        markercolor_set = [c_lib[i][0] for i in markercolor_str_set]

        for idx in range(len(markercolor_str_set)):
            legend.legendHandles[-len(markercolor_set)+idx].set_color(markercolor_set[idx])
    return(legend)


def show_c_lib(c_lib, fonts):
    """
    quicklook.show_c_lib(c_lib, fonts)
    """
    fig, ax = plt.subplots(nrows=1, figsize = (6,12))

    # hide spines
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_facecolor(c_lib['bg'])
    fig.set_facecolor(c_lib['bg'])

    ax.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False)
    color_strs = list(c_lib.keys())[3:]
    nrows = len(color_strs)
    y_loc = np.linspace(0.9,0.1,nrows)
    for i in range(nrows):
        ax.add_patch(patch.Ellipse((0.2,y_loc[i]),0.4, 0.2, color=c_lib[color_strs[i]][0]));
        ax.add_patch(patch.Ellipse((0.5,y_loc[i]),0.4, 0.2, color=c_lib[color_strs[i]][1]));
        ax.add_patch(patch.Ellipse((0.8,y_loc[i]),0.4, 0.2, color=c_lib[color_strs[i]][2]));
        ax.text(1, y_loc[i], color_strs[i],
                    horizontalalignment='left', verticalalignment='center',
                    size = fonts['size'][1], color=c_lib['text'],
                    bbox = dict(facecolor = c_lib['bg'], edgecolor = 'none',
                    boxstyle = 'round, pad = 0.5', alpha = 1, linewidth = 0.5, zorder = 1));
    return()
