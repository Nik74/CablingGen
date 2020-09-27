# Create elements for wire

from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO
from CablingGen.Label import Labels

_ = AGO.t.gettext


def output_wire_standard(frame, standard):
    frame.rowconfigure(2, {'minsize': 12.5})

    file = []

    if standard == 'GOST 6323-79':
        file.append(AGO.file_wire[0])
    elif standard == 'TU 16-505.945-76':
        file.append(AGO.file_wire[1])
    else:
        file = None

    """Labels.Labels(frame=frame, row=0, col=0, pad_x=AGO.x_indent_40, message=_("Section:"), width=AGO.width_0,
                  file=file, num=11)  # Section

    Labels.Labels(frame=frame, row=0, col=3, pad_x=AGO.x_indent_20, message=_("Wire thickness (mm):"),
                  width=AGO.width_3, file=file, num=3)  # Wire thickness

    Labels.Labels(frame=frame, row=3, col=0, pad_x=AGO.x_indent_40, message=_("Color:"), width=AGO.width_0,
                  file=file, num=5)  # Color

    Labels.Labels(frame=frame, row=3, col=3, pad_x=AGO.x_indent_20, message=_("Mark:"), width=AGO.width_3,
                  file=file, num=8)  # Mark"""
