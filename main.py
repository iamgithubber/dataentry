from tkinter import *
from datetime import datetime
#from time import sleep
def exit1():
    see.destroy()
def cleardata():
    f = open('data','w')
def seedata():
    global see
    see = Toplevel(main)
    see.title('database')
    f = open('data','r')
    for data in f:
        Label(see,text=data,font='calibre 10 bold').pack()
    f.close()
    Button(see,text='exit',command=exit1).pack()
def enter():
    name1=name.get()
    age1=age.get()
    phone1=phone_number.get()
    email1=email.get()
    file = open('data','a')
    file.write('||name :- '+name1+"||"+'age :- '+age1+"||"+'phone1 :- '+phone1+"||"+'email:-  '+email1+"||"+"time :-"+now.strftime('%y-%m-%d %H:%M:%S')+" ||")
    file.write("""
""")
    file.close()



    name_entry.delete(0,END)
    age_entry.delete(0,END)
    phone_entry.delete(0,END)
    email_entry.delete(0,END)
def mainscreen():
    global main
    main = Tk()
    main.geometry('300x700')
    main.title('data entry')
    global name,age,phone_number,email
    global name_entry, age_entry, phone_entry, email_entry
    name = StringVar()
    age = StringVar()
    phone_number = StringVar()
    email = StringVar()
    Label(text='enter the details',fg='red',bg='black',height='2',width='500',font='cartoon 15 bold').pack()
    Label(text="").pack()
    Label(text='name',fg='black',height='2',font='cartoon 10 bold underline').place(x=50,y=70)
    name_entry = Entry(textvariable=name,borderwidth='5')
    name_entry.place(x=120,y=70)
    Label(text='age',fg='black',height='2',font='cartoon 10 bold underline').place(x=50,y=170)
    age_entry = Entry(textvariable=age,borderwidth='5')
    age_entry.place(x=120,y=170)
    Label(text='phone number',fg='black',height='2',font='cartoon 10 bold underline').place(x=10,y=270)
    phone_entry = Entry(textvariable=phone_number,borderwidth='5')
    phone_entry.place(x=120,y=270)
    Label(text='email',fg='black',height='2',font='cartoon 10 bold underline').place(x=50,y=370)
    email_entry = Entry(textvariable=email,borderwidth='5')
    email_entry.place(x=120,y=370)
    global now
    now = datetime.now()
    Button(text='enter',height='2',width='20',command=enter,bg='skyblue').place(x=50,y=450)
    Button(text='see data', command=seedata,bg='yellow',fg='black').place(x=10,y=550)
    Button(text='clear data', command=cleardata, bg='yellow', fg='black').place(x=200, y=550)
    main.mainloop()
mainscreen()