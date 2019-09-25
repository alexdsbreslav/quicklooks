import matplotlib.pyplot as plt

def plot_scatter(ax, c_lib, size, x, y, color_str, zorder, label):
    """
    scatter = plot_scatter(ax, c_lib, size,
    x = ,
    y = ,
    color_str = ,
    zorder = 1,
    label = '')
    """

    # size of scatter points and edge width
    if type(size) is str:
        markersize = {'small':50, 'default':120, 'poster':50, 'poster_small':30}
        edge_width = {'small':1, 'default':2, 'poster':3, 'poster_small':2}

        markersize = markersize[size]
        edge_width = edge_width[size]
    else:
        markersize = size
        edge_width = 1

    #light style
    if c_lib['bg'] == '#fafbfc':
        fill = 0
        edge = 2
    #dark style
    elif c_lib['bg'] == '#292d34':
        fill = 0
        edge = 1

    scatter = ax.scatter(x = x, y = y, color = c_lib[color_str][fill], edgecolor = c_lib[color_str][edge],
               s = markersize, label = label, zorder = zorder, linewidths=edge_width);
    return(scatter)
