from pathlib import Path
import os
from matplotlib import font_manager
import numpy as np


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
    file_path = os.path.dirname(__file__)
    font_root = str(Path(file_path))
    title_path = font_root + '/fonts/Futura.ttc'
    text_path = font_root + '/fonts/SourceSansPro-Regular.ttf'

    fonts = {'title':font_manager.FontProperties(fname=title_path, size = fontsize[size][0]),
             'label':font_manager.FontProperties(fname=text_path, size = fontsize[size][1]),
             'size':fontsize[size]}
    return(fonts)
