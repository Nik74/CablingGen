# Create elements for tube standard

from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO, AuxiliaryFunctionsForLabel as AFL, \
    AuxuiliaryFunctionForRadiobutton as AFR
from CablingGen.Label import Labels
from CablingGen.Frames import FrameResult
from CablingGen import SQLite

_ = AGO.t.gettext


def output_tube_standard(frame, parent, standard, master):
    def selected_element(event):
        diameter_in = res_diameter_in.combobox.get()
        color = res_color.combobox.get()

        # Getting the name from the database
        diameter_in = SQLite.output_name_sen_and_tube_d_i(parent, AFL.del_symbol(diameter_in))
        color = SQLite.output_name_sen_and_tube_c(parent, AFL.del_symbol(color))

        result = AFL.intersection_2(diameter_in, color)

        frame_result = FrameResult.FrameResult(master=master)
        frame_result.grid(row=10, column=0, columnspan=4)

        AFR.output_radiobutton(parent, result, frame_result)

    res_color = Labels.Labels(frame=frame, row=0, col=0, pad_x=AGO.x_indent_40, message=_("Color:"), width=AGO.width_0,
                              parent=parent, element='color', standard=standard)  # Color

    res_diameter_in = Labels.Labels(frame=frame, row=0, col=3, pad_x=AGO.x_indent_20, message=_("Inner diameter (mm):"),
                                    width=AGO.width_3, parent=parent, element='diameter_in',
                                    standard=standard)  # Inner Diameter

    res_diameter_in.combobox.bind("<<ComboboxSelected>>", selected_element)
    res_color.combobox.bind("<<ComboboxSelected>>", selected_element)
