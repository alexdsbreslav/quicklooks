from pathlib import Path
import os
from matplotlib import font_manager
import numpy as np
import warnings
import matplotlib.ticker as ticker

# ---- used to find the text width for the y label
# ---- this helps set the distance between the edge of the plot
# ---- and the ylabel
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


# ---- define the fonts
def define_plot_style(size, ylabel, font_file):
    """
    Only used internally
    """
    # ---- define fonts
    fontsize = {'print': (12,10,9), 'half_slide': (26,20,18), 'full_slide': (40,34,32)}
    font_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
    # ---- handles font files regardless of .ttf or .otf
    # ---- check for title file
    if font_file == 'default':
        font_dir = os.listdir(font_folder)

        if not [i for i in os.listdir(font_folder) if 'title' in i]:
            raise FileNotFoundError('Make sure that the fonts folder contains a title.ttf or title.otf file')
        else:
            title_path = os.path.join(font_folder, font_dir[font_dir.index([i for i in font_dir if 'title' in i][0])])

        # ---- check for text file
        if not [i for i in os.listdir(font_folder) if 'text' in i]:
            raise FileNotFoundError('Make sure that the fonts folder contains a text.ttf or text.otf file')
        else:
            text_path = os.path.join(font_folder, font_dir[font_dir.index([i for i in font_dir if 'text' in i][0])])

    # ---- if we add and define a different tmp font
    else:
        title_path = os.path.join(font_folder, 'fonts', font_file)
        text_path = os.path.join(font_folder, 'fonts', font_file)

    fonts = {'title':font_manager.FontProperties(fname=title_path, size = fontsize[size][0]),
             'label':font_manager.FontProperties(fname=text_path, size = fontsize[size][1]),
             'legend':font_manager.FontProperties(fname=text_path, size = fontsize[size][2]),
             'size':fontsize[size]}

    # ---- create style settings for plot padding and ticks
    figsize = {'print': (6,4),
               'half_slide':(13,8.6666667),
               'full_slide': (23,15)}[size]
    label_pad = {'print': (5, 3*find_text_width(ylabel)[1] + 30),
                 'half_slide': (35,3*find_text_width(ylabel)[1] + 70),
                 'full_slide': (45,3*find_text_width(ylabel)[1] + 90)}[size]
    title_pad = {'print': 15, 'half_slide': 35, 'full_slide': 45}[size]
    linewidth = {'print': 1, 'half_slide': 2, 'full_slide': 3}[size]
    tick_pad = {'print': (3, 3), 'half_slide': (5, 15), 'full_slide': (7.5, 20)}[size]
    tick_length = {'print': 2.5, 'half_slide': 10, 'full_slide': 12.5}[size]

    return figsize, label_pad, title_pad, linewidth, tick_pad, tick_length, fonts


# ---- define the marker size based on the plot size
def define_markersize(size, marker_shape):
    markersize = {'print':6, 'half_slide':10, 'full_slide':14}[size]
    if marker_shape not in ['', False, 'none', 'None', None, 'na', 'NA', 'n/a']:
        markersize = markersize
        markeredgewidth = {'print':0.75, 'half_slide':2, 'full_slide':3}[size]
    else:
        markersize = 0
        markeredgewidth = 0
    return markersize, markeredgewidth

def set_tick_labels(labels, axis, axis_object, min_max):
    if labels == 'default':
        pass
    elif labels == 'percents':
        if axis == 'x':
            axis_object.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=min_max[1]))
        elif axis == 'y':
            axis_object.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=min_max[1]))
    elif type(labels) is list:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')

            # ---- get label positions and determine which are displayed
            if axis == 'x':
                label_position = [i.get_position()[0] for i in axis_object.get_xticklabels()]
            elif axis == 'y':
                label_position = [i.get_position()[1] for i in axis_object.get_yticklabels()]
            displayed_labels = label_position[1:-1]

            # ---- check length of list of xtick_labels
            if len(labels) != len(displayed_labels):
                raise Exception('Expected {} new {}_labels; {} are defined.'.format(len(displayed_labels), axis, len(labels)))
            # ---- create a new list of labels
            new_labels = [None] + [i for i in labels] + [None]
            # ---- update with new labels
            if axis == 'x':
                axis_object.set_xticklabels(new_labels)
            elif axis == 'y':
                axis_object.set_yticklabels(new_labels)
