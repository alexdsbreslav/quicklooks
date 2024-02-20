# quicklook.bar_plot
To add a bar to your chart, you will use the code:
```python
bar = ql.bar_plot(chart_skeleton,
xlabels = ,
y = ,
yerror = None, #If no values, None
bars_per_xlabel = 1,
bar_index = 0,
color = chart_skeleton.color_library.default,
opacity = 1,
label = '',
layer_order = 1)
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. Once you've typed `ql.bar_plot` into your notebook, you can hit `shift-tab` to view and copy/paste the Docstring.
## Parameters
## Returns
## Examples
## Note
- To add multiple bars, I set `bars_at_each_xlabel = 2`
- For the blue bars, I set `bar_index = 0`; this means that they will be created at the left most index 0.
- For the green bars, I set `bar_index = 1`; this means that they will be created at the right-most index 1<sup>*</sup>.
- If I wanted 3 bars at each x label: I would set `bars_at_each_xlabel = 3` and `bar_index = 0` would be the left, `bar_index = 1` would be in the middle, and `bar_index = 2` would be on the right.

<sup>*</sup>Remember that Python uses 0 index. This means that if there are two positions the bars can be in (left or right), there corresponding indices are 0 and 1.
