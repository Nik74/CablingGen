from CablingGen import SQLite


# Auxiliary function. Returns column values from SQLite by parent
def read_file(parent, element, standard) -> list:
    if (parent == 'sennit') or (parent == 'tube'):
        if element == 'standard':
            return SQLite.sel_standard_from_sennit_and_tube([parent, ])
        elif element == 'diameter_in':
            return SQLite.sel_diameter_in_from_sennit_and_tube(parent, standard)
        elif element == 'wall_thickness':
            return SQLite.sel_wall_thickness_from_sennit_and_tube(parent, standard)
        elif element == 'diameter_out':
            return SQLite.sel_diameter_out_from_sennit_and_tube(parent, standard)
        elif element == 'color':
            return SQLite.sel_color_from_sennit_and_tube(parent, standard)
    elif parent == 'wire':
        if element == 'standard':
            return SQLite.sel_standard_from_wire(parent)
        elif element == 'wire_thickness':
            return SQLite.sel_wire_thickness_from_wire(parent, standard)
        elif element == 'color':
            return SQLite.sel_color_from_wire(parent, standard)
        elif element == 'mark':
            return SQLite.sel_brand_from_wire(parent, standard)
        elif element == 'section':
            return SQLite.sel_section_from_wire(parent, standard)


# removes '{' and '}' from the string
def del_symbol(element):
    if '{' in element:
        return element[1:len(element) - 1:]

    return element


# Returns the intersection of two lists
def intersection_2(element_1, element_2) -> list:
    if (not element_1) and element_2:
        return element_2
    elif (not element_2) and element_1:
        return element_1
    elif element_1 and element_2:
        return list(set(element_1) & set(element_2))


# Returns the intersection of three lists
def intersection_3(element_1, element_2, element_3) -> list:
    if (not element_1) and (not element_2) and element_3:
        return element_3
    elif (not element_1) and (not element_3) and element_2:
        return element_2
    elif (not element_2) and (not element_3) and element_1:
        return element_1
    elif (not element_1) and element_2 and element_3:
        return list(set(element_2) & set(element_3))
    elif element_1 and (not element_2) and element_3:
        return list(set(element_1) & set(element_3))
    elif element_1 and element_2 and (not element_3):
        return list(set(element_1) & set(element_2))
    elif element_1 and element_2 and element_3:
        return list(set(element_1) & set(element_2) & set(element_3))


# Returns the intersection of four lists
def intersection_4(element_1, element_2, element_3, element_4) -> list:
    if element_1 and (not element_2) and (not element_3) and (not element_4):
        return element_1
    elif (not element_1) and element_2 and (not element_3) and (not element_4):
        return element_2
    elif (not element_1) and (not element_2) and element_3 and (not element_4):
        return element_3
    elif (not element_1) and (not element_2) and (not element_3) and element_4:
        return element_4
    elif element_1 and element_2 and (not element_3) and (not element_4):
        return list(set(element_1) & set(element_2))
    elif element_1 and (not element_2) and element_3 and (not element_4):
        return list(set(element_1) & set(element_3))
    elif element_1 and (not element_2) and (not element_3) and element_4:
        return list(set(element_1) & set(element_4))
    elif (not element_1) and element_2 and element_3 and (not element_4):
        return list(set(element_2) & set(element_3))
    elif (not element_1) and element_2 and (not element_3) and element_4:
        return list(set(element_2) & set(element_4))
    elif (not element_1) and (not element_2) and element_3 and element_4:
        return list(set(element_3) & set(element_4))
    elif element_1 and element_2 and element_3 and (not element_4):
        return list(set(element_1) & set(element_2) & set(element_3))
    elif element_1 and element_2 and (not element_3) and element_4:
        return list(set(element_1) & set(element_2) & set(element_4))
    elif element_1 and (not element_2) and element_3 and element_4:
        return list(set(element_1) & set(element_3) & set(element_4))
    elif (not element_1) and element_2 and element_3 and element_4:
        return list(set(element_2) & set(element_3) & set(element_4))
    elif element_1 and element_2 and element_3 and element_4:
        return list(set(element_1) & set(element_2) & set(element_3) & set(element_4))


