import matplotlib.pyplot as plt

def plot_line(ax, c_lib, size, x, y, linewidth, color_str, marker_on, marker_shape, label, zorder):
    """
    line = plot_line(ax, c_lib, size,
    x = ,
    y = ,
    linewidth = 3,
    color_str = '',
    marker_on = True,
    marker_shape = 'o',
    label = '',
    zorder = 1)
    """

    markersize = {'small':8, 'default':10, 'poster':10, 'poster_small':8}

    if marker_on == True:
        markersize = markersize[size]
    else:
        markersize = 0

    #light style
    if c_lib['bg'] == '#fafbfc':
        fill = 0
        edge = 2
    #dark style
    elif c_lib['bg'] == '#292d34':
        fill = 0
        edge = 1


    line = ax.plot(
            x,
            y,
            linewidth = linewidth,
            color = c_lib[color_str][0],
            marker = marker_shape,
            markersize = markersize,
            mec = c_lib[color_str][edge],
            mfc = c_lib[color_str][fill],
            mew = 2,
            label = label,
            zorder = zorder);
    return(line)
