# TreeView creates a tree list and output frames depending on the selected element in the tree

from tkinter import *
from tkinter import ttk
from CablingGen import Elements
from CablingGen.Frames import FrameImg, FramePlaceholderText, FrameResult
from CablingGen.Auxiliary import AuxiliaryFunctionsForTree as AFT, AuxiliaryGlobalObject as AGO

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
        tree_view = ttk.Treeview(self, height=AGO.height_window, selectmode='browse')

        tree_view.heading('#0', text='Material', anchor='w')

        result = AFT.add_list_to_tree_from_file(tree_view)

        tree_view.item(result, open=True)

        scrollbar_tree = Scrollbar(self, orient='horizontal')

        scrollbar_tree['command'] = tree_view.xview
        tree_view['xscrollcommand'] = scrollbar_tree.set

        scrollbar_tree.pack(side='bottom', fill=X)
        tree_view.pack()

        frame_img_coil = FrameImg.FrameImg(master=master, img_path=path_img_coil)
        AFT.pack_out(frame_img_coil)

        frame_placeholder_text = FramePlaceholderText.FramePlaceholderText(master=master)

        frame_img_shell = FrameImg.FrameImg(master=master, img_path=path_img_shell)

        frame_img_conductor = FrameImg.FrameImg(master=master, img_path=path_img_conductor)

        frame_result = FrameResult.FrameResult(master=frame_placeholder_text)
        frame_result.grid(row=10, column=0, columnspan=4)

        sennit_elements = Elements.Elements(master=frame_placeholder_text, element='Sennit')

        sennit_tu_16_k18_093_2007 = Elements.Elements(master=frame_placeholder_text, element='TU 16.K18-093-2007')

        sennit_tu4833_002_08558606_95 = Elements.Elements(master=frame_placeholder_text,
                                                          element='TU4833-002-08558606-95')

        tube_elements = Elements.Elements(master=frame_placeholder_text, element='Tube')

        tube_standard = Elements.Elements(master=frame_placeholder_text, element='TubeStandard')

        cable_elements = Elements.Elements(master=frame_placeholder_text, element='Cable')

        wire_elements = Elements.Elements(master=frame_placeholder_text, element='Wire')

        wire_tu_16_505_945_76 = Elements.Elements(master=frame_placeholder_text, element='TU 16-505.945-76')

        wire_gost_6323_79 = Elements.Elements(master=frame_placeholder_text, element='GOST 6323-79')

        def clicks(event):
            # Elements for which you don't need to output frame_placeholder_text
            el_pl_te_pa_fo = ('', 'coil', 'shell', 'conductor')

            item = tree_view.identify('item', event.x, event.y)

            if item == 'coil' or item == '':
                AFT.pack_out(frame_img_coil)
            else:
                frame_img_coil.pack_forget()

            if item in el_pl_te_pa_fo:
                frame_placeholder_text.pack_forget()
            else:
                AFT.pack_out(frame_placeholder_text)

            if item == 'shell':
                AFT.pack_out(frame_img_shell)
            else:
                frame_img_shell.pack_forget()

            if item == 'conductor':
                AFT.pack_out(frame_img_conductor)
            else:
                frame_img_conductor.pack_forget()

            if item == 'sennit':
                tree_view.column("#0", minwidth="{}".format(int(AGO.width_window / 3.072)))

                AFT.grid_out_col(sennit_elements)
            else:
                sennit_elements.grid_forget()

            if item == 'tu 16.k18-093-2007':
                AFT.grid_out_col_row_3(sennit_tu_16_k18_093_2007)
            else:
                sennit_tu_16_k18_093_2007.grid_forget()

            if item == 'tu4833-002-08558606-95':
                AFT.grid_out_col_row_3(sennit_tu4833_002_08558606_95)
            else:
                sennit_tu4833_002_08558606_95.grid_forget()

            if item == 'tube':
                AFT.grid_out_col_row_3(tube_elements)
            else:
                tube_elements.grid_forget()

            if item == 'gost 19034-82':
                AFT.grid_out_col(tube_standard)
            else:
                tube_standard.grid_forget()

            if item == 'cable':
                AFT.grid_out_col(cable_elements)
            else:
                cable_elements.grid_forget()

            if item == 'wire':
                AFT.grid_out_col_row_5(wire_elements)
            else:
                wire_elements.grid_forget()

            if item == 'tu 16-505.945-76':
                AFT.grid_out_col_row_3(wire_tu_16_505_945_76)
            else:
                wire_tu_16_505_945_76.grid_forget()

            if item == 'gost 6323-79':
                AFT.grid_out_col_row_3(wire_gost_6323_79)
            else:
                wire_gost_6323_79.grid_forget()

        tree_view.bind("<1>", clicks)
