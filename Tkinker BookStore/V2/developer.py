from tkinter import *

def develop():
        window = Tk()
        window.title('Developer')
        window.geometry('300x190+525+200')
        window.resizable(0, 0)
        window.grid_rowconfigure(3, weight=1)

        l1 = Label(window,text="Rohit Jain",pady=30,font='Helvetica 18 bold underline')
        l1.grid(row=0,column=0,sticky="nsew")

        l1 = Label(window,text="SE-IT",padx=60,pady=5,font='Helvetica 10')
        l1.grid(row=1,column=0,sticky="nsew")

        l1 = Label(window,text="rohitrocks2801@gmail.com",padx=60,pady=5,font='Helvetica 10')
        l1.grid(row=2,column=0,sticky="nsew")

        l1 = Label(window,text="8850237301",font='Helvetica 10')
        l1.grid(row=3,column=0,sticky="nsew")

        window.mainloop()