# Create elements for tube

from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO
from CablingGen.Label import Labels

_ = AGO.t.gettext


def output_tube(frame):
    frame.rowconfigure(2, {'minsize': 12.5})

    """Labels.Labels(frame=frame, row=0, col=0, pad_x=AGO.x_indent_40, message=_("Standard:"), width=AGO.width_0,
                  file=AGO.file_tube, num=13)  # Standard

    Labels.Labels(frame=frame, row=0, col=3, pad_x=AGO.x_indent_20, message=_("Inner diameter (mm):"),
                  width=AGO.width_3, file=AGO.file_tube, num=6)  # Inner Diameter

    Labels.Labels(frame=frame, row=3, col=0, pad_x=AGO.x_indent_40, message=_("Color:"), width=AGO.width_0,
                  file=AGO.file_tube, num=8)  # Color"""
