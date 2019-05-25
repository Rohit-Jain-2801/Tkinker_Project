import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import backend as bk

class MultiColumnListbox(object):
    # print('B')
    def run(self,list0=''):
        # print('C')   
        global dlist
        if list0=='':
            dlist = bk.view()
        else:
            dlist = list0
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        # container = ttk.Frame(window)
        # container.pack(fill='both', expand=True)
        self.tree = ttk.Treeview(columns=header, show="headings")
        self.tree.grid(row=3,column=0,rowspan=6,columnspan=4, sticky='nsew')
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        vsb.grid(row=3,column=5,rowspan=6, sticky='nsw')
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        hsb.grid(row=9,column=0,columnspan=4, sticky='new')
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        # container.grid_columnconfigure(0, weight=1)
        # container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in header:
            self.tree.heading(col, text=col, command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col, width=tkFont.Font().measure(col.title()))

        for item in dlist:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(header[ix],width=None)<col_w:
                    self.tree.column(header[ix], width=col_w)

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    # print(tree.get_children(''))
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    # tree.set command:
        # set(item, column=None, value=None)
        # With one argument, returns a dictionary of column/value pairs for the specified item.
        # With two arguments, returns the current value of the specified column.
        # With three arguments, sets the value of given column in given item to the specified value.
    # print(data)
    # if the data to be sorted is numeric change to float
    # data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
        # tree.move command:
        #     move(item, parent, index)
        #     Moves item to position index in parent’s list of children.
        #     It is illegal to move an item under one of its descendants.
        #     If index is less than or equal to zero, item is moved to the beginning;
        #     if greater than or equal to the number of children, it is moved to the end.
        #     If item was detached it is reattached.
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))

def clear(tree):
    tree.delete(*tree.get_children())

# print('A')
header = ['ID', 'Title', 'Author', 'Year', 'ISBN']