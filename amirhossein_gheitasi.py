from  tkinter import *
from tkinter import StringVar
from tkinter.messagebox import showinfo

#from amirhossein_gheitasi import *
product_list=[]

def save_clik():
    #if name_validator(name.get()) and name_validator(quantity.get())and name_validator
     product = {"name": name.get(),"quantity": quantity.get(),"price": price.get()}
     product_list.append(product)
     print(product_list)
     name.set("")
     quantity.set(0)
     price.set(0)
     showinfo("save","product saved")
     count.set(len(product_list))

window=Tk()

window.title("product")
window.geometry("250x250")

#name
Label(window,text="name").place(x=20,y=20)
name=StringVar()
Entry(window,textvariable=name).place(x=80,y=20)

#quantity
Label(window,text="quantity").place(x=20,y=60)
quantity=IntVar(value=0)
Entry(window,textvariable=quantity).place(x=80,y=60)

#price
Label(window,text="price").place(x=20,y=100)
price=IntVar()
Entry(window,textvariable=price).place(x=80,y=100)

count=StringVar(value="count=0")
Label(window,textvariable=count,text="count").place(x=30,y=150)
Button(window,text="save",width=10,command=save_clik).place(x=100,y=150)

window.mainloop()
