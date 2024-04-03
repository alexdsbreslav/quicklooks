import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

class distribution_plot:
    """
    dist = ql.distribution_plot(chart_skeleton,
    data = ,
    override_chart_skeleton = True,
    distribution_min_max = (None,None),
    bin_interval = None, #If dist_type is smooth_density, None
    dist_type = 'binned_counts', #['binned_counts', 'binned_density', 'smooth_density']
    color = chart_skeleton.color_library.default,
    opacity = 1,
    label = '',
    layer_order = 1)
    """

    def __init__(self, chart_skeleton, data, override_chart_skeleton,
    distribution_min_max, bin_interval,
    dist_type, color, opacity, label, layer_order):

        if not chart_skeleton.ax:
            raise Exception('The chart skeleton has not been built. You must build a chart skeleton for each new plot that you want to create.\n'
                            'Run quicklook.build_chart_skeleton to build a chart skeleton.')

        if chart_skeleton.xaxis_type == 'timeseries':
            raise Exception('''The chart skeleton xtick_label is set to a timeseries (e.g., months, days).
                               This is not compatible with a distribution plot.''')

        # ---- check data types
        if type(data) in [str, int, float, bool]:
            raise TypeError('x is not properly defined. x should be a 1 dimensional array of values.')
        # ---- check data shape and turn into series
        if np.shape(np.shape(data))[0] != 1:
            raise TypeError('data is not properly defined.; it is a {} x {} array. data must be 1-dimensional array.'.format(np.shape(data)[0], np.shape(data)[1]))
        data = pd.Series(data)


        # ---- auto set bins to integers between min and max
        if override_chart_skeleton:
            print('override_chart_skeleton is on.\n'
            'Look at the automatic settings we''ve generated and update your code above with appropriate settings.\n'
            'We highly recommend turning override_chart_skeleton off after updating your code.\n')
            # ---- get the data range
            data_range = np.max(data) - np.min(data)

            # ---- set the bins
            # ---- if the range is big, work it down until it has < 15 bins
            if data_range >= 10:

                # ---- set xlim to data min and max
                plt.xlim(np.floor(np.min(data)), np.ceil(np.max(data)));
                interval = 1
                bins = np.arange(np.floor(np.min(data)), np.ceil(np.max(data))+1, interval)
                while np.shape(bins)[0] >= 15:
                    interval += 1
                    bins = np.arange(np.floor(np.min(data)), np.ceil(np.max(data))+1, interval)
            # ---- if the range is small, work it up until it has >= 10 bins
            else:
                i = 0
                intervals = [0.5, 0.25, 0.2, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.00001]
                interval = intervals[i]
                decimals = [2,2,2,2,2,3,3,4,4]
                bins = np.arange(np.floor(np.min(data) * 10**decimals[i]) / 10**decimals[i],
                                 (np.ceil(np.max(data) * 10**decimals[i]) / 10**decimals[i])+interval,
                                 interval)
                while np.shape(bins)[0] < 10:
                    i += 1
                    interval = intervals[i]
                    bins = np.arange(np.floor(np.min(data) * 10**decimals[i]) / 10**decimals[i],
                                 (np.ceil(np.max(data) * 10**decimals[i]) / 10**decimals[i])+interval,
                                 interval)

                # ---- set xlim to data min and max
                plt.xlim(np.floor(np.min(data) * 10**decimals[i]) / 10**decimals[i],
                                 (np.ceil(np.max(data) * 10**decimals[i]) / 10**decimals[i])+interval);

            # ---- set ylim to 0 and max in bin
            binned_data = pd.cut(data, bins=bins).value_counts()
            if dist_type in ['binned_density', 'smooth_density']:
                plt.ylim(0, binned_data.max()/(binned_data.sum()*interval));
            elif dist_type == 'binned_counts':
                plt.ylim(0, np.ceil(binned_data.max()));
            else:
                raise KeyError('dist_type is not properly defined; it must be binned_counts, binned_density, or smooth_density')

            # ---- set the xticks to be on the bin edges
            xticks = bins
            plt.xticks(xticks)
            # ---- if that creates too many ticks, only plot every nth tick
            i = 1
            while chart_skeleton.ax.get_xticks().shape[0] > 10:
                i += 1
                plt.xticks(xticks[::i])

            # ---- set the yticks to a max of 10 ticks
            chart_skeleton.ax.yaxis.set_major_locator(plt.MaxNLocator(5))

        # ---- set bins manually if override_chart_skeleton is not on
        elif dist_type in ['binned_density', 'binned_counts']:
            bins = np.arange(distribution_min_max[0], distribution_min_max[1]+bin_interval, bin_interval)

        # ---- check for too many ticks
        if chart_skeleton.ax.get_xticks().shape[0] > 20:
            raise RuntimeError('quicklook is trying to plot too many xticks; increase the x_tick_interval')
        if chart_skeleton.ax.get_yticks().shape[0] > 20:
            raise RuntimeError('quicklook is trying to plot too many yticks; increase the y_tick_interval')

        # ---- get colors
        fill = color[1]

        if dist_type == 'smooth_density':
            dist = sns.kdeplot(data, fill=True, linewidth=0, color=fill,
                               clip= chart_skeleton.ax.get_xlim() if override_chart_skeleton else distribution_min_max,
                               alpha=opacity, ax=chart_skeleton.ax,
                               zorder=3, label=label);

        else:
            # ---- plot distribution
            dist = chart_skeleton.ax.hist(data, bins=bins, alpha=opacity,
                                      rwidth=0.85, color=fill, density= dist_type == 'binned_density',
                                      linewidth=0, label=label,
                                      zorder = 3, joinstyle='round');
        if override_chart_skeleton:
            print('Your build_chart_skeleton settings are automatically being set as:\n'
                  '- x_min_max = {}\n'
                  '- y_min_max = {} \n'
                  '- xtick_interval = {}\n'
                  '- ytick_interval = {}\n\n'
                  'Your add_distribution_plot settings are automatically being set as:\n'
                  '- distribution_min_max = {}\n'
                  '- bin_interval = {} \n'.format(chart_skeleton.ax.get_xlim(),
                                                  chart_skeleton.ax.get_ylim(),
                                                  chart_skeleton.ax.get_xticks()[1]-chart_skeleton.ax.get_xticks()[0],
                                                  chart_skeleton.ax.get_yticks()[1],
                                                  chart_skeleton.ax.get_xlim(),
                                                  interval))
        self.distribution_obj = dist
