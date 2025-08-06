from tkinter import *
#import sqlite3
from tkinter import messagebox
from tkinter import ttk


lesson_list=[]
# 5
def reset_form():
    Code.set(0)
    Title.set("")
    Teacher.set("")
    Class_number.set(0)
    Unit.set(0)


# 6
def save_click():
    lesson={
        "Code":Code.get(),
        "Title":Title.get(),
        "Teacher":Teacher.get(),
        "Class_Number":Class_number.get(),
        "Unit":Unit.get()
    }
    lesson_list.append(lesson)
    messagebox.showinfo("save",f"Successfuly saved!\n{lesson}")
    reset_form()
    table.insert("",END,values=tuple(lesson.values()))

# HomeWork
def edit_click():
    pass
def remove_click():
    #file_id = entry_id.get()
   # if not file_id.insdigit():
      #  return
    table_row=table.focus()
    selected = table.item(table_row)["values"]
    Code.set(selected[0])
    Title.set(selected[1])
    Teacher.set(selected[2])
    Class_number.set(selected[3])
    Unit.set(selected[4])

# 7
def table_select(event):
    table_row=table.focus()
    selected=table.item(table_row)["values"]
    Code.set(selected[0])
    Title.set(selected[1])
    Teacher.set(selected[2])
    Class_number.set(selected[3])
    Unit.set(selected[4])
# 0
window = Tk()
window.title("Lesson Information")
window.geometry("700x360")
window.resizable(False, False)


# 1
# Code
Code = IntVar()
Label(window,text="Code:").place(x=20,y=60)
Entry(window, textvariable=Code).place(x=100,y=60)
# Title
Title=StringVar()
Label(window,text="Title:").place(x=20,y=110)
Entry(window,textvariable=Title).place(x=100,y=110)
# Teacher
Teacher=StringVar()
Label(window,text="Teacher:").place(x=20,y=160)
Entry(window,textvariable=Teacher).place(x=100,y=160)
# Class Number
Class_number=IntVar()
Label(window,text="Class number:").place(x=20,y=210)
Entry(window,textvariable=Class_number).place(x=100,y=210)
# Unit
Unit=IntVar()
Label(window,text="Unit:").place(x=20,y=260)
Entry(window,textvariable=Unit).place(x=100,y=260)


# 2
# Buttons (Save-Edit-Remove)
Button(window,text="save",command=save_click,width=7).place(x=20,y=320)
Button(window,text="edit",command=edit_click,width=7).place(x=95,y=320)
Button(window,text="remove",command=remove_click,width=7).place(x=170,y=320)

# 3
#Search Title
title_search=StringVar()
Label(window,text="Title search:").place(x=250,y=20)
Entry(window,textvariable=title_search).place(x=320,y=20)
# Search Teacher
teacher_search=StringVar()
Label(window,text="Teacher search:").place(x=465,y=20)
Entry(window,textvariable=teacher_search).place(x=555,y=20)

# 4
# Table
table = ttk.Treeview(window, height=13,columns=(1,2,3,4,5),show="headings")
table.column(1, width=70)
table.column(2, width=90)
table.column(3, width=90)
table.column(4, width=100)
table.column(5, width=80)

table.heading(1,text="Code")
table.heading(2,text="Title")
table.heading(3,text="Teacher")
table.heading(4,text="Class Number")
table.heading(5,text="Unit")
# TreeviewSelect

# bind--> table_select
table.bind("<<TreeviewSelect>>", table_select)
table.place(x=250,y=60)





window.mainloop()