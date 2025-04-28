import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def connection() :
    global conn,cursor
    conn = sqlite3.connect("database/finalset6.db")
    cursor = conn.cursor()

def mainwindow() :
    root = Tk()
    w = 1100
    h = 800
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#28b5b5')
    root.title("Week13 Insert/Update/Delete Application: ")
    root.option_add('*font',"Garamond 15 bold")
    root.rowconfigure((0,1),weight=1)
    root.columnconfigure((0,1),weight=1)

    return root

def loginlayout() :
    global userentry,pwdentry
    loginframe.rowconfigure((0,1),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    llogin = Frame(loginframe,bg='#ffffff')
    llogin.grid(row=0,rowspan=2,column=0,sticky='news')
    llogin.rowconfigure(0,weight=1)
    llogin.columnconfigure(0,weight=1)

    rlogin = Frame(loginframe,bg='#000000')
    rlogin.grid(row=0,rowspan=2,column=1,sticky='news')
    rlogin.rowconfigure((0,1,2,3,4,5),weight=1)
    rlogin.columnconfigure((0,1),weight=1)

    loginframe.grid(row=0,column=0,columnspan=2,rowspan=2,sticky='news')
    Label(llogin,image=img1).grid(row=0,column=0)
    Label(rlogin,image=img2).grid(row=0,rowspan=2,column=0,columnspan=2)
    Label(rlogin,text="Username : ",bg='#8fd9a8',fg='#e4fbff',padx=20).grid(row=3,column=0,sticky='e')
    Label(rlogin,text="LOGIN PAGE",bg='#8fd9a8',fg='#e4fbff',padx=20).grid(row=2,column=0,columnspan=2)
    userentry = Entry(rlogin,bg='#e4fbff',width=20)
    userentry.grid(row=3,column=1,sticky='w',padx=20)
    pwdentry = Entry(rlogin,bg='#e4fbff',width=20,show='*')
    pwdentry.grid(row=4,column=1,sticky='w',padx=20)
    Label(rlogin,text="Password  : ",bg='#8fd9a8',fg='#e4fbff',padx=20).grid(row=4,column=0,sticky='e')
    Button(rlogin,text="Login",width=10,command=lambda:loginclick(userentry.get(),pwdentry.get())).grid(row=5,column=0,columnspan=2,pady=20,ipady=15,padx=40)
   
def loginclick(user,pwd) :
    global result
    if user == "" or pwd == "" :
        messagebox.showwarning("Admin : ","Please enter a username or password")
        userentry.focus_force()
    else :
        sql = "select * from login where user=?;"
        cursor.execute(sql,[user])
        result = cursor.fetchone()
        if result :
            sql = "select * from login where user=? and password=?;"
            cursor.execute(sql,[user,pwd])
            result = cursor.fetchone()
            if result :
                messagebox.showinfo("Admin : ","Login Successfully.")
                welcomepage(result)
            else :
                messagebox.showwarning("Admin : ","Incorrect Password \nPlease try again")
                pwdentry.selection_range(0,END)
                pwdentry.focus_force()
        else :
            messagebox.showwarning("Admin : ","The username not found.")
            userentry.selection_range(0,END)
            userentry.focus_force()

def welcomepage(result) :
    global top,left,right
    loginframe.grid_forget()
    pwdframe.grid_forget()
    updateframe.grid_forget()
    welcomeframe['bg'] = "#FCC2FC"
    welcomeframe.grid_rowconfigure((0),weight=1)
    welcomeframe.grid_rowconfigure((1),weight=5)
    welcomeframe.grid_columnconfigure((0),weight=1)
    welcomeframe.grid_columnconfigure((1),weight=5)
    welcomeframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')
    top = Frame(welcomeframe,bg='#FFF1D5')
    top.grid_rowconfigure(0,weight=1)
    top.grid_columnconfigure((0,1,2),weight=1)
    top.grid(row=0,column=1,sticky='news')
    left = Frame(welcomeframe,bg='#BDDDE4')
    left.grid_rowconfigure((0,1,2,3),weight=1)
    left.grid_columnconfigure(0,weight=1)
    left.grid(row=0,rowspan=2,column=0,sticky='news')
    right = Frame(welcomeframe,bg='#9EC6F3')
    right.grid_rowconfigure((0),weight=1)
    right.grid_columnconfigure(0,weight=1)
    right.grid(row=1,column=1,sticky='news')


    Label(left,image=img2,bg='#BDDDE4').grid(row=1,column=0,sticky='S')
    Label(left,text='User:Admin \nCourse Management Program',bg='#BDDDE4').grid(row=2,column=0,sticky='N')

    Button(top,compound='left',image=img5,text='Insert Subject',command=addclick).grid(row=0,column=0)
    Button(top,compound='left',image=img4,text='Search Subject',command=updateclick).grid(row=0,column=1)
    Button(top,compound='left',image=img6,text='Exit',command=exit).grid(row=0,column=2)

def addclick() :
    global addframe
    global codebox,namebox,daybox,roombox
    right.grid_forget()
    updateframe.grid_forget()
    addframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    addframe.grid_columnconfigure((0,1),weight=1)
    addframe.grid(row=1,column=1,sticky='news')
    Label(addframe,text="Subject Code : ",bg='#9EC6F3').grid(row=0,column=0,sticky='e')
    codebox = Entry(addframe,bg="#DAF5FF")
    codebox.grid(row=0,column=1,sticky='w',padx=20)
    Label(addframe,text="Subject Name : ",bg='#9EC6F3').grid(row=1,column=0,sticky='e')
    namebox = Entry(addframe,bg="#DAF5FF")
    namebox.grid(row=1,column=1,sticky='w',padx=20)
    Label(addframe,text="Subject type : ",bg='#9EC6F3').grid(row=2,column=0,sticky='e')
    daybox = Entry(addframe,bg="#DAF5FF")
    daybox.grid(row=2,column=1,sticky='w',padx=20)
    Label(addframe,text="Subject credit : ",bg='#9EC6F3').grid(row=3,column=0,sticky='e')
    roombox = Entry(addframe,bg="#DAF5FF")
    roombox.grid(row=3,column=1,sticky='w',padx=20)
    Button(addframe,text="Add",width=10,command=addcourse).grid(row=5,columnspan=2,ipady=10)

def addcourse() :
    if codebox.get() == "" or namebox.get() == "" or daybox.get() == "" or roombox.get() == "" :
        messagebox.showwarning("Admin: ","Please fullfill all of course data")
        codebox.focus_force()
    else : 
        sql = "select * from subject_1670702289 where scode=? or sname=?"
        cursor.execute(sql,[codebox.get(),namebox.get()])

        result = cursor.fetchone()
        if result :
            messagebox.showwarning("Admin: ","Course code or name already exist.")
            codebox.select_range(0,END)
            codebox.focus_force()
        else :
            sql = "insert into subject_1670702289 values (?,?,?,?)"
            cursor.execute(sql,[codebox.get(),namebox.get(),daybox.get(),roombox.get()])
            conn.commit()
            
            messagebox.showinfo("Admin:","Add course successfully")
            clearclick()

def searchclick() :

    sql = "select * from subject_1670702289 where scode=? collate nocase"
    #execute step
    cursor.execute(sql,[searchbox.get()])
    #fetch result
    result = cursor.fetchone()
    if result :
        eror.grid_forget()
        Label(updateframe,text="Subject Code : ",bg='#9EC6F3').grid(row=1,column=1,sticky='e')
        codebox = Entry(updateframe,bg="#DAF5FF")
        codebox.grid(row=1,column=2,sticky='w',padx=20)
        Label(updateframe,text="Subject Name : ",bg='#9EC6F3').grid(row=2,column=1,sticky='e')
        namebox = Entry(updateframe,bg="#DAF5FF")
        namebox.grid(row=2,column=2,sticky='w',padx=20)
        Label(updateframe,text="Subject type : ",bg='#9EC6F3').grid(row=3,column=1,sticky='e')
        daybox = Entry(updateframe,bg="#DAF5FF")
        daybox.grid(row=3,column=2,sticky='w',padx=20)
        Label(updateframe,text="Subject credit : ",bg='#9EC6F3').grid(row=4,column=1,sticky='e')
        roombox = Entry(updateframe,bg="#DAF5FF")
        roombox.grid(row=4,column=2,sticky='w',padx=20)
        Button(updateframe,text="Update Course",width=10,command=updatecourse).grid(row=5,column=2,columnspan=2,ipady=10)
        codebox.config(state='normal')
        codebox.delete(0,END)
        codebox.insert(0,result[0])
        namebox.delete(0,END)
        namebox.insert(0,result[1])
        daybox.delete(0,END)
        daybox.insert(0,result[2])
        roombox.delete(0,END)
        roombox.insert(0,result[3])
    else :
        eror.grid(row=1,rowspan=4,column=1,columnspan=3,sticky='news')
        eror.rowconfigure(0,weight=1)
        eror.columnconfigure(0,weight=1)
        Label(eror,image=img3,text='This Supject not found',bg='#9EC6F3',compound='bottom').grid(row=0,column=0)
        searchbox.select_range(0,END)
        searchbox.focus_force()

 
def updateclick() :
    global searchbox,codebox,namebox,daybox,roombox
    right.grid_forget()
    addframe.grid_forget()
    deleteframe.grid_forget()
    updateframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    updateframe.grid_columnconfigure((0,1,2,3),weight=1)
    updateframe.grid(row=1,column=1,sticky='news')
    Label(updateframe,text="Subject Code : ",bg='#9EC6F3').grid(row=0,column=0,sticky='e')
    searchbox = Entry(updateframe,bg="#DAF5FF")
    searchbox.grid(row=0,column=1,sticky='w',padx=20)
    Button(updateframe,image=img4,command=searchclick).grid(row=0,column=3,ipady=10)
    

def updatecourse() :
    global codebox,namebox,daybox,roombox
    if codebox.get() == "" or namebox.get() == "" or daybox.get() == "" or roombox.get() == "" :
        messagebox.showwarning("Admin: ","Please fullfill all of course data")
        codebox.focus_force()
    else :
        sql = "select * from subject_1670702289 where scode=?"

        cursor.execute(sql,[codebox.get()])
        result = cursor.fetchone()

        if result :
            sql = "select * from subject_1670702289 where sname=?"
            cursor.execute(sql,[namebox.get()])
            result = cursor.fetchone()
            if result :
                messagebox.showwarning("Admin : ","Duplicated course name")
                sql = """ 
                    update subject_1670702289 
                    set stype=?, scredit=?
                    where scode=?

                """

                cursor.execute(sql,[daybox.get(),roombox.get(),codebox.get()])
                conn.commit()
                messagebox.showinfo("Admin:","Update course successfully")
                clearclick()

            else :
                sql = """
                    update subject_1670702289
                    set sname=?, stype=?, scredit=?
                    where scode=?
 
                """
                cursor.execute(sql,[namebox.get(),daybox.get(),roombox.get(),codebox.get()])
                conn.commit()
                messagebox.showinfo("Admin:","Update course successfully")
                clearclick()
        else :
            messagebox.showwarning("Admin: ","Course code not found\n Try again.")
            codebox.select_range(0,END)
            codebox.focus_force()


   


def clearclick() :
    codebox.config(state='normal')
    codebox.delete(0,END)
    namebox.delete(0,END)
    daybox.delete(0,END)
    roombox.delete(0,END)
       


connection()
root = mainwindow()
loginframe = Frame(root,bg='#8fd9a8')
welcomeframe = Frame(root,bg='#FCC2FC')
updateframe = Frame(root,bg="#E5FDD1")
pwdframe = Frame(root,bg='#28b5b5')
addframe = Frame(welcomeframe,bg='#9EC6F3')
updateframe = Frame(welcomeframe,bg='#9EC6F3')
deleteframe = Frame(welcomeframe,bg='#9EC6F3')
eror = Frame(updateframe,bg='#9EC6F3')
selectoption = StringVar()
title = ["Course Code:","Course Name:","Day:","Room:"]
img1 = PhotoImage(file='imgset6/regist.png')
img2 = PhotoImage(file='imgset6/userimg.png')
img3 = PhotoImage(file="imgset6/course.png")
img4 = PhotoImage(file='imgset6/search.png')
img5 = PhotoImage(file='imgset6/add.png')
img6 = PhotoImage(file='imgset6/exit.png')

loginlayout()
root.mainloop()
cursor.close()
conn.close()

    