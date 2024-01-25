'''
This is a copy/paste/fill in the blank kind of library. Find the function that you want below, copy it (with the ?),
paste it into your notebook, then copy the function's docstring, paste it into your notebook, fille in the blanks
(or change the defaults) and you're all set!

Start with initializing the plot. Then add anything using quicklook, matplotlib, or seaborn by adding code below quicklook.init_plot().

FUNCTIONS:
quicklook.init_plot?                       | initialize a plot that you'll put stuff onto
quicklook.plot_line?                       | line plot
quicklook.plot_err_line?                   | line plot with err
quicklook.plot_vert_line?                  | vertical line
quicklook.plot_hor_line?                   | horizontal line
quicklook.plot_scatter?                    | scatter plot
quicklook.plot_err_scatter?                | scatter plot with x & y error
quicklook.add_text?                        | add text to plot
quicklook.add_legend?                      | add legend to plot
quicklook.show_c_lib(c_lib, fonts)         | show the colors and color names
'''

from .src.chart_skeleton import chart_skeleton
from .src.add_plots import bar_plot
