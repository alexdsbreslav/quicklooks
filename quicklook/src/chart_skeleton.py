import matplotlib.pyplot as plt
from .plot_func_internal import *
from .cs_attributes import *

class chart_skeleton:
    """
    chart_skeleton = ql.chart_skeleton(
    size = ql.chart_size.half_slide,
    color_library = ql.color_libraries.mariglow,
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

    def __init__(self, size, color_library, title, ylabel, xlabel, x_min_max,
                 y_min_max, xtick_interval, ytick_interval, xtick_labels,
                 ytick_labels, horizontal_gridlines_on, vertical_gridlines_on):

        # ---- size
        # ---- affects markersize for line and scatter plots
        self.size = size

        # ---- colors
        self.color_library = color_library

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

        # ---- x_min_max
        # ---- req for reference_line
        if type(x_min_max) is tuple and x_min_max[1] > x_min_max[0]:
            self.x_min_max = x_min_max
        else:
            raise AttributeError('x_min_max must be a tuple (e.g., (0,1) \
                                  where the second value is greater than \
                                  the first')

        # ---- y_min_max
        # ---- req for reference_line
        if type(y_min_max) is tuple and y_min_max[1] > y_min_max[0]:
            self.y_min_max = y_min_max
        else:
            raise AttributeError('y_min_max must be a tuple (e.g., (0,1) where\
                                  the second value is greater than the first')

        # ---- xtick_labels
        if type(xtick_labels) not in [str, list]:
            raise Exception('xtick_labels not properly defined: xtick_labels \
                             must be set to default, percents, or defined \
                             as a list of strings.')
        elif type(xtick_labels) is str and xtick_labels not in ['default', 'percents']:
            raise Exception('xtick_labels not properly defined: xtick_labels \
                             must be set to default, percents, or defined \
                             as a list of strings.')

        # ---- ytick_labels
        if type(ytick_labels) not in [str, list]:
            raise Exception('ytick_labels not properly defined: ytick_labels \
                             must be set to default, percents, or defined as a \
                             list of strings.')
        elif type(ytick_labels) is str and ytick_labels not in ['default', 'percents']:
            raise Exception('ytick_labels not properly defined: ytick_labels \
                             must be set to default, percents, or defined as a \
                             list of strings.')

        # ---- xtick_interval
        if xtick_interval > x_min_max[1] - x_min_max[0]:
            raise AttributeError('xtick_interval is not properly defined: \
                                  xtick_interval must be greater than \
                                  x_max minus x_min.')
        elif (x_min_max[1]-x_min_max[0])/xtick_interval > 50:
            raise RuntimeError('quicklook is trying to plot too many xticks; \
                                increase the xtick_interval')

        # ---- ytick_interval
        if ytick_interval > y_min_max[1] - y_min_max[0]:
            raise AttributeError('ytick_interval is not properly defined: \
                                  ytick_interval must be greater than \
                                  y_max minus y_min.')
        elif (y_min_max[1]-y_min_max[0])/ytick_interval > 50:
            raise RuntimeError('quicklook is trying to plot too many yticks; \
                                increase the ytick_interval')

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
        ps = plot_style(size, ylabel)

        # ---- req for legend and text
        self.plot_style = ps

        # ---- create the plot
        fig, ax = plt.subplots(nrows=1, figsize = ps.figsize)
        self.ax = ax

        # ---- add the title
        ax.set_title(title, color = color_library.text,
                     pad = ps.title_pad, fontproperties = ps.fonts.title)

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
            tick.set_font_properties(ps.fonts.label)
        for tick in ax.get_yticklabels():
            tick.set_font_properties(ps.fonts.label)

        # ---- set the axis limits and number of ticks
        ax.set_ylim(y_min_max)
        ax.set_xlim(x_min_max)

        # ---- set the number of ticks on the axes
        ax.yaxis.set_major_locator(plt.MultipleLocator(ytick_interval))
        ax.xaxis.set_major_locator(plt.MultipleLocator(xtick_interval))

        # ---- label the y axis
        ax.set_ylabel(ylabel, color=color_library.text,
                      rotation = 0, labelpad = ps.label_pad[1],
                      horizontalalignment = 'center',
                      linespacing = 1.6, fontproperties = ps.fonts.label)

        # ---- label the x axis
        ax.set_xlabel(xlabel, color = color_library.text,
                      labelpad = ps.label_pad[0], fontproperties = ps.fonts.label)

        # ---- set the x and y tick labels
        set_tick_labels(xtick_labels, 'x', ax, x_min_max)
        set_tick_labels(ytick_labels, 'y', ax, y_min_max)

        plt.tight_layout()
