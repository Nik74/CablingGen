# Create elements for sennit

from tkinter import *
from tkinter import ttk
from win32api import GetSystemMetrics


width_window = GetSystemMetrics(0) / 2.5
height_window = GetSystemMetrics(1) / 2.025


class Sennit(Label, ttk.Combobox):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.output_sennit()

    def output_sennit(self):
        var_sennit_standard = StringVar()
        sennit_label_standard = Label(self, textvariable=var_sennit_standard, font='Arial 12')
        var_sennit_standard.set("Стандарт:")

        sennit_standard = ttk.Combobox(self, state="readonly", font='Arial 10', height=5)

        var_sennit_diameter_in = StringVar()
        sennit_label_diameter_in = Label(self, textvariable=var_sennit_diameter_in, font='Arial 12')
        var_sennit_diameter_in.set("Внутренний диаметр (мм):")

        sennit_diameter_in = ttk.Combobox(self, state="readonly", font='Arial 10', height=5)

        sennit_label_standard.grid(row=0, column=0, padx=40, sticky=W)
        sennit_standard.grid(row=1, column=0, padx=40, sticky=W)

        sennit_label_diameter_in.grid(row=0, column=3, sticky=W, padx=20)
        sennit_diameter_in.grid(row=1, column=3, sticky=W, padx=20)
