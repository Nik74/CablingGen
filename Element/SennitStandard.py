# Create elements for sennit standard

from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO, AuxiliaryFunctionsForLabel as AFL,\
    AuxuiliaryFunctionForRadiobutton as AFR
from CablingGen.Label import Labels
from CablingGen.Frames import FrameResult
from CablingGen import SQLite

_ = AGO.t.gettext


def output_sennit_standard(frame, parent, standard, master):
    def selected_element(event):
        wall_thickness = res_wall_thickness.combobox.get()
        diameter_in = res_diameter_in.combobox.get()
        diameter_out = res_diameter_out.combobox.get()

        # Getting the name from the database
        wall_thickness = SQLite.output_name_sen_and_tube_w_t(parent, AFL.del_symbol(wall_thickness))
        diameter_in = SQLite.output_name_sen_and_tube_d_i(parent, AFL.del_symbol(diameter_in))
        diameter_out = SQLite.output_name_sen_and_tube_d_o(parent, AFL.del_symbol(diameter_out))

        result = AFL.intersection_3(wall_thickness, diameter_in, diameter_out)

        frame_result = FrameResult.FrameResult(master=master)
        frame_result.grid(row=10, column=0, columnspan=4)

        AFR.output_radiobutton(parent, result, frame_result)

    frame.rowconfigure(2, {'minsize': 12.5})

    res_wall_thickness = Labels.Labels(frame=frame, row=0, col=0, pad_x=AGO.x_indent_40,
                                       message=_("Wall thickness (mm):"), width=AGO.width_0, parent=parent,
                                       element='wall_thickness', standard=standard)  # Wall thickness

    res_diameter_in = Labels.Labels(frame=frame, row=0, col=3, pad_x=AGO.x_indent_20, message=_("Inner diameter (mm):"),
                                    width=AGO.width_3, parent=parent, element='diameter_in',
                                    standard=standard)  # Inner diameter

    res_diameter_out = Labels.Labels(frame=frame, row=3, col=0, pad_x=AGO.x_indent_40,
                                     message=_("Outer diameter (mm):"), width=AGO.width_0, parent=parent,
                                     element='diameter_out', standard=standard)  # Outer diameter

    res_wall_thickness.combobox.bind("<<ComboboxSelected>>", selected_element)
    res_diameter_in.combobox.bind("<<ComboboxSelected>>", selected_element)
    res_diameter_out.combobox.bind("<<ComboboxSelected>>", selected_element)
