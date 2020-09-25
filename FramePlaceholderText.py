from tkinter import *

import gettext

t = gettext.translation('messages', './locale', languages=['ru'])
t.install()
_ = t.gettext


class FramePlaceholderText(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.output_placeholder_text()

    def output_placeholder_text(self):
        var = StringVar()
        label = Label(self, textvariable=var, font='Arial 20')
        var.set(_("Selected parameter"))

        var_result = StringVar()
        label_result = Label(self, textvariable=var_result, font='Arial 14')
        var_result.set(_("Result of search:"))

        for i in range(1, 8):
            self.rowconfigure(i, {'minsize': 30})

        label.grid(row=0, column=0, columnspan=2)
        label_result.grid(row=9, column=0, sticky=W)
