# Create elements for sennit

from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO, AuxiliaryFunctionsForLabel as AFL, \
    AuxuiliaryFunctionForRadiobutton as AFR
from CablingGen.Label import Labels
from CablingGen.Frames import FrameResult
from CablingGen import SQLite

_ = AGO.t.gettext


def output_sennit(frame, element, master):
    def selected_element(event):
        standard = res_standard.combobox.get()
        diameter_in = res_diameter_in.combobox.get()

        # Getting the name from the database
        standard = SQLite.output_name_sen_and_tube_s(element, AFL.del_symbol(standard))
        diameter_in = SQLite.output_name_sen_and_tube_d_i(element, AFL.del_symbol(diameter_in))

        result = AFL.intersection_2(standard, diameter_in)

        frame_result = FrameResult.FrameResult(master=master)
        frame_result.grid(row=10, column=0, columnspan=4)

        AFR.output_radiobutton(element, result, frame_result)

    res_standard = Labels.Labels(frame=frame, row=0, col=0, pad_x=AGO.x_indent_40, message=_("Standard:"),
                                 width=AGO.width_0, parent=element, element='standard')  # Standard

    res_diameter_in = Labels.Labels(frame=frame, row=0, col=3, pad_x=AGO.x_indent_20, message=_("Inner diameter (mm):"),
                                    width=AGO.width_3, parent=element, element='diameter_in')  # Inner Diameter

    res_standard.combobox.bind("<<ComboboxSelected>>", selected_element)
    res_diameter_in.combobox.bind("<<ComboboxSelected>>", selected_element)
