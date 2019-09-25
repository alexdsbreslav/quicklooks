import numpy as np
import matplotlib.pyplot as plt

def plot_hor_line(ax, c_lib, y, xlim, width, style, color, label, zorder):
    """
    hor_line = plot_style.hor_line(ax, c_lib,
    y = ,
    xlim = (,),
    width = 3,
    style = '--',
    color = c_lib[''][0],
    label = '',
    zorder = 1)
    """
    hor_line = ax.plot(np.linspace(xlim[0],xlim[1],100), np.full(100,y), linestyle = style, linewidth = width, label = label, color = color, zorder = zorder)
    return(hor_line)
