import matplotlib.pyplot as plt

def plot_err_line(ax, c_lib, size, x, y_mean, y_err, linewidth, color_str, marker_on, marker_shape, label, zorder):
    """
    mean, ub, lb, fill = plot_err_line(ax, c_lib, size,
    x = ,
    y_mean = ,
    y_err = ,
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
        fill = 1
        edge = 2
    #dark style
    elif c_lib['bg'] == '#292d34':
        fill = 2
        edge = 1

    fill = ax.fill_between(
                          x,
                          y_mean - y_err,
                          y_mean + y_err,
                          color = c_lib[color_str][fill],
                          label = None,
                          alpha = 0.2,
                          zorder = zorder);
    mean = ax.plot(
                x,
                y_mean,
                linewidth = linewidth,
                color = c_lib[color_str][0],
                marker = marker_shape,
                markersize = markersize,
                label = label,
                zorder = zorder);
    ub = ax.plot(
                x,
                y_mean + y_err,
                linewidth = 0.5,
                color = c_lib[color_str][edge],
                label = None,
                zorder = zorder);
    lb = ax.plot(
                x,
                y_mean - y_err,
                linewidth = 0.5,
                color = c_lib[color_str][edge],
                label = None,
                zorder = zorder);
    return(mean, ub, lb, fill)
