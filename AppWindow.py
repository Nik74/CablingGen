# AppWindow creates an app window
from tkinter import *
from tkinter import ttk
from win32api import GetSystemMetrics
from CablingGen import TreeView, FramePlaceholderText

path_logo_ico = 'img/logo.ico'


class AppWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("CablingGen")
        self.iconbitmap(path_logo_ico)
        self.resizable(width=False, height=False)

        # Setting the size of the app window relative to the user's screen resolution
        width_window = GetSystemMetrics(0) / 2.5
        height_window = GetSystemMetrics(1) / 2.025

        # Setting the location of the application window relative to the user's screen resolution
        w_center = (GetSystemMetrics(0) - width_window) / 2
        h_center = (GetSystemMetrics(1) - height_window) / 2

        # Creating an application window
        self.geometry("{}x{}+{}+{}".format(int(width_window), int(height_window), int(w_center), int(h_center)))

        style = ttk.Style()
        style.theme_use('vista')

        TreeView.TreeView(master=self)

        self.mainloop()
