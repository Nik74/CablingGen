# AppWindow creates an app window

from tkinter import *
from tkinter import ttk
from win32api import GetSystemMetrics
from CablingGen import TreeView, Logs
from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO

path_logo_ico = 'img/logo.ico'


class AppWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("CablingGen")
        self.iconbitmap(path_logo_ico)
        self.resizable(width=False, height=False)

        # Setting the location of the application window relative to the user's screen resolution
        w_center = int((GetSystemMetrics(0) - AGO.width_window) / 2)
        h_center = int((GetSystemMetrics(1) - AGO.height_window) / 2)

        # Creating an application window
        self.geometry("{}x{}+{}+{}".format(int(AGO.width_window), int(AGO.height_window), int(w_center), int(h_center)))

        style = ttk.Style()
        style.theme_use('vista')

        TreeView.TreeView(master=self)

        self.mainloop()
