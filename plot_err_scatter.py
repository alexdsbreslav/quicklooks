import matplotlib.pyplot as plt
import matplotlib.patches as patch

def plot_err_scatter(ax, c_lib, x, y, xerr, yerr, color_str, zorder, label):
    """
    scatter, err_fill, err_outline = plot_err_scatter(ax, c_lib,
    x = ,
    y = ,
    xerr = ,
    yerr = ,
    color_str = ,
    zorder = 1,
    label = '')
    """
    #light style
    if c_lib['bg'] == '#fafbfc':
        fill = 1
    #dark style
    elif c_lib['bg'] == '#292d34':
        fill = 2

    scatter = ax.scatter(x = x, y = y, color = c_lib[color_str][3-fill], label = label, zorder = zorder+1);

    for pt in range(len(x)):
        err_fill = ax.add_patch(patch.Ellipse((x.iloc[pt],y.iloc[pt]), xerr.iloc[pt] * 2, yerr.iloc[pt] * 2,
                                                facecolor = c_lib[color_str][fill], alpha = .8, zorder = zorder))
        err_outline = ax.add_patch(patch.Ellipse((x.iloc[pt],y.iloc[pt]), xerr.iloc[pt] * 2, yerr.iloc[pt] * 2,
                                                    facecolor = 'none', edgecolor = c_lib[color_str][0], alpha = 0.3, linewidth = 2, zorder = zorder))
    return(scatter, err_fill, err_outline)
