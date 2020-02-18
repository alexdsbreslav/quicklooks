from pathlib import Path
import os
from matplotlib import font_manager
import numpy as np

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
def define_plot_style(style, size, ylabel):
    """
    Only used internally
    """
    # ---- define fonts
    fontsize = {'small': (24,18), 'default': (26,20)}
    font_folder = os.path.abspath('fonts')
    title_path = os.path.join(font_folder, 'Futura.ttc')
    text_path = os.path.join(font_folder, 'SourceSansPro-Regular.ttf')

    fonts = {'title':font_manager.FontProperties(fname=title_path, size = fontsize[size][0]),
             'label':font_manager.FontProperties(fname=text_path, size = fontsize[size][1]),
             'size':fontsize[size]}

    # ---- create style settings for plot padding and ticks
    figsize = {'small':(9,6), 'default':(12,8)}[size]
    label_pad = {'small': (25, 3*find_text_width(ylabel)[1] + 50),
                 'default': (35,3*find_text_width(ylabel)[1] + 70)}[size]
    title_pad = {'small': 25, 'default': 35}[size]
    linewidth = {'small': 1.5, 'default': 2}[size]
    tick_pad = {'small': (2.5, 10), 'default': (5, 15)}[size]
    tick_length = {'small': 5, 'default': 10}[size]

    # ---- define the color library
    if style == 'default':
        color_library = {'name': 'default',
                         'background': '#ffffff',
                         'text': '#000000',
                         'labels': '#000000',
                         'gray': ['#f8f9fa','#f1f3f5','#e9ecef','#dee2e6','#ced4da','#adb5bd','#868e96','#495057','#343a40','#212529'],
                         'red': ['#fff5f5','#ffe3e3','#ffc9c9','#ffa8a8','#ff8787','#ff6b6b','#fa5252','#f03e3e','#e03131','#c92a2a'],
                         'pink': ['#fff0f6','#ffdeeb','#fcc2d7','#faa2c1','#f783ac','#f06595','#e64980','#d6336c','#c2255c','#a61e4d'],
                         'grape': ['#f8f0fc','#f3d9fa','#eebefa','#e599f7','#da77f2','#cc5de8','#be4bdb','#ae3ec9','#9c36b5','#862e9c'],
                         'violet': ['#f3f0ff','#e5dbff','#d0bfff','#b197fc','#9775fa','#845ef7','#7950f2','#7048e8','#6741d9','#5f3dc4'],
                         'indigo': ['#edf2ff','#dbe4ff','#bac8ff','#91a7ff','#748ffc','#5c7cfa','#4c6ef5','#4263eb','#3b5bdb','#364fc7'],
                         'blue': ['#e7f5ff','#d0ebff','#a5d8ff','#74c0fc','#4dabf7','#339af0','#228be6','#1c7ed6','#1971c2','#1864ab'],
                         'cyan': ['#e3fafc','#c5f6fa','#99e9f2','#66d9e8','#3bc9db','#22b8cf','#15aabf','#1098ad','#0c8599','#0b7285'],
                         'teal': ['#e6fcf5','#c3fae8','#96f2d7','#63e6be','#38d9a9','#20c997','#12b886','#0ca678','#099268','#087f5b'],
                         'green': ['#ebfbee','#d3f9d8','#b2f2bb','#8ce99a','#69db7c','#51cf66','#40c057','#37b24d','#2f9e44','#2b8a3e'],
                         'lime': ['#f4fce3','#e9fac8','#d8f5a2','#c0eb75','#a9e34b','#94d82d','#82c91e','#74b816','#66a80f','#5c940d'],
                         'yellow': ['#fff9db','#fff3bf','#ffec99','#ffe066','#ffd43b','#fcc419','#fab005','#f59f00','#f08c00','#e67700'],
                         'orange': ['#fff4e6','#ffe8cc','#ffd8a8','#ffc078','#ffa94d','#ff922b','#fd7e14','#f76707','#e8590c','#d9480f']}

    elif style == 'simple_dark':
        # ---- created by alex breslav using https://learnui.design/tools/data-color-picker.html
        color_library = {'name': 'simple_dark',
                        'background':'#292d34',
                        'text':'#abb2bf',
                        'labels':'#292d34',
                        'green':('#69e788', '#44c168', '#179c49'),
                        'blue':('#16d8ff', '#40addf','#5384b6'),
                        'yellow': ('#ffeda3', '#fee370', '#b19b3a'),
                        'purple': ('#f9b2ff', '#bd82d0', '#8456a3'),
                        'red': ('#ff9f95', '#f57970', '#e84f4e'),
                        'gray':('#cfcfcf', '#b4b4b4', '#999999')}

    elif style == 'simple_light':
        # ---- created by alex breslav using https://learnui.design/tools/data-color-picker.html
        color_library = {'name': 'simple_light',
                        'background':'#fafbfc',
                        'text':'#393b43',
                        'labels':'#393b43',
                        'green':('#b1d9a0', '#179c49', '#0e4f25'),
                        'blue':('#c2e0f5', '#5384b6', '#25486a'),
                        'yellow': ('#ffeda3', '#fee370', '#b19b3a'),
                        'purple': ('#d3b3d5', '#8456a3', '#642d90'),
                        'red': ('#f58d90', '#e84f4e', '#9c2625'),
                        'gray':('#999999', '#40403f', '#000000')}

    return figsize, label_pad, title_pad, linewidth, tick_pad, tick_length, color_library, fonts

# ---- define the colors based on the style
def define_line_colors(color_library, color_string, color_brightness):
    # ---- check to make sure that the colors were entered properly
    if color_string not in list(color_library.keys())[4:]:
        raise Exception('Color entered is not in the color library. Enter one of the follow colors:\n''{}'\
                        .format([i for i in list(color_library.keys())[4:]]))
    if color_brightness not in ['default', 'light', 'dark']:
        raise Exception('Color brightness is not properly define. color_brightness must be set to default, light, or dark')
    else:
        pass

    # ---- define the colors based on the palette
    if color_library['name'] == 'simple_dark':
        fill = 1
        edge = 0
        line = 1
    elif color_library['name'] == 'simple_light':
        fill = 1
        edge = 2
        line = 1
    elif color_library['name'] == 'default':
        if color_brightness == 'default':
            line = 4
            fill = 4
            edge = 6
        elif color_brightness == 'light':
            line = 1
            fill = 1
            edge = 3
        else:
            line = 7
            fill = 7
            edge = 9
    return line, fill, edge


# ---- define the marker size based on the plot size
def define_markersize(size, marker_shape):
    markersize = {'small':8, 'default':10}[size]
    if marker_shape not in ['', False, 'none', 'None', None, 'na', 'NA', 'n/a']:
        markersize = markersize
    else:
        markersize = 0
    return markersize
