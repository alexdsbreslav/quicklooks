import numpy as np
import matplotlib.pyplot as plt

def plot_vert_line(ax, c_lib, x, ylim, width, style, color, label, zorder):
    """
    vert_line = plot_style.vert_line(ax, c_lib,
    x = ,
    ylim = (,),
    width = 3,
    style = '--',
    color = c_lib[''][0],
    label = '',
    zorder = 1)
    """
    vert_line = ax.plot(np.full(100,x), np.linspace(ylim[0],ylim[1],100), linestyle = style, linewidth = width, label = label, color = color, zorder = zorder)
    return(vert_line)
