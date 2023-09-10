from tkinter import *
import random
from tkinter import messagebox as msg
import mysql.connector as mc

#database connection
db = mc.connect(host="localhost",user = "root",password = "Ab@091006")
mycursor = db.cursor()
mycursor.execute("show databases;")

u = "admin" #default username
p = 123 #defualt password

#funtion for adding information to database
def addinfo():
    print("Added info")
    table_check = "select * from passwordusername;"
    if mycursor.execute(table_check).fetchall() == []:
        print("Table does not exist")
    t = "inser"
#function for sign up

def sign_up():
    m.destroy()
    sign_up_page = Tk()
    sign_up_page.title("Sign Up")
    sign_up_page.geometry("500x600+700+250")
    sign_up_page.resizable(False,False)
    sign_up_page.configure(background='#222')
    username_signup = StringVar()
    password_signup = StringVar()
    new_username_label = Label(sign_up_page,text="Username : ",bg="#222",fg="#fff",font=("sans-serif",15)).place(x=80,y=150)
    new_username_entry = Entry(sign_up_page,textvariable=username_signup,width=30).place(x=185,y=150)
    new_password_label = Label(sign_up_page,text="Password : ",bg="#222",fg="#fff",font=("sans-serif",15)).place(x=80,y=190)
    new_password_entry = Entry(sign_up_page,width=30,textvariable=password_signup).place(x=185,y=190)
    confirm_btn  = Button(sign_up_page,width=8,command=addinfo,font=("sans-serif",15),text="Confirm",bg="#df4167").place(x=200,y=250)
#login page
m=Tk()
m.geometry("500x600+700+250")
m.resizable(False,False)
m.configure(background='#222')
#username
userid = StringVar()
passwd = StringVar() 
username_Label = Label(m,text="Username : ",bg="#222",fg="#fff",font=("sans-serif",15)).place(x=80,y=150)
username_Label_entry = Entry(m,textvariable=userid,width=30).place(x=185,y=150)
#password
password = Label(m,text="Password : ",bg="#222",fg="#fff",font=("sans-serif",15)).place(x=80,y=190)
password_entry =Entry(m,textvariable=passwd,width=30).place(x=185,y=190)
#Button for sign up
sign_up = Button(m,text="Sign Up",width=8,bg="#df4167",font=("sans-serif",15),command=sign_up).place(x=300,y=250)


def login():
    if u == userid.get() and p == int(passwd.get()):
        login_page()
    else:
        mess = msg.showinfo("Info","Please use the correct username and password")

def login_page():
    m.destroy()
    r = Tk()
    r.geometry("900x500+450+250")
    r.resizable(False,False)
    r.title("Booking system")
    r.configure(background="#222")

    #funtions
    #1. Funtion for getting the name
    def n():
        print(s1.get(),s2.get(),s3.get(),s4.get(),s5.get())
    #Funtion to open new window for ticket booking
    def booking_window():
        a = Toplevel(r)
        a.geometry("900x500+450+250")
        a.resizable(False,False)
        a.title("Booking")
        a.configure(background="#222")

        # label,entry for name
        f1 = Frame(a,background='green').pack()
        global s1
        s1 = StringVar()
        e1 = Entry(a,width=50,textvariable=s1,font=("sans-serif",12)).place(x=250,y=150)
        l1 = Label(a,text="NAME",font='sans-serif',bg="#222",fg="#fff").place(x=90,y=150)
        test_btn = Button(a,width=10,command=n,text="Test",bg="#df4167").place(x=350,y=300)

        #label,entry for phone
        global s2
        s2 = StringVar()
        l2 = Label(a,text="PHONE : ",font="sans-serif",bg="#222",fg="#fff").place(x=90,y=100)
        e2 = Entry(a,textvariable=s2,width=50,font=("sans-serif",12)).place(x=250,y=100)

        #label,entry for conuntry
        global s3
        s3 = StringVar()
        l3 = Label(a,text="COUNTRY : ",font="sans-serif",bg="#222",fg="#fff").place(x=90,y=50)
        e3 = Entry(a,textvariable=s3,width=50,font=("sans-serif",12)).place(x=250,y=50)

        #label,entry for gender
        global s4
        s4 = StringVar()
        l4 = Label(a,text="GENDER : ",font="sans-serif",bg="#222",fg="#fff").place(x=90,y=200)
        e4 = Entry(a,textvariable=s4,width=50,font=("sans-serif",12)).place(x=250,y=200)

        # TICKET CODE
        global s5
        s5 = StringVar()
        l5 = Label(a,text="REFERENCE CODE : ",font="sans-serif",bg="#222",fg="#fff").place(x=90,y=250)
        e5 = Entry(a,textvariable=s5,width=50,state='disabled',font=("sans-serif",12)).place(x=250,y=250)


    #function for history page
    def history_window():
        b = Toplevel(r)
        b.geometry("900x500+450+250")
        b.resizable(False,False)
        b.title("History")
    #function for delete page
    def delete_window():
        c = Toplevel(r)
        c.geometry("900x500+450+250")
        c.resizable(False,False)
        c.title("Deletion")
        temp = mycursor.execute("select * from passwordusername")
        for i in temp:
            d = Label(c,text=i).grid(row=1,column=2)
            

    # function for close    
    def close():
        r.destroy()




    #Heading: Ticket Booking System
    h1 = Label(r,text="Book Your Tickets",font=('sans-serif',15),bg="#222",fg="#fff").pack()


    #new window for ticket booking

    b2 = Button(r,width=20,command=booking_window,text="Booking",height=8,bg='#55d6aa').place(x=73.5,y=70)
    b3 = Button(r,width=20,command=history_window,text="History",height=8,bg='#55d6aa').place(x=647.5,y=70)
    b4 = Button(r,width=20,command=delete_window,text="Delete",height=8,bg='#55d6aa').place(x=73.5,y=220)
    b5 = Button(r,width=20,command=close,text="Close",height=8,bg='#55d6aa').place(x=647.5,y=220)





    #test_btn = Button(f1,width=10,command=n,text="Test").pack()
    r.mainloop()



b_login = Button(m,width=5,text="Login",command=login,font=("sans-serif",15),bg="#df4167").place(x=100,y=250)


m.mainloop()