# Returns the intersection of five lists
def intersection_5(element_1, element_2, element_3, element_4, element_5) -> list:
    if element_1 and (not element_2) and (not element_3) and (not element_4) and (not element_5):
        return element_1
    elif (not element_1) and element_2 and (not element_3) and (not element_4) and (not element_5):
        return element_2
    elif (not element_1) and (not element_2) and element_3 and (not element_4) and (not element_5):
        return element_3
    elif (not element_1) and (not element_2) and (not element_3) and element_4 and (not element_5):
        return element_4
    elif (not element_1) and (not element_2) and (not element_3) and (not element_4) and element_5:
        return element_5
    elif element_1 and element_2 and (not element_3) and (not element_4) and (not element_5):
        return list(set(element_1) & set(element_2))
    elif element_1 and (not element_2) and element_3 and (not element_4) and (not element_5):
        return list(set(element_1) & set(element_3))
    elif element_1 and (not element_2) and (not element_3) and element_4 and (not element_5):
        return list(set(element_1) & set(element_4))
    elif element_1 and (not element_2) and (not element_3) and (not element_4) and element_5:
        return list(set(element_1) & set(element_5))
    elif (not element_1) and element_2 and element_3 and (not element_4) and (not element_5):
        return list(set(element_2) & set(element_3))
    elif (not element_1) and element_2 and (not element_3) and element_4 and (not element_5):
        return list(set(element_2) & set(element_4))
    elif (not element_1) and element_2 and (not element_3) and (not element_4) and element_5:
        return list(set(element_2) & set(element_5))
    elif (not element_1) and (not element_2) and element_3 and element_4 and (not element_5):
        return list(set(element_3) & set(element_4))
    elif (not element_1) and (not element_2) and element_3 and (not element_4) and element_5:
        return list(set(element_3) & set(element_5))
    elif (not element_1) and (not element_2) and (not element_3) and element_4 and element_5:
        return list(set(element_4) & set(element_5))
    elif element_1 and element_2 and element_3 and (not element_4) and (not element_5):
        return list(set(element_1) & set(element_2) & set(element_3))
    elif element_1 and element_2 and (not element_3) and element_4 and (not element_5):
        return list(set(element_1) & set(element_2) & set(element_4))
    elif element_1 and element_2 and (not element_3) and (not element_4) and element_5:
        return list(set(element_1) & set(element_2) & set(element_5))
    elif element_1 and (not element_2) and element_3 and element_4 and (not element_5):
        return list(set(element_1) & set(element_3) & set(element_4))
    elif element_1 and (not element_2) and element_3 and (not element_4) and element_5:
        return list(set(element_1) & set(element_3) & set(element_5))
    elif element_1 and (not element_2) and (not element_3) and element_4 and element_5:
        return list(set(element_1) & set(element_4) & set(element_5))
    elif (not element_1) and element_2 and element_3 and element_4 and (not element_5):
        return list(set(element_2) & set(element_3) & set(element_4))
    elif (not element_1) and element_2 and element_3 and (not element_4) and element_5:
        return list(set(element_2) & set(element_3) & set(element_5))
    elif (not element_1) and element_2 and (not element_3) and element_4 and element_5:
        return list(set(element_2) & set(element_4) & set(element_5))
    elif (not element_1) and (not element_2) and element_3 and element_4 and element_5:
        return list(set(element_3) & set(element_4) & set(element_5))
    elif element_1 and element_2 and element_3 and element_4 and (not element_5):
        return list(set(element_1) & set(element_2) & set(element_3) & set(element_4))
    elif element_1 and element_2 and element_3 and (not element_4) and element_5:
        return list(set(element_1) & set(element_2) & set(element_3) & set(element_5))
    elif element_1 and element_2 and (not element_3) and element_4 and element_5:
        return list(set(element_1) & set(element_2) & set(element_4) & set(element_5))
    elif element_1 and (not element_2) and element_3 and element_4 and element_5:
        return list(set(element_1) & set(element_3) & set(element_4) & set(element_5))
    elif (not element_1) and element_2 and element_3 and element_4 and element_5:
        return list(set(element_2) & set(element_3) & set(element_4) & set(element_5))
    elif element_1 and element_2 and element_3 and element_4 and element_5:
        return list(set(element_1) & set(element_2) & set(element_3) & set(element_4) & set(element_5))
