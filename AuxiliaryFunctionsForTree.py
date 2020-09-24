from tkinter import ttk, BOTH


# Adding a list to the tree from a file
def add_list_to_tree_from_file(tree: ttk.Treeview) -> str:
    result = ''

    flag = 0

    parent = {}
    parent_count = {}

    f = open('./Material/Material.csv', 'r')

    for line in f:
        number = int(line[0: line.find(' '): 1])

        if '\n' in line[line.find(' ') + 1: len(line):]:  # If not the last element
            string = line[line.find(' ') + 1: len(line) - 1:]
        else:
            string = line[line.find(' ') + 1: len(line):]

        if number in parent.keys():
            parent[number] = string.lower()
            parent_count[number] = parent_count[number] + 1
        else:
            parent.update({number: string.lower()})
            parent_count.update({number: 0})

        if 0 == number:
            tree.insert('', parent_count[number], string.lower(),
                        text=string)
            result = string.lower()
        else:
            if flag > number:
                parent_count[flag] = 0

            tree.insert(parent[number - 1], parent_count[number], string.lower(),
                        text=string)

        flag = number

    f.close()

    return result


# Outputs frame with parameters pack(padx=10, pady=10, fill=BOTH)
def pack_out(frame):
    frame.pack(padx=10, pady=10, fill=BOTH)


# Outputs objects with parameters grid(row=2, columnspan=2, rowspan=3)
def grid_out_col_row(obj):
    obj.grid(row=2, columnspan=2, rowspan=3)


# Outputs objects with parameters grid(row=2, columnspan=2)
def grid_out_col(obj):
    obj.grid(row=2, columnspan=2)
