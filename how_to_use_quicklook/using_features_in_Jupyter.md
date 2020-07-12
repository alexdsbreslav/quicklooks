# Using features in JupyterLab to copy-and-paste code
JupyterLab and Jupyter Notebooks make it easy to copy and paste code directly into your notebook.
- **Step 1:** import quicklook into your notebook
```python
import quicklook
```
- **Step 2:** type
```python
quicklook.
```
and hit `tab`. When you do that a drop down of all of the functions in quicklook should show up. Notice that they all have a blue f next to them.
![tab](https://github.com/alexdsbreslav/quicklook/blob/master/images/tab.png)

- **Step 3:** start typing out the function that you want, once it is the only one left in the list, you can hit `enter` and it will fill in the rest.
```python
quicklook.build_chart_skeleton
```

- **Step 4:** hold `shift` and hit `tab`. When you do, you should see a pop-up with the function's documentation. Scroll down to the part that says `Docstring:`. Copy everything under `Docstring:` though to the last `)`. Select the code in the cell and paste over it. The code in your cell should match what was in the `Docstring:`
![shift_tab](https://github.com/alexdsbreslav/quicklook/blob/master/images/shift_tab.png)

- **Step 5:** Fill in any blanks and adjust default settings in the code as needed. Hold `shift` and hit `enter` to execute the code cell and show your new chart!
![chart](https://github.com/alexdsbreslav/quicklook/blob/master/images/chart.png)
