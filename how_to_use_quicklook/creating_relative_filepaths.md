## Create a relative filepath to save your chart
To save your chart to your computer, we need to tell JupyterLab where to put it.  
To direct JupyterLab to the folder that we want to put the chart in, we need to define a file path.  
To define a file path, we first define our current directory. The current directory is where your notebook is located in our Finder. When I say *your notebook*, I'm referring the the Jupyter Notebook that you're using to create your data visualizations.

`os.path.abspath()` with `''` as an input will tell me what file directory I am currently working in.

```python
current_directory = os.path.abspath('')
```

Next, we want to define where our chart should go **relative** to our current directory. These are called **relative paths**; defining filepaths relative to where your notebook is really important for other people to be able to run your code. The code that we will use to define the relative filepath is essentially a set of directions to navigate from this Jupyter Notebook file to the folder that you want to put your chart.  

We are going to use two functions from the path module to do this:
1. `os.path.dirname()`: `dirname()` is short for directory name and will return the folder that contains the filepath that you enter.
2. `os.path.join()`: `join()` will add folder names to the file path.

`os.path.dirname(current_directory)` will return the folder that this notebook file is in. We can nest this function multiple times (e.g. `os.path.dirname(os.path.dirname(current_directory))` to return higher and higher level folders.  

For example,
```python
os.path.dirname(os.path.dirname('/Users/alex/Documents/example_experiment_scripts'))
```
will return the filepath
```python
'/Users/alex'
```
*Note that the filepath `/Users/alex` is unique to my computer. I am on a Mac and the username on my Mac in `alex`. This part of the filepath will be unique to your computer.*

`os.path.join()` will add folders and files to the filepath.

For example,
```python
os.path.join('/Users/alex', 'Documents', 'example_experiment', 'charts')
``` 
would return the following path to the folder `charts`
```python
'/Users/alex/Documents/example_experiment/charts'
```
So, imagine that you have a folder named `charts` that was right next to your Jupyter Notebook. You could use the following code to save your chart (called `example_chart_name`) in the `charts` folder.
```python
current_directory = os.path.abspath('')
quicklook.save_chart(chart_name = 'example_chart_name', 
                     path_to_folder_to_save_chart_in = os.path.join(current_directory, 'charts'),
                     print_confirmation=True);
```
