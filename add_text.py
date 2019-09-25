import matplotlib.pyplot as plt

def add_text(ax, c_lib, fonts, frame_on, text, x_loc, y_loc, hor_align, vert_align, zorder):
    """
    text = add_text(ax, c_lib, fonts,
    frame_on = True,
    text = '',
    x_loc = ,
    y_loc = ,
    hor_align = 'center',
    vert_align = 'center',
    zorder = 1)
    """

    if frame_on == True:
        text = ax.text(x_loc, y_loc, text,
                        horizontalalignment=hor_align, verticalalignment=vert_align,
                        size = fonts['size'][1], color=c_lib['text'],
                        bbox = dict(facecolor = c_lib['bg'], edgecolor = c_lib['text'],
                        boxstyle = 'round, pad = 0.5', alpha = 1, linewidth = 0.5, zorder = zorder));
    else:
        text = ax.text(x_loc, y_loc, text,
                        horizontalalignment=hor_align, verticalalignment=vert_align,
                        size = fonts['size'][1], color=c_lib['text']);

    return(text)
