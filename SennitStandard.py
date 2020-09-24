# Create elements for sennit standard

from tkinter import *
from tkinter import ttk
from win32api import GetSystemMetrics


width_window = GetSystemMetrics(0) / 2.5
height_window = GetSystemMetrics(1) / 2.025


class SennitStandard(Label, ttk.Combobox):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.output_sennit_standard()

    def output_sennit_standard(self):
        self.rowconfigure(2, {'minsize': 12.5})

        var_wall_thick = StringVar()
        label_wall_thick = Label(self, textvariable=var_wall_thick, font='Arial 12')
        var_wall_thick.set("Толщина стены (мм):")

        wall_thick = ttk.Combobox(self, state="readonly", font='Arial 10', height=5)

        var_diameter_in = StringVar()
        label_diameter_in = Label(self, textvariable=var_diameter_in, font='Arial 12')
        var_diameter_in.set("Внутренний диаметр (мм):")

        diameter_in = ttk.Combobox(self, state="readonly", font='Arial 10', height=5)

        var_diameter_out = StringVar()
        label_diameter_out = Label(self, textvariable=var_diameter_out, font='Arial 12')
        var_diameter_out.set("Внутренний диаметр (мм):")

        diameter_out = ttk.Combobox(self, state="readonly", font='Arial 10', height=5)

        label_wall_thick.grid(row=0, column=0, padx=40, sticky=W)
        wall_thick.grid(row=1, column=0, padx=40, sticky=W)

        label_diameter_in.grid(row=0, column=3, sticky=W, padx=20)
        diameter_in.grid(row=1, column=3, sticky=W, padx=20)

        label_diameter_out.grid(row=3, column=0, padx=40, sticky=W)
        diameter_out.grid(row=4, column=0, padx=40, sticky=W)
