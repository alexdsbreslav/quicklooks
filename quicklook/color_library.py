# ---- define the color library
# ---- based on Open Color https://yeun.github.io/open-color/
color_library = {'properties':{'name': 'default',
                             'brightness': {'light': [1,1,3], 'default': [4,4,6], 'dark': [7,7,9]},
                             'default_color': 'blue',
                             'background': '#ffffff',
                             'text': '#000000'},
                 'colors':{'gray': ['#f8f9fa','#f1f3f5','#e9ecef','#dee2e6','#ced4da','#adb5bd','#868e96','#495057','#343a40','#212529'],
                             'red': ['#fff5f5','#ffe3e3','#ffc9c9','#ffa8a8','#ff8787','#ff6b6b','#fa5252','#f03e3e','#e03131','#c92a2a'],
                             'pink': ['#fff0f6','#ffdeeb','#fcc2d7','#faa2c1','#f783ac','#f06595','#e64980','#d6336c','#c2255c','#a61e4d'],
                             'grape': ['#f8f0fc','#f3d9fa','#eebefa','#e599f7','#da77f2','#cc5de8','#be4bdb','#ae3ec9','#9c36b5','#862e9c'],
                             'violet': ['#f3f0ff','#e5dbff','#d0bfff','#b197fc','#9775fa','#845ef7','#7950f2','#7048e8','#6741d9','#5f3dc4'],
                             'indigo': ['#edf2ff','#dbe4ff','#bac8ff','#91a7ff','#748ffc','#5c7cfa','#4c6ef5','#4263eb','#3b5bdb','#364fc7'],
                             'blue': ['#e7f5ff','#d0ebff','#a5d8ff','#74c0fc','#4dabf7','#339af0','#228be6','#1c7ed6','#1971c2','#1864ab'],
                             'cyan': ['#e3fafc','#c5f6fa','#99e9f2','#66d9e8','#3bc9db','#22b8cf','#15aabf','#1098ad','#0c8599','#0b7285'],
                             'teal': ['#e6fcf5','#c3fae8','#96f2d7','#63e6be','#38d9a9','#20c997','#12b886','#0ca678','#099268','#087f5b'],
                             'green': ['#ebfbee','#d3f9d8','#b2f2bb','#8ce99a','#69db7c','#51cf66','#40c057','#37b24d','#2f9e44','#2b8a3e'],
                             'lime': ['#f4fce3','#e9fac8','#d8f5a2','#c0eb75','#a9e34b','#94d82d','#82c91e','#74b816','#66a80f','#5c940d'],
                             'yellow': ['#fff9db','#fff3bf','#ffec99','#ffe066','#ffd43b','#fcc419','#fab005','#f59f00','#f08c00','#e67700'],
                             'orange': ['#fff4e6','#ffe8cc','#ffd8a8','#ffc078','#ffa94d','#ff922b','#fd7e14','#f76707','#e8590c','#d9480f']}}

# ---- define the colors based on the style
def define_colors(chart_skeleton, color_name, color_brightness):
    
    # ---- if color is text, there is no variation
    if color_name == 'text':
        line = color_library['properties']['text']
        fill = line
        edge = line
    else:
        # ---- check to make sure that the colors were entered properly
        if color_name not in list(color_library['colors'].keys()):
            raise KeyError('Color entered is not in the color library. Enter one of the follow colors:\n''{}'\
                            .format(list(color_library['colors'].keys())))

        # ---- make sure brightness was entered correctly
        if color_brightness not in list(color_library['properties']['brightness']):
            raise KeyError('Color brightness is not properly defined. color_brightness must be in {}'.format(list(color_library['properties']['brightness'])))


        line = color_library['colors'][color_name][color_library['properties']['brightness'][color_brightness][0]]
        fill = line
        edge = color_library['colors'][color_name][color_library['properties']['brightness'][color_brightness][2]]
    
    return line, fill, edge