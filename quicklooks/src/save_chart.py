import os

def save_chart(chart_skeleton,
                        chart_name,
                        path_to_folder_to_save_chart_in,
                        print_confirmation=True,
                        format='png'):
    """
    quicklook.save_chart_to_computer(chart_skeleton,
                         chart_name = '',
                         path_to_folder_to_save_chart_in = '',
                         print_confirmation=True)
    """

    dpi = {'notebook': 300, 'full_slide': 72, 'half_slide': 72}
    plt.savefig(os.path.join(path_to_folder_to_save_chart_in, chart_name+'.{}'.format(format)), format=format, dpi=dpi[chart_skeleton['size']]);
    if print_confirmation:
        print('{} saved in the folder: {}'.format(chart_name, path_to_folder_to_save_chart_in));
    return()
