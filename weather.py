import tkinter as tk
import requests
import time
      def getWeather():
          city =textfield.get() 
          
canvas = tk.Tk()
canvas.geometry("600*500")
canvas.title("Weather Appplication")

f=("poppins",15,"bold")      #define fonts
t=("poppins",35,"bold")

#text field
textfield = tk.Entry(canvas, font =t)
textfield.pack(pady=20)
textfield.focus()

label1= tk.Label(canvas, font =t)
lable1.pack()    
label2 = tk,Label2(canvas , font =f)

canvas.mainloop()
