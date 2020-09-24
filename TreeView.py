# TreeView creates a tree list and output frames depending on the selected element in the tree

from tkinter import *
from tkinter import ttk
from win32api import GetSystemMetrics
from CablingGen import AuxiliaryFunctionsForTree, FrameImg, FramePlaceholderText, Sennit, SennitStandard, Tube, \
    TubeStandard

height_window = int(GetSystemMetrics(1) / 2.025)
width_window = GetSystemMetrics(0) / 2.5

path_img_coil = 'img/logo_coil.png'
path_img_shell = 'img/logo_shell.png'
path_img_conductor = 'img/logo_conductor.png'


class TreeView(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=10, pady=10, side='left', fill=Y)
        self.create_tree_and_frames(master=master)

    def create_tree_and_frames(self, master=None):
        tree_view = ttk.Treeview(self, height=height_window, selectmode='browse')

        tree_view.heading('#0', text='Material', anchor='w')

        result = AuxiliaryFunctionsForTree.add_list_to_tree_from_file(tree_view)

        tree_view.item(result, open=True)

        scrollbar_tree = Scrollbar(self, orient='horizontal')

        scrollbar_tree['command'] = tree_view.xview
        tree_view['xscrollcommand'] = scrollbar_tree.set

        scrollbar_tree.pack(side='bottom', fill=X)
        tree_view.pack()

        frame_img_coil = FrameImg.FrameImg(master=master, img_path=path_img_coil)
        AuxiliaryFunctionsForTree.pack_out(frame_img_coil)

        frame_placeholder_text = FramePlaceholderText.FramePlaceholderText(master=master)

        frame_img_shell = FrameImg.FrameImg(master=master, img_path=path_img_shell)

        frame_img_conductor = FrameImg.FrameImg(master=master, img_path=path_img_conductor)

        sennit_elements = Sennit.Sennit(master=frame_placeholder_text)

        sennit_standard = SennitStandard.SennitStandard(master=frame_placeholder_text)

        tube_elements = Tube.Tube(master=frame_placeholder_text)

        tube_standard=TubeStandard.TubeStandard(master=frame_placeholder_text)

        def clicks(event):
            # Elements for which you don't need to output frame_placeholder_text
            el_pl_te_pa_fo = ('', 'coil', 'shell', 'conductor')

            item = tree_view.identify('item', event.x, event.y)

            if item == 'coil' or item == '':
                AuxiliaryFunctionsForTree.pack_out(frame_img_coil)
            else:
                frame_img_coil.pack_forget()

            if item in el_pl_te_pa_fo:
                frame_placeholder_text.pack_forget()
            else:
                AuxiliaryFunctionsForTree.pack_out(frame_placeholder_text)

            if item == 'shell':
                AuxiliaryFunctionsForTree.pack_out(frame_img_shell)
            else:
                frame_img_shell.pack_forget()

            if item == 'conductor':
                AuxiliaryFunctionsForTree.pack_out(frame_img_conductor)
            else:
                frame_img_conductor.pack_forget()

            if item == 'sennit':
                tree_view.column("#0", minwidth="{}".format(int(width_window / 3.072)))

                AuxiliaryFunctionsForTree.grid_out_col(sennit_elements)
            else:
                sennit_elements.grid_forget()

            if item == 'tu 16.k18-093-2007' or item == 'tu4833-002-08558606-95':
                AuxiliaryFunctionsForTree.grid_out_col_row(sennit_standard)
            else:
                sennit_standard.grid_forget()

            if item == 'tube':
                AuxiliaryFunctionsForTree.grid_out_col_row(tube_elements)
            else:
                tube_elements.grid_forget()

            if item == 'gost 19034-82':
                AuxiliaryFunctionsForTree.grid_out_col(tube_standard)
            else:
                tube_standard.grid_forget()

        tree_view.bind("<1>", clicks)
