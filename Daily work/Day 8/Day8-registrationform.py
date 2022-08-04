"""Registration Form"""

from tkinter import *
from tkinter import messagebox
from mysql import connector

def database():
    conn = connector.connect(
       user='root',

       password='root',

       host='127.0.0.1',

       port='3306',

       database='register')
    mycursor = conn.cursor()
    mycursor.execute("insert into form values(%s,%s,%s,%s,%s,%s)",
                    (e_1.get(), e_2.get(), e_3.get(), e_4.get(), l_5.get(), var.get()))
    messagebox.showinfo("Info","Submitted")
    conn.commit()
    


ab=Tk()
ab.title("Registration Form")

l_0 = Label(ab,text="Registration form",width=20,font=("bold", 20))
l_0.place(x=70,y=53)


l_1 = Label(ab,text="SR NO:",width=20,font=("bold", 10))
l_1.place(x=90,y=130)

e_1 = Entry(ab)
e_1.place(x=210,y=130)

l_2 = Label(ab,text="NAME:",width=20,font=("bold", 10))
l_2.place(x=220,y=180)

e_2 = Entry(ab)
e_2.place(x=210,y=180)

l_3= Label(ab,text="ROLL NO:",width=20,font=("bold",10))
l_3.place(x=82,y=230)
e_3=Entry(ab)
e_3.place(x=210,y=230)

l_4=Label(ab,text="ADDRESS:",width=20,font=("bold", 10))
l_4.place(x=80,y=280)

e_4=Entry(ab)
e_4.place(x=210,y=280)
l_5=Label(ab,text="BRANCH:",width=20,font=("bold", 10))
l_5.place(x=80,y=330)
l_5= StringVar(ab)
l_5.set("Select one") 

dd= OptionMenu(ab,l_5,"CSE","IT","ECE","ME","EE")
dd.pack()
dd.place(x=210,y=325)

l_6 = Label(ab,text="Gender:",width=20,font=("bold", 10))
l_6.place(x=75,y=380)
var = IntVar()
Radiobutton(ab,text="Male",padx = 5, variable=var, value=1).place(x=200,y=380)
Radiobutton(ab,text="Female",padx = 20, variable=var, value=2).place(x=270,y=380)

Button(ab,text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=440)
ab.configure(background = "green")
ab.mainloop()
print("registration form  seccussfully created...")