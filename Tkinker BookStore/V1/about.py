from tkinter import *
import tkinter as tk
from TkTreectrl import MultiListbox
import backend as bk

def select_cmd(selected):
    print ('Selected items:', selected)

window = Tk()
window.title('Book Galary')
window.geometry('443x600+450+25')
window.resizable(0, 0)
window.grid_rowconfigure(3, weight=1)

mlb = MultiListbox(window)
# mlb.pack(side='top', fill='both', expand=1)
mlb.grid(row=3,column=0,rowspan=6,columnspan=4,sticky="wnse")
mlb.focus_set()   
mlb.configure(selectcmd=select_cmd, selectmode='extended')
mlb.config(columns=('Id', 'Title','Author','Year','ISBN'))
for row in bk.view():
    mlb.insert('end',*map(unicode,row))

window.mainloop()
# list1 = Listbox(window,width=70)
# list1.grid(row=3,column=0,rowspan=6,columnspan=4,sticky="wnse")
# sb1 = Scrollbar(window)
# sb1.grid(row=3,column=5,rowspan=6,sticky="wns")
# sb2 = Scrollbar(window)
# sb2.grid(row=9,column=0,columnspan=4,sticky="nwe")
# list1.configure(yscrollcommand=sb1.set,xscrollcommand=sb2.set)
# sb1.configure(command=list1.yview)
# sb2.configure(command=list1.xview,orient='horizontal')
# list1.bind('<<ListboxSelect>>',get_selected_row)