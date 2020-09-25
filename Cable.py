# Create elements for cable

from tkinter import *
from tkinter import ttk
from CablingGen import FramePlaceholderText, Sennit

_ = FramePlaceholderText.t.gettext

x_indent_36 = 36


def output_cable(frame):
    var_standard = StringVar()
    label_standard = Label(frame, textvariable=var_standard, font='Arial 12')
    var_standard.set(_("Standard:"))

    standard = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    var_density = StringVar()
    label_density = Label(frame, textvariable=var_density, font='Arial 12')
    var_density.set(_("Density of the cable:"))

    density = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    label_standard.grid(row=0, column=0, padx=Sennit.x_indent_40, sticky=W)
    standard.grid(row=1, column=0, padx=Sennit.x_indent_40, sticky=W)

    label_density.grid(row=0, column=3, sticky=W, padx=x_indent_36)
    density.grid(row=1, column=3, sticky=W, padx=x_indent_36)
