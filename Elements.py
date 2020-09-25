# Prints out the elements for Cable, Sennit, SennitStandard, Tube, TubeStandard, Wire, WireStandard

from tkinter import *
from tkinter import ttk
from CablingGen import Cable, Sennit, SennitStandard, Tube, TubeStandard, Wire, WireStandard


class Elements(Label, ttk.Combobox):
    def __init__(self, master=None, element=None):
        super().__init__(master)
        self.master = master

        if element == 'Cable':
            Cable.output_cable(self)
        elif element == 'Sennit':
            Sennit.output_sennit(self)
        elif element == "SennitStandard":
            SennitStandard.output_sennit_standard(self)
        elif element == "Tube":
            Tube.output_tube(self)
        elif element == "TubeStandard":
            TubeStandard.output_tube_standard(self)
        elif element == "Wire":
            Wire.output_wire(self)
        elif element == "WireStandard":
            WireStandard.output_wire_standard(self)
