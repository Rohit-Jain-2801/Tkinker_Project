from tkinter import *

def about():
        window = Tk()
        window.title('About')
        window.geometry('300x190+525+200')
        window.resizable(0, 0)
        window.grid_rowconfigure(3, weight=1)

        d1 = 'BookStore is a application based on Tkinker.'
        d2 = 'All the details are stored in a local sqlite3 database.'
        d3 = 'All rights reserved.'

        l1 = Label(window,text=d1,pady=30,font='Helvetica 10')
        l2 = Label(window,text=d2,font='Helvetica 10')
        l3 = Label(window,text=d3,pady=30,font='Helvetica 10')
        l1.pack(fill=X)
        l2.pack(fill=X)
        l3.pack(fill=X)

        window.mainloop()