# Create elements for sennit

from tkinter import *
from tkinter import ttk
from CablingGen import FramePlaceholderText

_ = FramePlaceholderText.t.gettext

x_indent_40 = 40
x_indent_20 = 20


def output_sennit(frame):
    var_sennit_standard = StringVar()
    sennit_label_standard = Label(frame, textvariable=var_sennit_standard, font='Arial 12')
    var_sennit_standard.set(_("Standard:"))

    sennit_standard = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    var_sennit_diameter_in = StringVar()
    sennit_label_diameter_in = Label(frame, textvariable=var_sennit_diameter_in, font='Arial 12')
    var_sennit_diameter_in.set(_("Inner diameter (mm):"))

    sennit_diameter_in = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    sennit_label_standard.grid(row=0, column=0, padx=x_indent_40, sticky=W)
    sennit_standard.grid(row=1, column=0, padx=x_indent_40, sticky=W)

    sennit_label_diameter_in.grid(row=0, column=3, sticky=W, padx=x_indent_20)
    sennit_diameter_in.grid(row=1, column=3, sticky=W, padx=x_indent_20)
