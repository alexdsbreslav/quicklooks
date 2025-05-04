import matplotlib.pyplot as plt
from .plot_and_text_styling import define_markersize

class legend:
    """
    legend = ql.legend(chart_skeleton,
    legend_location = ql.legend.loc.best, frame=False);
    """

    class loc:
        best = 'best'
        up_right = 'upper right'
        up_left = 'upper left'
        low_left = 'lower left'
        low_right = 'lower right'
        right = 'right'
        center_left = 'center left'
        center_right = 'center right'
        low_center = 'lower center'
        up_center = 'upper center'
        center = 'center'

    def __init__(self, chart_skeleton, legend_location, frame):
        if not chart_skeleton.ax:
            raise Exception('''The chart skeleton has not been built. \
            You must build a chart skeleton for each new plot that \
            you want to create.''')

        legend = chart_skeleton.ax.legend(
                            loc = legend_location,
                            prop = chart_skeleton.font_style.legend,
                            frameon = frame,
                            fancybox = True,
                            facecolor = chart_skeleton.color_library.background,
                            framealpha = 1);

        # ---- set the text color
        for text in legend.get_texts():
            text.set_color(chart_skeleton.color_library.text)

        if frame:
            # ---- set the edgewidth on the frame
            legend.get_frame().set_linewidth(1)

            # ---- set the edge color of the frame
            legend.get_frame().set_edgecolor('0.8')

        self.legend_obj = legend
