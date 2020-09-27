# Template for creating and displaying label

from tkinter import *
from tkinter import ttk
from CablingGen.Auxiliary import AuxiliaryFunctionsForLabel


class Labels:
    def __init__(self, frame=None, row=None, col=None, pad_x=None, message=None, width=None, file=None, num=None):
        var = StringVar()
        self.label = Label(frame, textvariable=var, font='Arial 12', width=width, anchor=W)
        var.set(message)

        self.combobox = ttk.Combobox(frame, state="readonly", font='Arial 10', height=5, width=22)

        if file is not None:
            read_elements = AuxiliaryFunctionsForLabel.read_file(file, num)

            self.combobox['values'] = read_elements

        self.label.grid(row=row, column=col, padx=pad_x, sticky=W)
        self.combobox.grid(row=row + 1, column=col, padx=pad_x, sticky=W)

        self.combobox.bind("<<ComboboxSelected>>", self.func)

    def func(self, event):
        print(self.combobox.get())
