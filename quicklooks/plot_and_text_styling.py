from pathlib import Path
import os
from matplotlib import font_manager # type: ignore
import numpy as np # type: ignore
import warnings
import matplotlib.ticker as ticker # type: ignore
import matplotlib.dates as mdates # type: ignore

# ---- used to find the text width for the y label
# ---- this helps set the distance between the edge of the plot
# ---- and the ylabel
class chart_skeleton_style:
    def __init__(self, chart_size, ylabel):
        def find_text_width(text):
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

        # ---- create style settings for plot padding and ticks
        self.figsize = {
        'notebook': (6*16/9,6),
        'half_slide':(15,15*3/4),
        'full_slide': (30,30/1.94)
        }[chart_size]

        self.label_pad = {
        'notebook': (15,3*find_text_width(ylabel)[1] + 20),
        'half_slide': (15,15),
        'full_slide': (30,3*find_text_width(ylabel)[1] + 70)
        }[chart_size]

        self.title_pad = {'notebook': 30,
                          'half_slide': 35,
                          'full_slide': 35}[chart_size]
        self.linewidth = {'notebook':2,
                          'half_slide': 2,
                          'full_slide': 4}[chart_size]
        self.tick_pad = {'notebook': (5,5),
                         'half_slide': (5, 5),
                         'full_slide': (10, 10)}[chart_size]
        self.tick_length = {'notebook': 6,
                            'half_slide': 6,
                            'full_slide': 10}[chart_size]

class font_style:
    class font_size:
        def __init__(self,chart_size):
            fs = {'notebook': 20,
                  'half_slide': 32,
                  'full_slide': 48}
            self.xl = fs[chart_size]
            self.l = fs[chart_size] - 4
            self.m = fs[chart_size] - 8
            self.s = fs[chart_size] - 12

    def __init__(self,chart_size,chart_skeleton):
        # ---- define fonts
        this_directory = Path(__file__).parent
        font_folder = os.path.join(this_directory,
                        'fonts',
                        chart_skeleton.font)
        # ---- handles font files regardless of .ttf or .otf
        # ---- check for title file
        font_dir = os.listdir(font_folder)

        if not [i for i in os.listdir(font_folder) if 'title' in i]:
            raise FileNotFoundError('''Make sure that the fonts folder \
            contains a title.ttf or title.otf file''')
        else:
            title_path = os.path.join(
                font_folder, font_dir[font_dir.index(
                    [i for i in font_dir if 'title' in i][0])])

        # ---- check for text file
        if not [i for i in os.listdir(font_folder) if 'text' in i]:
            raise FileNotFoundError('Make sure that the fonts folder \
                contains a text.ttf or text.otf file')
        else:
            text_path = os.path.join(font_folder,
                font_dir[font_dir.index(
                    [i for i in font_dir if 'text' in i][0])])

        self.size = self.font_size(chart_size)
        self.title = font_manager.FontProperties(
            fname=title_path, size = self.size.xl)
        self.label = font_manager.FontProperties(
            fname=text_path, size = self.size.l)
        self.legend = font_manager.FontProperties(
            fname=text_path,size = self.size.m)

# ---- define the marker size based on the plot size
def define_markersize(size, marker_shape):
    markersize = {'notebook':7,
                  'half_slide':10,
                  'full_slide':14}[size]
    if marker_shape not in ['', False, 'none', 'None', None, 'na', 'NA', 'n/a']:
        markersize = markersize
        markeredgewidth = {'notebook':2,
                           'half_slide':2,
                           'full_slide':3}[size]
    else:
        markersize = 0
        markeredgewidth = 0
    return markersize, markeredgewidth

def set_tick_labels(labels, axis, axis_object, min_max):
    # ---- don't do anything if default
    if labels == 'default':
        pass
    # ---- handle lists; x/y differentiation baked in
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
    # ---- handle everything else, split by axis
    else:
        labels_need_edit = False
        if axis == 'x':
            if labels == 'percents':
                axis_object.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
            elif labels == 'years':
                axis_object.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
            elif labels == 'quarters':
                axis_object.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
                labels_need_edit = True
            # ---- dont include year if all months in the same year
            elif labels == 'months':
                if min_max[0].year == min_max[1].year:
                    axis_object.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
                # ---- include year if all months goes across two years
                else:
                    axis_object.xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
                    labels_need_edit = True

            elif labels in ['days', 'weeks']:
                axis_object.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))

            else:
                raise TypeError('''xtick_labels not properly defined''')

            # ---- alter the xtick labels for quarters and month/year
            if labels_need_edit:
                pos = [i.get_position()[0] for i in axis_object.get_xticklabels()]
                axis_object.xaxis.set_major_locator(ticker.FixedLocator(pos))
                ao_labels = [i.get_text() for i in axis_object.get_xticklabels()]

                # ---- replace month with name of quarter
                if labels == 'quarters':
                    replacements = {'Jan':'Q1', 'Apr':'Q2', 'Jul':'Q3', 'Oct':'Q4'}
                    new_labels = ['{}\n{}'.format(replacements[l.split(' ')[0]],
                        l.split(' ')[1]) for l in ao_labels]
                # ---- only keep the first year and if month is Jan
                elif labels == 'months':
                    new_labels = [l if l.split('\n')[0] == 'Jan' or \
                        l == ao_labels[0] else l.split('\n')[0] for l in ao_labels]

                axis_object.set_xticklabels(new_labels)

        elif axis == 'y':
            if labels == 'percents':
                axis_object.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
            elif labels in ['1k', '100k', '1m']:
                pos = [i.get_position()[1] for i in axis_object.get_yticklabels()]
                axis_object.yaxis.set_major_locator(ticker.FixedLocator(pos))
                ao_labels = [i.get_text() for i in axis_object.get_yticklabels()]

                text_map = dict(zip(['1k','100k','1m'],[1e3,1e3,1e6]))
                denom = text_map[labels]
                label = labels[-1].upper()

                if labels == '100k':
                    new_labels = ['{:3.0f}{}'.format(
                        i.get_position()[1]/denom,label
                    ) for i in axis_object.get_yticklabels()]
                else:
                    new_labels = ['{:3.1f}{}'.format(
                        i.get_position()[1]/denom,label
                    ) for i in axis_object.get_yticklabels()]

                axis_object.set_yticklabels(new_labels)
