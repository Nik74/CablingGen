# Create elements for sennit standard

from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO
from CablingGen.Label import Labels

_ = AGO.t.gettext


def output_sennit_standard(frame, standard):
    frame.rowconfigure(2, {'minsize': 12.5})

    file = []

    if standard == 'TU 16.K18-093-2007':
        file.append(AGO.file_sennit[0])
    elif standard == 'TU4833-002-08558606-95':
        file.append(AGO.file_sennit[1])
    else:
        file = None

    """Labels.Labels(frame=frame, row=0, col=0, pad_x=AGO.x_indent_40, message=_("Wall thickness (mm):"),
                  width=AGO.width_0, file=file, num=3)  # Wall thickness

    Labels.Labels(frame=frame, row=0, col=3, pad_x=AGO.x_indent_20, message=_("Inner diameter (mm):"),
                  width=AGO.width_3, file=file, num=6)  # Inner diameter

    Labels.Labels(frame=frame, row=3, col=0, pad_x=AGO.x_indent_40, message=_("Outer diameter (mm):"),
                  width=AGO.width_0, file=file, num=7)  # Outer diameter"""
