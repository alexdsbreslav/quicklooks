# quicklook.distribution_plot
To add a bar to your chart, you will use the code:
```python
dist = ql.distribution_plot(chart_skeleton,
data = ,
override_chart_skeleton = True,
distribution_min_max = (None,None),
bin_interval = None, #If dist_type is smooth_density, None
dist_type = 'binned_counts', #['binned_counts', 'binned_density', 'smooth_density']
color = chart_skeleton.color_library.default,
color_brightness = 'default', #{}
opacity = 1,
label = '',
layer_order = 1)
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. Once you've typed `ql.bar_plot` into your notebook, you can hit `shift-tab` to view and copy/paste the Docstring.
## Parameters
## Returns
## Examples
## Note
### When you use `override_chart_skeleton` you'll get a printout that looks something like:  
```
override_chart_skeleton is on.
Look at the automatic settings weve generated and update your code above with appropriate settings.
We highly recommend turning override_chart_skeleton off after updating your code.

Your build_chart_skeleton settings are automatically being set as:
- x_min_max = (-19.0, 27.0)
- y_min_max = (0.0, 19.0)
- xtick_interval = 8.0
- ytick_interval = 4.0

Your add_distribution_plot settings are automatically being set as:
- distribution_min_max = (-19.0, 27.0)
- bin_interval = 4
```
At this point, we want to update all of our settings to create a neat, shareable, distribution plot. We'll set `override_chart_skeleton = False` and update all six settings listed above.

### To accurately compare multiple distributions, I **strongly recommend**:
- Using the same `distribution_min_max` for both variables
- Using the same `bin_interval` for both variables
- Setting `dist_type = 'binned_density'` (density refers to a probability density<sup>*</sup>)
- Setting `opacity = 0.5` so you can see overlapping parts

<sup>*</sup>For more info, [right-click here](https://machinelearningmastery.com/probability-density-estimation/) to open an article by Jason Brownlee and read through "Summarize Density with a Histogram".

###  Using `dist_type = 'smooth_density'`
I did not show an example with `dist_type = 'smooth_density'`. This setting turns your distribution in a [kernal density estimate](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). Kernel density estimates look nice, but they obscure important information about your distribution like the true shape, minimum, and maximum. I only recommend using `dist_type = 'smooth_density'` if you need to compare multiple overlapping distributions and all that you care about is the rough shape.

If you set `dist_type = 'smooth_density'`, `bin_interval` is ignored. The distrbution is clipped/cropped using `distribution_min_max`.
