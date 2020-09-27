# Create elements for wire

from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO
from CablingGen.Label import Labels

_ = AGO.t.gettext


def output_wire(frame):
    frame.rowconfigure(2, {'minsize': 12.5})
    frame.rowconfigure(5, {'minsize': 12.5})

    """Labels.Labels(frame=frame, row=0, col=0, pad_x=AGO.x_indent_40, message=_("Standard:"), width=AGO.width_0,
                  file=AGO.file_wire, num=12)  # Standard

    Labels.Labels(frame=frame, row=0, col=3, pad_x=AGO.x_indent_20, message=_("Wire thickness (mm):"),
                  width=AGO.width_3, file=AGO.file_wire, num=3)  # Wire thickness

    Labels.Labels(frame=frame, row=3, col=0, pad_x=AGO.x_indent_40, message=_("Color:"), width=AGO.width_0,
                  file=AGO.file_wire, num=5)  # Color

    Labels.Labels(frame=frame, row=3, col=3, pad_x=AGO.x_indent_20, message=_("Mark:"), width=AGO.width_3,
                  file=AGO.file_wire, num=8)  # Mark

    Labels.Labels(frame=frame, row=6, col=0, pad_x=AGO.x_indent_40, message=_("Section:"), width=AGO.width_0,
                  file=AGO.file_wire, num=11)  # Section"""
