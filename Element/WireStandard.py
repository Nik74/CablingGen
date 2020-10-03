# Create elements for wire

from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO, AuxiliaryFunctionsForLabel as AFL, \
    AuxuiliaryFunctionForRadiobutton as AFR
from CablingGen.Label import Labels
from CablingGen.Frames import FrameResult
from CablingGen import SQLite

_ = AGO.t.gettext


def output_wire_standard(frame, parent, standard, master):
    def selected_element(event):
        wire_thickness = res_wire_thickness.combobox.get()
        color = res_color.combobox.get()
        mark = res_mark.combobox.get()
        section = res_section.combobox.get()

        # Getting the name from the database
        wire_thickness = SQLite.output_name_wire_w_t(parent, AFL.del_symbol(wire_thickness))
        color = SQLite.output_name_wire_c(parent, AFL.del_symbol(color))
        mark = SQLite.output_name_wire_m(parent, AFL.del_symbol(mark))
        section = SQLite.output_name_wire_sec(parent, AFL.del_symbol(section))

        result = AFL.intersection_4(wire_thickness, color, mark, section)

        frame_result = FrameResult.FrameResult(master=master)
        frame_result.grid(row=10, column=0, columnspan=4)

        AFR.output_radiobutton(parent, result, frame_result)

    frame.rowconfigure(2, {'minsize': 12.5})

    res_section = Labels.Labels(frame=frame, row=0, col=0, pad_x=AGO.x_indent_40, message=_("Section:"),
                                width=AGO.width_0, parent=parent, element='section', standard=standard)  # Section

    res_wire_thickness = Labels.Labels(frame=frame, row=0, col=3, pad_x=AGO.x_indent_20,
                                       message=_("Wire thickness (mm):"), width=AGO.width_3, parent=parent,
                                       element='wire_thickness', standard=standard)  # Wire thickness

    res_color = Labels.Labels(frame=frame, row=3, col=0, pad_x=AGO.x_indent_40, message=_("Color:"), width=AGO.width_0,
                              parent=parent, element='color', standard=standard)  # Color

    res_mark = Labels.Labels(frame=frame, row=3, col=3, pad_x=AGO.x_indent_20, message=_("Mark:"), width=AGO.width_3,
                             parent=parent, element='mark', standard=standard)  # Mark

    res_wire_thickness.combobox.bind("<<ComboboxSelected>>", selected_element)
    res_color.combobox.bind("<<ComboboxSelected>>", selected_element)
    res_mark.combobox.bind("<<ComboboxSelected>>", selected_element)
    res_section.combobox.bind("<<ComboboxSelected>>", selected_element)
