# Create template .spl

from CablingGen.Template_spl import TemplateForSennit, TemplateForTube, TemplateForWire
from CablingGen.Auxiliary import AuxiliaryFunctionsForLabel as AFL


def create_spl(parent, name):
    name = AFL.del_symbol(name)

    if parent == 'sennit':
        TemplateForSennit.template_sennit(parent, name)
    elif parent == 'tube':
        TemplateForTube.template_tube(parent, name)
    elif parent == 'wire':
        TemplateForWire.template_wire(parent, name)
