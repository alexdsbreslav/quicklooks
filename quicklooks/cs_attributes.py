class chart_ylabel:
    default = 'default'
    percents = 'percents'
    millions = '1m'
    hundredK = '100k'
    thousands = '1k'

class chart_xlabel:
    default = 'default'
    percents = 'percents'
    years = 'years'
    quarters = 'quarters'
    months = 'months'
    days = 'days'

class chart_size:
    notebook = 'notebook'
    half_slide = 'half_slide'
    full_slide = 'full_slide'

class fonts:
    lato = 'lato'
    montserrat = 'montserrat'
    oswald = 'oswald'
    roboto = 'roboto'
    rubik = 'rubik'
    source_sans = 'source_sans'
    work_sans = 'work_sans'

class color_libraries:
    class mariglow:
        default = ['#9AA7FE', '#4B64FE', '#203DFE'] #blue
        background = '#ffffff'
        text = '#000000'
        color_list = ['orange', 'peach', 'navy', 'blue']
        orange = ['#EF7B57', '#E94819', '#BB3911']
        peach = ['#FAF3EF', '#ECCFC0', '#DEAB91']
        navy = ['#2C4177', '#1A2747', '#0B101E']
        blue = ['#9AA7FE', '#4B64FE', '#203DFE']
        light_gray = ['#f1f3f5', '#e9ecef', '#dee2e6']
        gray = ['#ced4da', '#adb5bd', '#868e96']
        dark_gray = ['#495057', '#343a40', '#212529']
        black = ['#000000', '#000000', '#000000']

    class skygrove:
        default = ['#6E80D8', '#3E56CC', '#2B3FA1'] #blue
        background = '#ffffff'
        text = '#000000'
        color_list = ['blue', 'periwinkle', 'sea_green', 'green_tea']
        blue = ['#6E80D8', '#3E56CC', '#2B3FA1']
        periwinkle = ['#EBEFFF', '#ADBEFF', '#708DFF']
        sea_green = ['#57B27C', '#3E885B', '#2D6242']
        green_tea = ['#EAF0D1', '#D5E1A3', '#BFD274']
        light_gray = ['#f1f3f5', '#e9ecef', '#dee2e6']
        gray = ['#ced4da', '#adb5bd', '#868e96']
        dark_gray = ['#495057', '#343a40', '#212529']
        black = ['#000000', '#000000', '#000000']

    # https://yeun.github.io/open-color/
    class opencolor:
        """
        chart_skeleton.color_library.
        color_list = [chart_skeleton.color_library.light_red, 
                      chart_skeleton.color_library.red, 
                      chart_skeleton.color_library.light_dark_red,
                      chart_skeleton.color_library.light_pink, 
                      chart_skeleton.color_library.pink, 
                      chart_skeleton.color_library.light_dark_pink,
                      chart_skeleton.color_library.light_grape, 
                      chart_skeleton.color_library.grape, 
                      chart_skeleton.color_library.light_dark_grape,
                      chart_skeleton.color_library.light_violet, 
                      chart_skeleton.color_library.violet, 
                      chart_skeleton.color_library.dark_violet,
                      chart_skeleton.color_library.light_indigo, 
                      chart_skeleton.color_library.indigo, 
                      chart_skeleton.color_library.dark_indigo,
                      chart_skeleton.color_library.light_blue, 
                      chart_skeleton.color_library.blue, 
                      chart_skeleton.color_library.dark_blue,
                      chart_skeleton.color_library.light_cyan, 
                      chart_skeleton.color_library.cyan, 
                      chart_skeleton.color_library.dark_cyan,
                      chart_skeleton.color_library.light_teal, 
                      chart_skeleton.color_library.teal, 
                      chart_skeleton.color_library.dark_teal,
                      chart_skeleton.color_library.light_green, 
                      chart_skeleton.color_library.green, 
                      chart_skeleton.color_library.dark_green,
                      chart_skeleton.color_library.light_lime, 
                      chart_skeleton.color_library.lime, 
                      chart_skeleton.color_library.dark_lime,
                      chart_skeleton.color_library.light_yellow, 
                      chart_skeleton.color_library.yellow, 
                      chart_skeleton.color_library.dark_yellow,
                      chart_skeleton.color_library.light_orange, 
                      chart_skeleton.color_library.orange, 
                      chart_skeleton.color_library.dark_orange]
        """
        
        default = ['#4dabf7','#339af0','#228be6'] #blue
        background = '#ffffff'
        text = '#000000'
        color_list = [chart_skeleton.color_library.light_red', 'red', 'dark_red',
                      chart_skeleton.color_library.light_pink', 'pink', 'dark_pink',
                      chart_skeleton.color_library.light_grape', 'grape', 'dark_grape',
                      chart_skeleton.color_library.light_violet', 'violet', 'dark_violet',
                      chart_skeleton.color_library.light_indigo', 'indigo', 'dark_indigo',
                      chart_skeleton.color_library.light_blue', 'blue', 'dark_blue',
                      chart_skeleton.color_library.light_cyan', 'cyan', 'dark_cyan',
                      chart_skeleton.color_library.light_teal', 'teal', 'dark_teal',
                      chart_skeleton.color_library.light_green', 'green', 'dark_green',
                      chart_skeleton.color_library.light_lime', 'lime', 'dark_lime',
                      chart_skeleton.color_library.light_yellow', 'yellow', 'dark_yellow',
                      chart_skeleton.color_library.light_orange', 'orange', 'dark_orange']

        light_red = ['#ffe3e3','#ffc9c9','#ffa8a8']
        red = ['#ff8787','#ff6b6b','#fa5252']
        dark_red = ['#f03e3e','#e03131','#c92a2a']
        light_pink = ['#ffdeeb','#fcc2d7','#faa2c1']
        pink = ['#f783ac','#f06595','#e64980']
        dark_pink = ['#d6336c','#c2255c','#a61e4d']
        light_grape = ['#f3d9fa','#eebefa','#e599f7']
        grape = ['#da77f2','#cc5de8','#be4bdb']
        dark_grape = ['#ae3ec9','#9c36b5','#862e9c']
        light_violet = ['#e5dbff','#d0bfff','#b197fc']
        violet = ['#9775fa','#845ef7','#7950f2']
        dark_violet = ['#7048e8','#6741d9','#5f3dc4']
        light_indigo = ['#dbe4ff','#bac8ff','#91a7ff']
        indigo = ['#748ffc','#5c7cfa','#4c6ef5']
        dark_indigo = ['#4263eb','#3b5bdb','#364fc7']
        light_blue = ['#d0ebff','#a5d8ff','#74c0fc']
        blue = ['#4dabf7','#339af0','#228be6']
        dark_blue = ['#1c7ed6','#1971c2','#1864ab']
        light_cyan = ['#c5f6fa','#99e9f2','#66d9e8']
        cyan = ['#3bc9db','#22b8cf','#15aabf']
        dark_cyan = ['#1098ad','#0c8599','#0b7285']
        light_teal = ['#c3fae8','#96f2d7','#63e6be']
        teal = ['#38d9a9','#20c997','#12b886']
        dark_teal = ['#0ca678','#099268','#087f5b']
        light_green = ['#d3f9d8','#b2f2bb','#8ce99a']
        green = ['#69db7c','#51cf66','#40c057']
        dark_green = ['#37b24d','#2f9e44','#2b8a3e']
        light_lime = ['#e9fac8','#d8f5a2','#c0eb75']
        lime = ['#a9e34b','#94d82d','#82c91e']
        dark_lime = ['#74b816','#66a80f','#5c940d']
        light_yellow = ['#fff3bf','#ffec99','#ffe066']
        yellow = ['#ffd43b','#fcc419','#fab005']
        dark_yellow = ['#f59f00','#f08c00','#e67700']
        light_orange = ['#ffe8cc','#ffd8a8','#ffc078']
        orange = ['#ffa94d','#ff922b','#fd7e14']
        dark_orange = ['#f76707','#e8590c','#d9480f']
        light_gray = ['#f1f3f5', '#e9ecef', '#dee2e6']
        gray = ['#ced4da', '#adb5bd', '#868e96']
        dark_gray = ['#495057', '#343a40', '#212529']
        black = ['#000000', '#000000', '#000000']

    # https://www.figma.com/blog/bringing-new-life-to-figmas-brand/
    class figma:
        default =  #blue
        background = '#ffffff'
        text = '#000000'
        color_list = ['purple', 'periwinkle', 'blue', 'cornflower', 'yellow', 'green', 'coral', 'red']
        purple = ['#B887FD', '#A261FC', '#8835FD']
        periwinkle = ['#EFEBFE', '#C6BAFD', '#B29EFA']
        blue = ['#888AFC', '#5659FB', '#383BFA']
        cornflower = ['#C6D9FB', '#6B9DF4', '#79A7F6']
        yellow = ['#FED35D', '#FEC62E', '#FEBD0B']
        green = ['#27CE6F', '#20A85B', '#1A894A']
        coral = ['#FEB5AF', '#FD857B', '#FD6B5D']
        red = ['#F17255', '#EE4F2A', '#E23912']
        light_gray = ['#f1f3f5', '#e9ecef', '#dee2e6']
        gray = ['#ced4da', '#adb5bd', '#868e96']
        dark_gray = ['#495057', '#343a40', '#212529']
        black = ['#000000', '#000000', '#000000']
        
