# Create elements for cable

from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO
from CablingGen.Label import Labels

_ = AGO.t.gettext


def output_cable(frame):
    """Labels.Labels(frame=frame, row=0, col=0, pad_x=AGO.x_indent_40, message=_("Standard:"),
                  width=AGO.width_0, file=None, num=None)  # Standard

    Labels.Labels(frame=frame, row=0, col=3, pad_x=AGO.x_indent_20, message=_("Density of the cable:"),
                  width=AGO.width_3, file=None, num=None)  # Density"""
