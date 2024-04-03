# quicklooks.reference_line
To add a reference line to your chart, you will use the code:
```python
ref_line = ql.reference_line(chart_skeleton,
line_type = 'h', #['h' (hor), 'v' (vert), 'du' (diag-up), 'dd' (diag-down)]
location = , #If diag-up or diag-down, None
color = chart_skeleton.color_library.text,
linewidth = 2,
linestyle = '--', #['-', '--', ':', '-.']
marker_shape = None, #['o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
opacity = 1,
label = '',
layer_order = 1)
```

**Always copy and paste!** quicklooks is designed as a copy-and-paste package. Once you've typed `ql.reference_line` into your notebook, you can hit `shift-tab` to view and copy/paste the Docstring.
## Parameters
## Returns
## Examples
