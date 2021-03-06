# frame creates a image

from tkinter import *
from PIL import Image, ImageTk
from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO
from CablingGen import Logs


class FrameImg(Frame):
    def __init__(self, master=None, img_path=None):
        super().__init__(master)
        self.master = master
        self.load_img(img_path=img_path)

    def load_img(self, img_path=None):
        try:
            img = Image.open(img_path)
            img = img.resize((int(AGO.width_window / 1.536), int(AGO.height_window / 1.075)), Image.ANTIALIAS)

            render = ImageTk.PhotoImage(img)

            initial = Label(self, image=render)
            initial.image = render
            initial.pack()
        except FileNotFoundError:
            Logs.logger.error("File {} not found!".format(img_path))
