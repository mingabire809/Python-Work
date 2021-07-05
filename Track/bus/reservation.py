import mysql.connector
import sys
import random
from calendar import week
import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter import *
from typing import Sized
from tkcalendar import *
from tkinter import messagebox
from tkinter import ttk
import calendar
import datetime
import tkinter
import tkcalendar
mydb = mysql.connector.connect(
    host="localhost",user="root",passwd="Michael60647",database = "Bus"
)
bus = tk.Tk()
bus.geometry('900x750')

intro = Label(bus,text='Bus Management',font=('Arial',25))
intro.pack()
my_cursor = mydb.cursor()
place = 0
def intro():
    for widget in bus.winfo_children():
        widget.destroy()
    #intro = Label(bus,text='Dashboard',font=('Arial',25))
    #intro.pack()
    intro = Label(bus,text='Dashboard',font=('Arial',25))
    intro.pack()
    frame = tk.Frame(bus,bg='white')
    frame.place(relwidth= 0.8, relheight= 0.8, relx=0.1, rely= 0.1)
    #intro = Label(frame,text='Dashboard',font=('Arial',25))
    #intro.pack()
    label1 = Label(frame, text= 'Full Name',font=('Arial',10))
    label1.place(x=40,y=20)
    global mytext
    mytext = Text(frame,width = 30, height = 1,)
    mytext.pack(pady = 20)
    label2 = Label(frame,text="Destination",font=('Arial',10))
    label2.place(x=40,y=70)
    global variable
    variable = StringVar(frame)
    variable.set("Choose the destination")
    destinations = OptionMenu(frame,variable,'Nairobi','Mombasa','Kigali',"Bujumbura",'Juba','Kampala','Dar es Salam')
    destinations.pack()
    label3 = Label(frame,text= 'Date of travelling',font=('Arial',10))
    label3.place(x= 40, y=120)
    global cal
    cal = Calendar(frame)
    cal.pack()
    confirm = tk.Button(frame,text='register',bg = 'gray',command=registration)
    confirm.pack(side=BOTTOM)
    retrieve = tk.Button(frame,text='show client',bg='gray',command=display)
    retrieve.pack(side=RIGHT)
    
def registration():
    registration_number = random.randint(1,1000)
    name = mytext.get(1.0,END)
    destination = variable.get()
    date = cal.get_date()
    dates  = datetime.date.today()
    form = "Insert into reservation(name,reference,destination,date,bookingdate) values(%s,%s,%s,%s,%s)"
    data =  [(name,registration_number,destination,date,dates),]
    my_cursor.executemany(form, data)
    mydb.commit()
    if(destination == 'Nairobi'):
        forms = "Insert into nairobi(reference,name,date,bookingdate) values(%s,%s,%s,%s)"
        datas = [(registration_number,name,date,dates)]
        my_cursor.executemany(forms,datas)
        mydb.commit()
    elif(destination == 'Mombasa'):
        forms = "Insert into mombasa(reference,name,date,bookingdate) values(%s,%s,%s,%s)"
        datas = [(registration_number,name,date,dates)]
        my_cursor.executemany(forms,datas)
        mydb.commit()
    elif(destination == 'Kigali'):
        forms = "Insert into kigali(reference,name,date,bookingdate) values(%s,%s,%s,%s)"
        datas = [(registration_number,name,date,dates)]
        my_cursor.executemany(forms,datas)
        mydb.commit()
    elif(destination == 'Bujumbura'):
        forms = "Insert into bujumbura(reference,name,date,bookingdate) values(%s,%s,%s,%s)"
        datas = [(registration_number,name,date,dates)]
        my_cursor.executemany(forms,datas)
        mydb.commit()
    elif(destination == 'Juba'):
        forms = "Insert into juba(reference,name,date,bookingdate) values(%s,%s,%s,%s)"
        datas = [(registration_number,name,date,dates)]
        my_cursor.executemany(forms,datas)
        mydb.commit()
    elif(destination == 'Kampala'):
        forms = "Insert into kampala(reference,name,date,bookingdate) values(%s,%s,%s,%s)"
        datas = [(registration_number,name,date,dates)]
        my_cursor.executemany(forms,datas)
        mydb.commit()
    else:
        forms = "Insert into dar_es_salam(reference,name,date,bookingdate) values(%s,%s,%s,%s)"
        datas = [(registration_number,name,date,dates)]
        my_cursor.executemany(forms,datas)
        mydb.commit()
    try:
      messagebox.showinfo("Status",f"Client {name} with reference number {registration_number} and destination to {destination} registered successfully!")
      mytext.delete(1.0,END)
    except:
        messagebox.showerror("Error","Error While registering data!!")
    
