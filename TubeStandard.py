# Create elements for tube standard

from tkinter import *
from tkinter import ttk
from win32api import GetSystemMetrics


width_window = GetSystemMetrics(0) / 2.5
height_window = GetSystemMetrics(1) / 2.025


class TubeStandard(Label, ttk.Combobox):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.output_tube_standard()

    def output_tube_standard(self):
        var_color = StringVar()
        label_color = Label(self, textvariable=var_color, font='Arial 12')
        var_color.set("Цвет:")

        color = ttk.Combobox(self, state="readonly", font='Arial 10', height=5)

        var_diameter_in = StringVar()
        label_diameter_in = Label(self, textvariable=var_diameter_in, font='Arial 12')
        var_diameter_in.set("Внутренний диаметр (мм):")

        diameter_in = ttk.Combobox(self, state="readonly", font='Arial 10', height=5)

        label_diameter_in.grid(row=0, column=3, sticky=W, padx=20)
        diameter_in.grid(row=1, column=3, sticky=W, padx=20)

        label_color.grid(row=0, column=0, padx=40, sticky=W)
        color.grid(row=1, column=0, padx=40, sticky=W)
