# quicklook How-To
quicklook is written to be copied-and-pasted into your code. It makes visualization easy and lowers to barrier to creating attractive plots.
I use quicklook in JupyterLab (and Jupyter Notebook) and I wrote it with that user interface in mind.
If you do not already use JupyterLab and are interested in learning how, check out my python_for_uxr tutorial.

## Using features in JupyterLab to copy-and-paste code
JupyterLab and Jupyter Notebooks make it easy to copy and paste code directly into your notebook.
- Step 1: import quicklook into your notebook
```python
import quicklook
```
- Step 2: type
```python
quicklook.
```
and hit `tab`. When you do that a drop down of all of the functions in quicklook should show up. Notice that they all have a blue f next to them.
![tab](https://github.com/alexdsbreslav/quicklook/blob/master/images/tab.png)

- Step 3: start typing out the function that you want, once it is the only one left in the list, you can hit `enter` and it will fill in the rest.
```python
quicklook.build_chart_skeleton
```
- Step 4: hold `shift` and hit `tab`. When you do, you should see a pop-up with the function's documentation. Scroll down to the part that says `Docstring:`. Copy everything under `Docstring:` though to the last `)`. Select the code in the cell and paste over it. The code in your cell should match what was in the `Docstring:`
![shift_tab](https://github.com/alexdsbreslav/quicklook/blob/master/images/shift_tab.png)

## Step 1: Build a chart skeleton.
A **chart skeleton** is the background, title, axes, and axis labels. It is a skeleton (or wireframe, or background) that we will layer **plots** onto.
**Plots** are various ways that we can visualize data like line plots, bar plots, histograms, scatter plots etc.

## Step 2: Add plots to your chart skeleton to visualize your data.
Click on any of the links below to go to directions for that plot:
- Add a line plot to your chart
- Add a line plot (with error) to your chart
- Add a vertical line to your chart
- Add a horizontal line to your chart
- Add a scatter plot to your chart
- Add a scatter plot (with error) to your chart
- Add a histogram to your chart
- Add a bar plot to your chart

For each of these plots, you need to **choose colors**! Click here for directions of specifying colors in your plots.

## Step 3: Add text and/or a legend to provide context for your visualization.
Click on any of the links below to go to directions for that feature:
- Add a legend to your chart
- Add text to your chart

## Step 4: Export your plot.
