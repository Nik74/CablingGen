# Create elements for sennit

from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO
from CablingGen.Label import Labels

_ = AGO.t.gettext

file = AGO.file_sennit


def output_sennit(frame):
    Labels.Labels(frame=frame, row=0, col=0, pad_x=AGO.x_indent_40, message=_("Standard:"),
                  width=AGO.width_0, file=file, num=11)  # Standard

    Labels.Labels(frame=frame, row=0, col=3, pad_x=AGO.x_indent_20, message=_("Inner diameter (mm):"),
                  width=AGO.width_3, file=file, num=6)  # Inner Diameter
