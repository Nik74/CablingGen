# Create elements for tube

from tkinter import *
from tkinter import ttk
from CablingGen import FramePlaceholderText, Sennit

_ = FramePlaceholderText.t.gettext


def output_tube(frame):
    frame.rowconfigure(2, {'minsize': 12.5})

    var_standard = StringVar()
    label_standard = Label(frame, textvariable=var_standard, font='Arial 12')
    var_standard.set(_("Standard:"))

    standard = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    var_diameter_in = StringVar()
    label_diameter_in = Label(frame, textvariable=var_diameter_in, font='Arial 12')
    var_diameter_in.set(_("Inner diameter (mm):"))

    diameter_in = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    var_color = StringVar()
    label_color = Label(frame, textvariable=var_color, font='Arial 12')
    var_color.set(_("Color:"))

    color = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    label_standard.grid(row=0, column=0, padx=Sennit.x_indent_40, sticky=W)
    standard.grid(row=1, column=0, padx=Sennit.x_indent_40, sticky=W)

    label_diameter_in.grid(row=0, column=3, sticky=W, padx=Sennit.x_indent_20)
    diameter_in.grid(row=1, column=3, sticky=W, padx=Sennit.x_indent_20)

    label_color.grid(row=3, column=0, padx=Sennit.x_indent_40, sticky=W)
    color.grid(row=4, column=0, padx=Sennit.x_indent_40, sticky=W)
