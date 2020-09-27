# Prints out the elements for Cable, Sennit, SennitStandard, Tube, TubeStandard, Wire, WireStandard

from tkinter import *
from tkinter import ttk
from CablingGen.Element import Cable, Sennit, SennitStandard, Tube, TubeStandard, Wire, WireStandard


class Elements(Label, ttk.Combobox):
    def __init__(self, master=None, element=None):
        super().__init__(master)
        self.master = master

        if element == 'Cable':
            Cable.output_cable(self)
        elif element == 'Sennit':
            Sennit.output_sennit(self)
        elif element == 'TU 16.K18-093-2007':
            SennitStandard.output_sennit_standard(self, 'TU 16.K18-093-2007')
        elif element == 'TU4833-002-08558606-95':
            SennitStandard.output_sennit_standard(self, 'TU4833-002-08558606-95')
        elif element == 'Tube':
            Tube.output_tube(self)
        elif element == 'TubeStandard':
            TubeStandard.output_tube_standard(self)
        elif element == 'Wire':
            Wire.output_wire(self)
        elif element == 'TU 16-505.945-76':
            WireStandard.output_wire_standard(self, 'TU 16-505.945-76')
        elif element == 'GOST 6323-79':
            WireStandard.output_wire_standard(self, 'GOST 6323-79')
