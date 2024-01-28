import matplotlib.pyplot as plt
from .plot_func_internal import define_markersize

class legend:
    """
    legend = quicklook.add_legend(chart_skeleton,
    legend_location = 'best', frame_around_legend=False);

    Options
    -------
    legend_location:      ['best', 'upper right', 'upper left', 'lower left',
                           'lower right', 'right', 'center left', 'center right',
                           'lower center', 'upper center', 'center']
    frame_around_legend:  [True, False]
    """

    def __init__(self, chart_skeleton, legend_location, frame_around_legend):
        if not chart_skeleton.ax:
            raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                            'Run quicklook.build_chart_skeleton to build a chart skeleton.')

        legend = chart_skeleton.ax.legend(
                            loc = legend_location,
                            prop = chart_skeleton['fonts']['legend'],
                            frameon = frame_around_legend,
                            fancybox = True,
                            facecolor = chart_skeleton['color_library']['properties']['background'],
                            framealpha = 1);

        _, markeredgewidth = define_markersize(chart_skeleton['size'], 'o')
        legend.get_frame().set_linewidth(markeredgewidth)

        for text in legend.get_texts():
            text.set_color(chart_skeleton['color_library']['properties']['text'])

        return {'legend': legend}
