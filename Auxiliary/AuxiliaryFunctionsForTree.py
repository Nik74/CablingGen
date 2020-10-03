from tkinter import ttk, BOTH
from CablingGen import SQLite


# Adding a list to the tree from a file
def add_list_to_tree_from_file(tree: ttk.Treeview) -> str:
    result = ''

    for line in SQLite.sel_from_material():
        if line[0] == 1:
            result = line[1].lower()

        tree.insert(line[2].lower(), line[3], line[1].lower(), text=line[1])

    return result


# Outputs frame with parameters pack(padx=10, pady=10, fill=BOTH)
def pack_out(frame):
    frame.pack(padx=10, pady=10, fill=BOTH)


# Outputs objects with parameters grid(row=2, columnspan=2, rowspan=3)
def grid_out_col_row_3(obj):
    obj.grid(row=2, columnspan=2, rowspan=3)


# Outputs objects with parameters grid(row=2, columnspan=2)
def grid_out_col(obj):
    obj.grid(row=2, columnspan=2)


# Outputs objects with parameters grid(row=2, columnspan=2, rowspan=3)
def grid_out_col_row_5(obj):
    obj.grid(row=2, columnspan=2, rowspan=5)
