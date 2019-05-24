from tkinter import *
import tkinter.messagebox as tkmb
import backend as bk
from multilist import *
import developer,about
from pdf_creator import *

window = Tk()
window.title('Book Galary')
window.geometry('443x600+450+25')
window.resizable(0, 0)
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure(3, weight=1)

def save_pdf():
        try:
                create_pdf(bk.view())
        except Exception as err:
                tkmb.showwarning('Records',err,parent=window)
        else:
                tkmb.showinfo('Successful','Pdf is successfully created!',parent=window)

def delete_inputs():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)

def get_selected_row(event):
        try:
                global selected_tuple
                selected_tuple=list1.tree.item(list1.tree.focus())['values']
                delete_inputs()
                e1.insert(END,selected_tuple[1])
                e2.insert(END,selected_tuple[2])
                e3.insert(END,selected_tuple[3])
                e4.insert(END,selected_tuple[4])
        except IndexError:
                pass

def view_command():
        try:
                clear(list1.tree)
        except:
                pass
        try:
                list1.run()
                status['text']='STATUS: Running\t\t\t\tTotal Rows: {}'.format(len(bk.view()))
                list1.tree.bind('<Button-1>',get_selected_row)
        except Exception as err:
                tkmb.showwarning('Records',err,parent=window)

def search_command():
        try:
                clear(list1.tree)
        except:
                pass
        try:
                rows = bk.search(title.get(),author.get(),year.get(),isbn.get())
                list1.run(list0=rows)
                list1.tree.bind('<Button-1>',get_selected_row)
        except Exception as err:
                tkmb.showwarning('Records',err,parent=window)
        finally:
                status['text']='STATUS: Running\t\t\t\tTotal Rows: {}'.format(len(rows))

def add_command():
        try:
                bk.insert(title.get(),author.get(),year.get(),isbn.get())
                delete_inputs()
                tkmb.showinfo('Successful','An entry is added to database successfully!',parent=window)
                view_command()
        except:
                tkmb.showerror('Error','Please check the input data!',parent=window)

def delete_command():
        if list1.tree.item(list1.tree.focus())==():
                tkmb.showwarning('Failed','No Entry Selected!',parent=window)
        else:
                # print(list1.tree.item(list1.tree.focus())['values'])
                if tkmb.askquestion('Delete Confirmation','Are you sure?',parent=window)=="yes":
                        bk.delete(list1.tree.item(list1.tree.focus())['values'][0])
                        delete_inputs()
                        tkmb.showinfo('Successful','An entry is deleted from database successfully!',parent=window)
                        view_command()

def update_command():
        if list1.tree.item(list1.tree.focus())==():
                tkmb.showwarning('Failed','No Entry Selected!',parent=window)
        else:
                try:
                        bk.update(list1.tree.item(list1.tree.focus())['values'][0],title.get(),author.get(),year.get(),isbn.get())
                        delete_inputs()
                        tkmb.showinfo('Successful','An entry is updated successfully!',parent=window)
                        view_command()
                except:
                        tkmb.showerror('Error','Updation Failed!',parent=window)

menu = Menu(window)
window.config(menu=menu)

submenu1 = Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="Save as PDF",command=save_pdf)
submenu1.add_separator()
submenu1.add_command(label="Exit",command=quit)

submenu2 = Menu(menu,tearoff=0)
menu.add_cascade(label="Help",menu=submenu2)
submenu2.add_command(label="About",command=about.about)
submenu2.add_command(label="Contact",command=developer.develop)

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)
title = StringVar()
e1 = Entry(window,textvariable=title)
e1.grid(row=0,column=1,sticky="we")

l1 = Label(window,text="Author")
l1.grid(row=0,column=2)
author = StringVar()
e2 = Entry(window,textvariable=author)
e2.grid(row=0,column=3,sticky="we")

l1 = Label(window,text="Year")
l1.grid(row=1,column=0)
year = StringVar()
e3 = Entry(window,textvariable=year)
e3.grid(row=1,column=1,sticky="we")

l1 = Label(window,text="ISBN")
l1.grid(row=1,column=2)
isbn = StringVar()
e4 = Entry(window,textvariable=isbn)
e4.grid(row=1,column=3,sticky="we")

frame = Frame(window)
frame.grid(row=2,columnspan=4,sticky="we")
b1 = Button(frame,text="View All",command=view_command)
b1.pack(side=LEFT,fill=X,expand=1)
b2 = Button(frame,text="Add",command=add_command)
b2.pack(side=LEFT,fill=X,expand=1)
b3 = Button(frame,text="Update",command=update_command)
b3.pack(side=LEFT,fill=X,expand=1)
b4 = Button(frame,text="Delete",command=delete_command)
b4.pack(side=LEFT,fill=X,expand=1)
b5 = Button(frame,text="Search",command=search_command)
b5.pack(side=LEFT,fill=X,expand=1)

list1 = MultiColumnListbox()

status = Label(window,text="STATUS: Running",bd=1,relief=SUNKEN,anchor=W)
status.grid(row=10,columnspan=6,sticky="we")

window.mainloop()