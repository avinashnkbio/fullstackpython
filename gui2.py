#python application to create a simple button  
  
from tkinter import *   
  
  
top = Tk()  
  
top.geometry("200x100")  
  
b = Button(top,text = "Submit")  
  
b.pack()  
  
top.mainloop()  
