# Create and output radiobutton

from tkinter import *
from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO
from CablingGen.Template_spl import Template


def output_radiobutton(parent, element, frame_result):
    canvas_result = Canvas(frame_result)
    frame_canvas = Frame(canvas_result)
    scrollbar_result = Scrollbar(frame_result, orient='vertical')

    scrollbar_result['command'] = canvas_result.yview
    canvas_result.configure(yscrollcommand=scrollbar_result.set)

    canvas_result.place(y="0", width="{}".format(int(AGO.width_frame_result / 1.03)),
                        height="{}".format(int(AGO.height_frame_result / 1.03)))
    scrollbar_result.place(x="{}".format(int(AGO.width_frame_result / 1.055)), y="0",
                           height="{}".format(int(AGO.height_frame_result / 1.003)))
    canvas_result.create_window((0, 0), window=frame_canvas, anchor='nw')

    def conf(event):
        canvas_result.configure(scrollregion=canvas_result.bbox('all'))

    def select(event):
        Template.create_spl(parent, res.get())
        sys.exit()

    frame_canvas.bind('<Configure>', conf)

    res = StringVar()

    k = 0

    for i in element:
        result_rad = Radiobutton(frame_canvas, text=i, value=i, variable=res, state=NORMAL)
        result_rad.grid(row=k, column=0, sticky='w')
        result_rad.bind('<Double-Button-1>', select)
        k += 1