def display():
    for widget in bus.winfo_children():
      widget.destroy()
    intro = Label(bus,text='Customer Records',font=('Arial',25))
    intro.pack()
    frame1 = tk.Frame(bus,bg='white')
    frame1.place(relwidth= 0.8, relheight= 0.8, relx=0.1, rely= 0.1)
    variables = StringVar(frame1)
    variables.set("Choose the destination")
    destinations = OptionMenu(frame1,variables,'Nairobi','Mombasa','Kigali',"Bujumbura",'Juba','Kampala','Dar es Salam','all')
    destinations.pack()
    global canvas
    canvas = tk.Canvas(frame1, height=600, width= 700, bg= "#263D42")
    canvas.pack()
    
    
    tree = ttk.Treeview(frame1)
    tree['columns'] = ('Full Name','Reference','Date','Booking Date')
    tree.column("#0",width=120,minwidth=25)
    tree.column("Full Name", anchor=W, width= 120)
    tree.column("Reference", anchor= CENTER,width=80)
    tree.column("Date", anchor=W,width= 80)
    tree.column("Booking Date",anchor=W,width=120)
    tree.heading('#0',text="Label",anchor = W)
    tree.heading('Full Name',text='Customer name',anchor = W)
    tree.heading('Reference',text='Reference Number',anchor = CENTER)
    tree.heading('Date',text='Departure Date',anchor = W)
    tree.heading('Booking Date',text='Booking date',anchor = W)
    
    def show():
        destinations = variables.get()
        if(destinations == 'Nairobi'):
            
           my_cursor.execute("Select * from nairobi")
           result = my_cursor.fetchall()
           for widget in canvas.winfo_children():
                widget.destroy()
           label = tk.Label(canvas, text=f"{destinations} Records", font=("Arial",20)).grid(row=0, columnspan=3)
 
           cols = ('Reference', 'Full Name', 'date','booking date')
           listBox = ttk.Treeview(canvas, columns=cols, show='headings')
           for col in cols:
             listBox.heading(col, text=col)    
             listBox.grid(row=1, column=0, columnspan=2)
            
           for i,(reference,full_name,date,booking_date) in enumerate(result,start=1):
                listBox.insert("","end",values=(reference,full_name,date,booking_date))


        elif(destinations == 'Mombasa'):
            my_cursor.execute("Select * from mombasa")
            result = my_cursor.fetchall()
            for widget in canvas.winfo_children():
                widget.destroy()
            label = tk.Label(canvas, text=f"{destinations} Records", font=("Arial",20)).grid(row=0, columnspan=3)
 
            cols = ('Reference', 'Full Name', 'date','booking date')
            listBox = ttk.Treeview(canvas, columns=cols, show='headings')
            for col in cols:
              listBox.heading(col, text=col)    
              listBox.grid(row=1, column=0, columnspan=2)
            count = 0
            for i,(reference,full_name,date,booking_date) in enumerate(result,start=1):
                listBox.insert("","end",values=(reference,full_name,date,booking_date))
        elif(destinations == 'Kigali'):
            my_cursor.execute("Select * from kigali")
            result = my_cursor.fetchall()
            for widget in canvas.winfo_children():
                widget.destroy()
            label = tk.Label(canvas, text=f"{destinations} Records", font=("Arial",20)).grid(row=0, columnspan=3)
 
            cols = ('Reference', 'Full Name', 'date','booking date')
            listBox = ttk.Treeview(canvas, columns=cols, show='headings')
            for col in cols:
              listBox.heading(col, text=col)    
              listBox.grid(row=1, column=0, columnspan=2)
            count = 0
            for i,(reference,full_name,date,booking_date) in enumerate(result,start=1):
                listBox.insert("","end",values=(reference,full_name,date,booking_date))
        elif(destinations == 'Bujumbura'):
            my_cursor.execute("Select * from bujumbura")
            result = my_cursor.fetchall()
            for widget in canvas.winfo_children():
                widget.destroy()
            #i = 0
            label = tk.Label(canvas, text=f"{destinations} Records", font=("Arial",20)).grid(row=0, columnspan=3)
 
            cols = ('Reference', 'Full Name', 'date','booking date')
            listBox = ttk.Treeview(canvas, columns=cols, show='headings')
            for col in cols:
              listBox.heading(col, text=col)    
              listBox.grid(row=1, column=0, columnspan=2)
            count = 0
            for i,(reference,full_name,date,booking_date) in enumerate(result,start=1):
                listBox.insert("","end",values=(reference,full_name,date,booking_date))
           
        elif(destinations == 'Juba'):
            my_cursor.execute("Select * from juba")
            result = my_cursor.fetchall()
            for widget in canvas.winfo_children():
                widget.destroy()
           
            label = tk.Label(canvas, text=f"{destinations} Records", font=("Arial",20)).grid(row=0, columnspan=3)
 
            cols = ('Reference', 'Full Name', 'date','booking date')
            listBox = ttk.Treeview(canvas, columns=cols, show='headings')
            for col in cols:
              listBox.heading(col, text=col)    
              listBox.grid(row=1, column=0, columnspan=2)
            count = 0
            for i,(reference,full_name,date,booking_date) in enumerate(result,start=1):
                listBox.insert("","end",values=(reference,full_name,date,booking_date))
        elif(destinations == 'Kampala'):
            my_cursor.execute("Select * from kampala")
            result = my_cursor.fetchall()
            for widget in canvas.winfo_children():
                widget.destroy()
            label = tk.Label(canvas, text=f"{destinations} Records", font=("Arial",20)).grid(row=0, columnspan=3)
 
            cols = ('Reference', 'Full Name', 'date','booking date')
            listBox = ttk.Treeview(canvas, columns=cols, show='headings')
            for col in cols:
              listBox.heading(col, text=col)    
              listBox.grid(row=1, column=0, columnspan=2)
            count = 0
            for i,(reference,full_name,date,booking_date) in enumerate(result,start=1):
                listBox.insert("","end",values=(reference,full_name,date,booking_date))
        elif(destinations == 'Dar es Salam'):
            my_cursor.execute("Select * from dar_es_salam")
            result = my_cursor.fetchall()
            for widget in canvas.winfo_children():
                widget.destroy()
            label = tk.Label(canvas, text=f"{destinations} Records", font=("Arial",20)).grid(row=0, columnspan=3)
 
            cols = ('Reference', 'Full Name', 'date','booking date')
            listBox = ttk.Treeview(canvas, columns=cols, show='headings')
            for col in cols:
              listBox.heading(col, text=col)    
              listBox.grid(row=1, column=0, columnspan=2)
            count = 0
            for i,(reference,full_name,date,booking_date) in enumerate(result,start=1):
                listBox.insert("","end",values=(reference,full_name,date,booking_date))
        elif(destinations == 'all'):
            my_cursor.execute("Select * from reservation")
            result = my_cursor.fetchall()
            for widget in canvas.winfo_children():
                widget.destroy()
            i = 0
          
            label = tk.Label(canvas, text=f"{destinations} Records", font=("Arial",20)).grid(row=0, columnspan=3)
 
            cols = ('Full Name','Reference','destination', 'date','booking date')
            listBox = ttk.Treeview(canvas, columns=cols, show='headings')
            for col in cols:
              listBox.heading(col, text=col)    
              listBox.grid(row=1, column=0, columnspan=2)
            count = 0
            for i,(full_name,reference,destination,date,booking_date) in enumerate(result,start=1):
                listBox.insert("","end",values=(full_name,reference,destination,date,booking_date))
        else:
            messagebox.showerror("Error","No destination selected!!")
    confirm = tk.Button(bus,text='Display Client',command=show)
    confirm.place(x=350,y=680)
    dashboard = tk.Button(bus, text="Dasboard", command= clearing)
    dashboard.place(x=500,y=680)
    
    def clear_data():
        for widget in frame1.winfo_children():
            widget.destroy()
        display()
    clears = tk.Button(bus,text='Clear',command=clear_data)
    clears.place(x=450,y=680)
   
def clearing():
    
    for widgets in bus.winfo_children():
        widgets.destroy()
    intro()
intro()