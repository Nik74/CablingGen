# Create elements for wire

from tkinter import *
from tkinter import ttk
from CablingGen import FramePlaceholderText, Sennit

_ = FramePlaceholderText.t.gettext

x_indent_31 = 31


def output_wire(frame):
    frame.rowconfigure(2, {'minsize': 12.5})
    frame.rowconfigure(5, {'minsize': 12.5})

    var_wire_thick = StringVar()
    label_wire_thick = Label(frame, textvariable=var_wire_thick, font='Arial 12')
    var_wire_thick.set(_("Wire thickness (mm):"))

    wire_thick = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    var_color = StringVar()
    label_color = Label(frame, textvariable=var_color, font='Arial 12')
    var_color.set(_("Color:"))

    color = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    var_mark = StringVar()
    lable_mark = Label(frame, textvariable=var_mark, font='Arial 12')
    var_mark.set(_("Mark:"))

    mark = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    var_section = StringVar()
    lable_section = Label(frame, textvariable=var_section, font='Arial 12')
    var_section.set(_("Section:"))

    section = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    var_standard = StringVar()
    label_standard = Label(frame, textvariable=var_standard, font='Arial 12')
    var_standard.set(_("Standard:"))

    standard = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5)

    label_standard.grid(row=0, column=0, padx=Sennit.x_indent_40, sticky=W)
    standard.grid(row=1, column=0, padx=Sennit.x_indent_40, sticky=W)

    label_wire_thick.grid(row=0, column=3, padx=x_indent_31, sticky=W)
    wire_thick.grid(row=1, column=3, padx=x_indent_31, sticky=W)

    label_color.grid(row=3, column=0, sticky=W, padx=Sennit.x_indent_40)
    color.grid(row=4, column=0, sticky=W, padx=Sennit.x_indent_40)

    lable_mark.grid(row=3, column=3, padx=x_indent_31, sticky=W)
    mark.grid(row=4, column=3, padx=x_indent_31, sticky=W)

    lable_section.grid(row=6, column=0, sticky=W, padx=Sennit.x_indent_40)
    section.grid(row=7, column=0, sticky=W, padx=Sennit.x_indent_40)
