import matplotlib.pyplot as plt
from .plot_and_text_styling import *
from .cs_attributes import *
from datetime import datetime
from dateutil import relativedelta
import matplotlib.dates as mdates
import pandas as pd

class chart_skeleton:
    """
    chart_skeleton = ql.chart_skeleton(
    size = ql.chart_size.notebook,
    color_library = ql.color_libraries.opencolor,
    font = ql.fonts.rubik,
    title = '',
    xlabel = '',
    ylabel = '',
    x_min_max = (0,1), y_min_max = (0,1),
    xtick_interval = 0.25, ytick_interval = 0.25,
    xtick_labels = ql.chart_xlabel.default,
    ytick_labels = ql.chart_ylabel.default,
    horizontal_gridlines_on = False,
    vertical_gridlines_on = False);
    """

    def __init__(self, size, color_library, font, title, ylabel, xlabel, x_min_max,
                 y_min_max, xtick_interval, ytick_interval, xtick_labels,
                 ytick_labels, horizontal_gridlines_on, vertical_gridlines_on):

        # ---- size
        # ---- affects markersize for line and scatter plots
        self.size = size

        # ---- colors
        self.color_library = color_library

        # ---- font
        self.font = font

        # ---- title
        if type(title) is not str:
            raise AttributeError('title not properly define: must be a string \
                                 (e.g., Daily Active Users)')

        # ---- ylabel
        if type(ylabel) is not str:
            raise AttributeError('ylabel not properly define: must be a string \
                                 (e.g., "Daily Active Users")')

        # ---- xlabel
        if type(xlabel) is not str:
            raise AttributeError('xlabel not properly define: must be a string \
                                 (e.g., "Date")')

        # ---- y_min_max
        # ---- req for reference_line
        if type(y_min_max) is tuple and y_min_max[1] > y_min_max[0]:
            self.y_min_max = y_min_max
            yrange = y_min_max[1] - y_min_max[0]
            self.yrange = yrange

        else:
            raise AttributeError('y_min_max must be a tuple (e.g., (0,1) where\
                                  the second value is greater than the first')

        # ---- xtick_labels
        if type(xtick_labels) not in [str, list]:
            raise Exception('xtick_labels not properly defined: xtick_labels \
                             must be set to default, percents, or defined \
                             as a list of strings.')

        # ---- set xaxis_type (will overwrite if timeseries)
        xaxis_type = 'default'

        # ---- check that label type and min_max match
        if xtick_labels in ['years', 'months', 'weeks', 'quarters', 'days']:
            for i in range(2):
                if type(x_min_max[i]) is str:
                    x_min_max[i] = datetime.strptime(x_min_max[i], '%Y-%m-%d')
                elif type(x_min_max[i]) in (datetime.date, pd._libs.tslibs.timestamps.Timestamp, datetime):
                    pass
                else:
                    raise TypeError('''If xtick label is set to a timeseries,
                    x_min_max must be a tuple with date strings in the format
                    YYYY-MM-DD or datetime objects''')

            xaxis_type = 'timeseries'

        # ---- req for reference line
        self.xaxis_type = xaxis_type

        # ---- ytick_labels
        if type(ytick_labels) not in [str, list]:
            raise Exception('''ytick_labels not properly defined: ytick_labels
                             must be set to default, percents, or defined as a
                             list of strings.''')

        # ---- check xtick labels
        # ---- for timeseries
        def_error = False
        int_error = False

        if xaxis_type == 'timeseries':
            xrange = (x_min_max[1] - x_min_max[0]).days
            rd = relativedelta.relativedelta(x_min_max[1], x_min_max[0])

            if xtick_labels in ['days', 'weeks', 'years']:
                def_error = True if xtick_interval > xrange else False
                int_error = True if 20*xtick_interval < xrange else False

            elif xtick_labels == 'months':
                if 2 > rd.years * 12 + rd.months:
                    raise Exception('''xtick_interval not properly defined.
                    Use days or weeks if the date range <= 3 months''')
                elif 15 < rd.years * 12 + rd.months:
                    raise Exception('''xtick_interval not properly defined.
                    Use quarters if the date range > 15 months''')

            elif xtick_labels == 'quarters':
                if 9 > rd.years * 12 + rd.months:
                    raise Exception('''xtick_interval not properly defined.
                    Use months if the date range <= 9 months''')
                elif 48 < rd.years * 12 + rd.months:
                    raise Exception('''xtick_interval not properly defined.
                    Use quarters if the date range > 16 quarters''')

        # ---- for everything else
        else:
            xrange = x_min_max[1] - x_min_max[0]
            def_error = True if xtick_interval > xrange else False
            int_error = True if 20*xtick_interval < xrange else False

        if def_error:
            raise Exception('''xtick_interval not properly defined.
            Decrease the xtick_interval or change the xtick_labels''')
        if int_error:
            raise Exception('''xtick_interval is too small.
            Increase the xtick_interval or change the xtick_labels''')


        self.x_min_max = x_min_max
        # ---- req for reference line
        self.xrange = xrange

        # ---- check ytick_labels
        if ytick_interval > yrange:
            raise Exception('''ytick_interval not properly defined;
            decrease the ytick_interval''')

        elif 20*ytick_interval < yrange:
            raise Exception('''ytick_interval is too small;
            increase the ytick_interval.''')

        # ---- vertical gridlines
        if type(vertical_gridlines_on) is not bool:
            raise AttributeError('Vertical gridlines is not properly defined: \
                                  vertical_gridlines_on must be set to \
                                  True or False.')

        # ---- horizontal gridlines
        if type(horizontal_gridlines_on) is not bool:
            raise AttributeError('Horizontal gridlines is not properly defined: \
                                  horizontal_gridlines_on must be set to \
                                  True or False.')

        # ----------------------------------------------------------------------
        # style the plot -------------------------------------------------------
        # ----------------------------------------------------------------------
        # ---- define plot style based on style and size choice
        ps = chart_skeleton_style(size, ylabel)
        fs = font_style(size, self)

        # ---- req for legend and text
        self.plot_style = ps
        self.font_style = fs

        # ---- create the plot
        fig, ax = plt.subplots(nrows=1, figsize = ps.figsize)
        self.ax = ax

        # ---- add the title
        ax.set_title(title, color = color_library.text,
                     pad = ps.title_pad, fontproperties = fs.title)

        # ---- create a patch to set the background color of the plot
        ax.patch.set_xy((-0.16, -0.14))
        ax.patch.set_height(1.2)
        ax.patch.set_width(1.28)
        ax.set_facecolor(color_library.background)

        # ---- set facecolor of fig (around ax face)
        fig.set_facecolor(color_library.background)

        # ---- add grid lines if necessary
        if horizontal_gridlines_on == True:
            ax.yaxis.grid(which='major', linestyle=':',
            linewidth = ps.linewidth, color = '0.8', zorder=1)

        if vertical_gridlines_on == True:
            ax.xaxis.grid(which='major', linestyle=':',
            linewidth = ps.linewidth, color = '0.8', zorder=1)

        # ---- style the axis lines
        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)
        for spine in ['bottom', 'left']:
            ax.spines[spine].set_linewidth(ps.linewidth)
            ax.spines[spine].set_color(color_library.text)
            ax.spines[spine].set_zorder(2)

        # ---- style the axis ticks
        for i in range(2):
            ax.tick_params(['x','y'][i],
                           colors=color_library.text,
                           width = ps.linewidth, pad = ps.tick_pad[i],
                           length = ps.tick_length)

        for tick in ax.get_xticklabels():
            tick.set_font_properties(fs.label)
        for tick in ax.get_yticklabels():
            tick.set_font_properties(fs.label)

        # ---- set the axis limits and number of ticks
        ax.set_ylim(y_min_max)
        ax.set_xlim(x_min_max)

        # ---- set the number of ticks on the axes
        ax.yaxis.set_major_locator(plt.MultipleLocator(ytick_interval))
        if xaxis_type == 'default':
            ax.xaxis.set_major_locator(plt.MultipleLocator(xtick_interval))
        else:
            if xtick_labels == 'years':
                ax.xaxis.set_major_locator(mdates.YearLocator(base=1))
                print('xtick_interval ignored when xtick_label = years\n')
            elif xtick_labels == 'quarters':
                ax.xaxis.set_major_locator(mdates.MonthLocator((1,4,7,10)))
                print('xtick_interval ignored when xtick_label = quarters\n')
            elif xtick_labels == 'months':
                ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
                print('xtick_interval ignored when xtick_label = months\n')
            elif xtick_labels == 'weeks':
                ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0, interval=xtick_interval))
            elif xtick_labels == 'days':
                ax.xaxis.set_major_locator(mdates.DayLocator(interval=xtick_interval))

        # ---- label the y axis
        ax.set_ylabel(ylabel, color=color_library.text,
                      rotation = 90 if size == 'half_slide' else 0, labelpad = ps.label_pad[1],
                      horizontalalignment = 'center',
                      linespacing = 1.6, fontproperties = fs.label)

        # ---- label the x axis
        ax.set_xlabel(xlabel, color = color_library.text,
                      labelpad = ps.label_pad[0], fontproperties = fs.label)

        # ---- set the x and y tick labels
        set_tick_labels(xtick_labels, 'x', ax, x_min_max)
        set_tick_labels(ytick_labels, 'y', ax, y_min_max)

        plt.tight_layout()
