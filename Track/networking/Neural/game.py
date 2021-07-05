from calendar import week
import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter import *
from typing import Sized
from tkcalendar import *
import random


root = tk.Tk()
root.title("Bus Reservation System")
#root.iconbitmap('C:\Users\ZEBRA\Downloads\carbackground.jpg')
apps = []
if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        print(tempApps)
def addApp():
    for widget in frame.winfo_children():
      widget.destroy()
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select File", 
    filetypes = (("executable","*.exe"),("a;; files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg="gray")
        label.pack()
def runApps():
    for app in apps:
        os.startfile(app)
def submit():
    username = entry.get()
    print(username)
def delete():
    entry.delete(0, END) #delete the line of text
def backspace():
    entry.delete(len(entry.get())-1, END) #delete last character

canvas = tk.Canvas(root, height=600, width= 700, bg= "#263D42")
#Entry widget
#mytext = Text(root,width = 60, height = 20)
#mytext.pack(pady = 20)



#entry.insert(0, 'Python')


# entry.config(show='*') for password especially


canvas.pack()

frame = tk.Frame(root, bg= 'white')

frame.place(relwidth= 0.8, relheight= 0.8, relx=0.1, rely= 0.1)
label1 = Label(frame, text= 'Full Name')
label1.place(x=20,y=20)
mytext = Text(frame,width = 30, height = 1,)
mytext.pack(pady = 20)
destination = Label(frame,text="Destination")
destination.place(x=20,y=70)
variable = StringVar(frame)
variable.set("Choose the destination")
destinations = OptionMenu(frame,variable,'Nairobi','Mombasa','Kigali',"Bujumbura",'Juba','Kampala','Dar es Salam')
destinations.pack()

print(variable)
direction = tk.Label(frame,text=destinations.__str__())
direction.pack()
label2 = Label(frame,text= 'Date of travelling')
label2.place(x= 20, y=120)
label3 = Label(frame,text="Test")
label3.place(x=250,y= 130)
cal = Calendar(frame)
cal.pack()
dates = cal.get_date()
des = destinations
print(dates)

entry = Entry()

entry.config(font=("Ink Free",20))
entry.config(bg="gray")
entry.config(fg="white")
entry.config(width= 12)
entry.pack()
openFile = tk.Button(root, text= 'Open File', padx=10, pady=5, fg='white',bg="#263D42", command= addApp) 
openFile.pack()
runApps = tk.Button(root, text= 'Run Apps', padx=10, pady=5, fg='white',bg="#263D42",command=runApps)
runApps.pack()
submit = tk.Button(root, text = 'Submit', command= submit)
submit.pack(side = RIGHT)
delete = tk.Button(root, text = 'delete', command= delete)
delete.pack(side = LEFT)

backspace = tk.Button(root, text = 'backspace', command= backspace)
backspace.pack(side = LEFT)

root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')


