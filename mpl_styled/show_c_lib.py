import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch

def show_c_lib(c_lib, fonts):
    """
    show_c_lib(c_lib, fonts)
    """
    fig, ax = plt.subplots(nrows=1, figsize = (6,12))

    # hide spines
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_facecolor(c_lib['bg'])
    fig.set_facecolor(c_lib['bg'])

    ax.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False)
    color_strs = list(c_lib.keys())[3:]
    nrows = len(color_strs)
    y_loc = np.linspace(0.9,0.1,nrows)
    for i in range(nrows):
        ax.add_patch(patch.Ellipse((0.2,y_loc[i]),0.4, 0.2, color=c_lib[color_strs[i]][0]));
        ax.add_patch(patch.Ellipse((0.5,y_loc[i]),0.4, 0.2, color=c_lib[color_strs[i]][1]));
        ax.add_patch(patch.Ellipse((0.8,y_loc[i]),0.4, 0.2, color=c_lib[color_strs[i]][2]));
        ax.text(1, y_loc[i], color_strs[i],
                    horizontalalignment='left', verticalalignment='center',
                    size = fonts['size'][1], color=c_lib['text'],
                    bbox = dict(facecolor = c_lib['bg'], edgecolor = 'none',
                    boxstyle = 'round, pad = 0.5', alpha = 1, linewidth = 0.5, zorder = 1));
    return()
