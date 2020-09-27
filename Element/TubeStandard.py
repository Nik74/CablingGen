# Create elements for tube standard

from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO
from CablingGen.Label import Labels

_ = AGO.t.gettext


def output_tube_standard(frame):
    """Labels.Labels(frame=frame, row=0, col=0, pad_x=AGO.x_indent_40, message=_("Color:"), width=AGO.width_0,
                  file=AGO.file_tube, num=8)  # Color

    Labels.Labels(frame=frame, row=0, col=3, pad_x=AGO.x_indent_20, message=_("Inner diameter (mm):"),
                  width=AGO.width_3, file=AGO.file_tube, num=6)  # Inner Diameter"""
