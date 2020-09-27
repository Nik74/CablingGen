from win32api import GetSystemMetrics

import gettext

# height and width of window
height_window = int(GetSystemMetrics(1) / 2.025)
width_window = GetSystemMetrics(0) / 2.5

# object for translate message
t = gettext.translation('messages', './locale', languages=['ru'])
t.install()

# objects to indent from the border
x_indent_40 = 40
x_indent_20 = 20

# width of the objects
width_0 = 20  # width 0 column
width_3 = 21  # width 3 column

# files for sennit
file_sennit = ('./Material/Coil/Shell/Sennit/TU 16.K18-093-2007/TU 16.K18-093-2007.csv',
               './Material/Coil/Shell/Sennit/TU4833-002-08558606-95/TU4833-002-08558606-95.csv')

# files for tube
file_tube = ('./Material/Coil/Shell/Tube/GOST 19034-82/GOST 19034-82.csv',)

# file for wire
file_wire = ('./Material/Coil/Conductor/Wire/GOST 6323-79/GOST 6323-79.csv',
             './Material/Coil/Conductor/Wire/TU 16-505.945-76/TU 16-505.945-76.csv')
