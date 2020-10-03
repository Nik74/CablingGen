# Prints out the elements for Cable, Sennit, SennitStandard, Tube, TubeStandard, Wire, WireStandard

from tkinter import *
from tkinter import ttk
from CablingGen.Element import Cable, Sennit, SennitStandard, Tube, TubeStandard, Wire, WireStandard
from CablingGen.Auxiliary import AuxiliaryGlobalObject as AGO

_ = AGO.t.gettext


class Elements(Label, ttk.Combobox):
    def __init__(self, master=None, element=None):
        super().__init__(master)
        self.master = master

        if element == 'Cable':
            Cable.output_cable(self, element.lower())
        elif element == 'Sennit':
            Sennit.output_sennit(self, element.lower(), master)
        elif element == _('TU16.K18-093-2007'):
            SennitStandard.output_sennit_standard(self, 'sennit', element, master)
        elif element == _('TU 4833-002-08558606-95'):
            SennitStandard.output_sennit_standard(self, 'sennit', element, master)
        elif element == 'Tube':
            Tube.output_tube(self, element.lower(), master)
        elif element == _('GOST 19034-82'):
            TubeStandard.output_tube_standard(self, 'tube', element, master)
        elif element == 'Wire':
            Wire.output_wire(self, element.lower(), master)
        elif element == _('TU 16-505.945-76'):
            WireStandard.output_wire_standard(self, 'wire', element, master)
        elif element == _('GOST 6323-79'):
            WireStandard.output_wire_standard(self, 'wire', element, master)
