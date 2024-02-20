# quicklook.legend
To add a legend to your chart, you will use the code:
```python
legend = ql.legend(chart_skeleton,
legend_location = ql.legend.loc.best, frame=False);
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. Once you've typed `ql.legend` into your notebook, you can hit `shift-tab` to view and copy/paste the Docstring.
## Prerequisites for adding a legend to your chart
The `ql.legend` function looks for plots that you've added to your chart skeleton and **labeled** and then puts those plots and labels into a legend.
1. You must have a chart skeleton.
2. Your chart skeleton must have one or more plots added to it.
3. Those plots must have labels!
4. The code `ql.legend` must come after your chart skeleton and plots.
## Parameters
## Returns
## Examples
