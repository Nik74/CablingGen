from win32api import GetSystemMetrics

import gettext

# height and width of window
height_window = int(GetSystemMetrics(1) / 2.025)
width_window = GetSystemMetrics(0) / 2.5

# height and width of the result field
height_frame_result = height_window / 2.53
width_frame_result = width_window / 1.43

# object for translate message
t = gettext.translation('messages', './locale', languages=['ru'])
t.install()

# objects to indent from the border
x_indent_40 = 40
x_indent_20 = 20

# width of the objects
width_0 = 20  # width 0 column
width_3 = 21  # width 3 column
