# frame for output result

from tkinter import *
from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO


class FrameResult(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(height=int(AGO.height_frame_result), width=int(AGO.width_frame_result))
