# quicklook How-To
**quicklook is written to be copied-and-pasted into your code**. I use quicklook in JupyterLab (and Jupyter Notebook) and I wrote it with that user interface in mind. If you do not already use JupyterLab and are interested in learning how, check out my [python_for_uxr tutorial](https://github.com/alexdsbreslav/python_for_uxr).

## Before you start...
1. Make sure that quicklook is imported into your notebook. At the top of every one of my notebooks, I import quicklook along with several other key packages:
```python
import pandas as pd
import numpy as np
import os
import quicklook
```
2. Learn a few tips that will make copying-and-pasting quicklook code into your Jupyter Notebook quick and easy. [Right-click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md) to open the cheat-sheet in a new tab.

## For each new chart that you want to create...
### Step 1: Build a chart skeleton.
A **chart skeleton** is the background, title, axes, and axis labels. It is a skeleton (or wireframe, or background) that we will layer **plots** onto.
**Plots** are various ways that we can visualize data like line plots, bar plots, histograms, scatter plots etc.
- [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) to go to directions for building a chart skeleton.

### Step 2: Add plots to your chart skeleton to visualize your data.
Click on the links below to go to directions for that plot:
- [Add a line plot to your chart](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/add_line_to_chart.md)
- Add a line plot (with error) to your chart
- Add a vertical line to your chart
- Add a horizontal line to your chart
- Add a scatter plot to your chart
- Add a scatter plot (with error) to your chart
- Add a histogram to your chart
- Add a bar plot to your chart

For each of these plots, you need to **choose colors**! [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/setting_your_chart_style.md) for directions of specifying colors in your plots.

### Step 3: Add text and/or a legend to provide context for your visualization.
Click on the links below to go to directions for that feature:
- Add a legend to your chart
- Add text to your chart

### Optional: Export your plot.
Most of the time, my plots live within my Jupyter Notebooks. Sometimes you may want to export your plots to put them in slides or share them with colleagues. [Click here]() for directions for exporting your plots.
