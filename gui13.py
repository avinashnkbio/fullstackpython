# !/usr/bin/python3  
  
from tkinter import *  
  
top = Tk()  
  
top.geometry("300x350")  
  
lbl = Label(top,text = "List of me and  my full stack python students")  
  
listbox = Listbox(top)  
  
listbox.insert(1,"Anjana S")  
  
listbox.insert(2, "Rincy R")  
  
listbox.insert(3, "Anju A")  
  
listbox.insert(4, "Nithin J")  

listbox.insert(5, "Avinash Nandakumar")  
  
lbl.pack()  
listbox.pack()  
  
top.mainloop()  