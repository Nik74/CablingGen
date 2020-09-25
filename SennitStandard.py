# Create elements for sennit standard

from tkinter import *
from tkinter import ttk
from CablingGen import FramePlaceholderText, Sennit

_ = FramePlaceholderText.t.gettext

x_indent_9 = 9


def output_sennit_standard(frame):
    frame.rowconfigure(2, {'minsize': 12.5})

    var_wall_thick = StringVar()
    label_wall_thick = Label(frame, textvariable=var_wall_thick, font='Arial 12')
    var_wall_thick.set(_("Wall thickness (mm):"))

    wall_thick = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    var_diameter_in = StringVar()
    label_diameter_in = Label(frame, textvariable=var_diameter_in, font='Arial 12')
    var_diameter_in.set(_("Inner diameter (mm):"))

    diameter_in = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    var_diameter_out = StringVar()
    label_diameter_out = Label(frame, textvariable=var_diameter_out, font='Arial 12')
    var_diameter_out.set(_("Outer diameter (mm):"))

    diameter_out = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    label_wall_thick.grid(row=0, column=0, padx=Sennit.x_indent_40, sticky=W)
    wall_thick.grid(row=1, column=0, padx=Sennit.x_indent_40, sticky=W)

    label_diameter_in.grid(row=0, column=3, sticky=W, padx=x_indent_9)
    diameter_in.grid(row=1, column=3, sticky=W, padx=x_indent_9)

    label_diameter_out.grid(row=3, column=0, padx=Sennit.x_indent_40, sticky=W)
    diameter_out.grid(row=4, column=0, padx=Sennit.x_indent_40, sticky=W)
