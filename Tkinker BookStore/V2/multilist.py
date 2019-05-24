import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import backend as bk

class MultiColumnListbox(object):
    # print('B')
    def run(self,list0=''):
        # print('C')    
        global car_list
        if list0=='':
            car_list = bk.view()
        else:
            car_list = list0
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        # container = ttk.Frame(window)
        # container.pack(fill='both', expand=True)
        self.tree = ttk.Treeview(columns=header, show="headings")
        self.tree.grid(row=3,column=0,rowspan=6,columnspan=4, sticky='nsew')
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        vsb.grid(row=3,column=5,rowspan=6, sticky='ns')
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        hsb.grid(row=9,column=0,columnspan=4, sticky='ew')
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        # container.grid_columnconfigure(0, weight=1)
        # container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in header:
            self.tree.heading(col, text=col, command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col, width=tkFont.Font().measure(col.title()))

        for item in car_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(header[ix],width=None)<col_w:
                    self.tree.column(header[ix], width=col_w)

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))

def clear(tree):
    tree.delete(*tree.get_children())

# print('A')
header = ['ID', 'Title', 'Author', 'Year', 'ISBN']