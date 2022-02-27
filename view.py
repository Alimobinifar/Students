from cgitb import reset, text
from dataclasses import dataclass
from stat import ST_UID
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from turtle import tracer
from controller import show_studens,create_student,remove_student,update_student_controller
#1
root=Tk()
root.title("سامانه جامع مدیریت")
root.geometry('1200x700')
welcome_lbl = Label(root, text="به سیستم جامع مدیریت دانش جویان دانشگاه مشهد خوش آمدید", font=("titr",20,"bold")).place(x=300,y=20)
#2
name = StringVar()
family = StringVar()
phone = StringVar()
address = StringVar()

name_entry = Entry(root, font=("arial",20,"bold"),textvariable=name,justify="right").place(x=250,y=90, height=40,width=250)
# name = Entry(root, font=("titr",20,"bold"),textvariable=family,justify="right").place(x=250, y=90, height=40, width=250)
family_entry = Entry(root, font=("titr",20,"bold"),textvariable=family,justify="right").place(x=250, y=150, height=40, width=250)
phone_entry = Entry(root, font=("titr",20,"bold"),justify="right",textvariable=phone).place(x=250, y=210, height=40, width=250)
address_entry = Entry(root, font=("titr",20,"bold"),justify="right",textvariable=address).place(x=250, y=270, height=40, width=250)
name_lbl = Label(root, text=":لطفا نام دانشجو را وارد نمایید ", font=("titr",20,"bold")).place(x=520,y=90)
family_lbl = Label(root, text=":لطفا نام خانوادگی  دانشجو را وارد نمایید ", font=("titr",20,"bold")).place(x=520,y=150)
phone_lbl = Label(root, text=":لطفا شماره تلفن  دانشجو را وارد نمایید ", font=("titr",20,"bold")).place(x=520,y=210)
address_lbl = Label(root, text=":لطفا آدرس  دانشجو را وارد نمایید ", font=("titr",20,"bold")).place(x=520,y=270)

sub_btn = Button(root, font=("titr",20,"bold"),text="ثبت دانشجو" \
    ,justify="right",command=lambda:create()).place(x=520,y=330)

#3
columns= ("address","phone","family","name","id")
tree = ttk.Treeview(root, columns=columns,show="headings")
tree.place(x=150,y=400)
tree.heading("id",text="شماره دانشجویی")
tree.column("id",anchor=CENTER)
tree.heading("name", text="نام دانشجو")
tree.column("name",anchor=CENTER)
tree.heading("family", text="نام خانودگی دانشجو")
tree.column('family',anchor=CENTER)
tree.heading("phone",text="شماره تماس")
tree.column("phone",anchor=CENTER)
tree.heading("address",text= "ادرس")
tree.column("address",anchor=CENTER)

def clear_tree():
    for i in tree.get_children():
        tree.delete(i)


def clear_entry():
    name.set("")
    family.set("")
    phone.set("")
    address.set("")

def refresh():
    clear_tree()
    clear_entry()
    data = show_studens()
    for i in data :
        tree.insert("","end",values=(i[4],i[3],i[2],i[1],i[0]))


def create():
    create_student(name.get(),family.get(),phone.get(),address.get())
    if create:
        messagebox.showinfo("Info ","registred successfully")
        refresh()
    else:
         messagebox.showerror("Error ","something is wrong")

def item_selected (event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        global student_id
        student_id=record[4]
        name.set(record[3])
        family.set(record[2])
        phone.set(record[1])
        address.set(record[0])

tree.bind("<<TreeviewSelect>>",item_selected)


def delete():

    msgbox=messagebox.askquestion("Warning !","are you sure to delete?")
    if msgbox=="yes":
            remove_student(student_id)
            refresh()
            clear_entry()
            messagebox.showinfo("Delete","deleted successfully")
    else:
        pass

def update():
    update_student_controller(student_id,name.get(),family.get(),phone.get(),address.get())
    refresh()
    messagebox.showinfo("info","Updated successfully")













refresh_btn = Button(root, font=("titr",20,"bold"),text="تازه سازی" ,justify="right",command=refresh).place(x=380,y=330)
delete_btn = Button(root, font=("titr",20,"bold"),text = "حذف دانشجو",command=lambda:delete()).place(x=680,y=330)
update_btn = Button(root, font=("titr",20,"bold"),text = "آپدیت دانشجو",command=lambda:update()).place(x=840,y=330)


root.mainloop()