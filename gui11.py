from tkinter import *   
  
top = Tk()  
  
top.geometry("300x300")  
  
checkvar1 = IntVar()  
  
checkvar2 = IntVar()  
  
checkvar3 = IntVar()  

checkvar4 = IntVar()
  
chkbtn1 = Checkbutton(top, text = "C", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn2 = Checkbutton(top, text = "C++", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn3 = Checkbutton(top, text = "Java", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10)  

chkbtn4 = Checkbutton(top, text = "FullStackPython", variable = checkvar4, onvalue = 1, offvalue = 0, height = 2, width = 15)  

b = Button(top,text = "Submit")  
  
b.pack()  
  
chkbtn1.pack()  
  
chkbtn2.pack()  
  
chkbtn3.pack()
  
chkbtn4.pack()
  
top.mainloop()  