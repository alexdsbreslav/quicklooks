import matplotlib.pyplot as plt

def add_legend(ax, c_lib, size, fonts, frame_on, loc, bbox_coord, markerscale, markercolor_str_set):
    """
    legend = add_legend(ax, c_lib, size, fonts,
    frame_on=False, loc = 'best', bbox_coord = (1,1),
    markerscale = 1, markercolor_str_set = []);
    """
    legend = ax.legend(loc=loc, bbox_to_anchor = bbox_coord, prop = fonts['label'],
                       frameon = frame_on, fancybox = True, shadow = True,
                       markerscale = markerscale, facecolor = c_lib['bg']);

    for text in legend.get_texts():
        text.set_color(c_lib['text'])

    # check if I've entered a list of strs for colors
    if not markercolor_str_set:
        markercolor_set = [c_lib[i][0] for i in markercolor_str_set]

        for idx in range(len(markercolor_str_set)):
            legend.legendHandles[-len(markercolor_set)+idx].set_color(markercolor_set[idx])
    return(legend)
