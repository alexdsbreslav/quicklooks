import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from matplotlib import font_manager

def init_plot(style, size, title, ylabel, xlabel, xlim, ylim, xticks, yticks, ygrid_on, xgrid_on, mid_line_on, perf_corr_line_on, axes_type):
    """fig, ax, c_lib, size, style, fonts = init_plot(style = 'dark', size = 'default',
    title = '',
    xlabel = '',
    ylabel = '',
    xlim = (), ylim = (), xticks = , yticks = ,
    ygrid_on = False, xgrid_on = False,
    mid_line_on = False, perf_corr_line_on = False, axes_type = 0);"""

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



def find_text_width(text):
    """
    Only used internally
    """
    idx_list = [0]
    idx = 0
    linebreak_idx = 0
    while linebreak_idx != -1:
        linebreak_idx = text[idx:].find('\n')
        if linebreak_idx != -1:
            linebreak_idx = linebreak_idx + idx
            idx_list.append(linebreak_idx)
            idx = linebreak_idx + 1
    if len(idx_list) == 1:
        breaks = 0
        return(breaks, len(text))
    elif len(idx_list) == 2:
        breaks = 1
        return(breaks, np.max([idx_list[1], len(text[idx_list[1]+2:])]))
    else:
        breaks = len(idx_list) - 1
        return(breaks, np.max([idx_list[1]] + \
                     [len(text[idx_list[i]+2:idx_list[i+1]]) for i in range(1,len(idx_list)-2)] + \
                     [len(text[idx_list[-1]+2:])]))


def def_fonts(style, size):
    """
    Only used internally
    """
    fontsize = {'small': (24,18), 'default': (26,20), 'poster':(20,20), 'poster_small':(20,20)}

    # define fonts
    # title_path = './fonts/SourceSansPro-Black.ttf'
    title_path = './fonts/Futura.ttc'
    text_path = './fonts/SourceSansPro-Regular.ttf'

    fonts = {'title':font_manager.FontProperties(fname=title_path, size = fontsize[size][0]),
             'label':font_manager.FontProperties(fname=text_path, size = fontsize[size][1]),
             'size':fontsize[size]}
    return(fonts)
