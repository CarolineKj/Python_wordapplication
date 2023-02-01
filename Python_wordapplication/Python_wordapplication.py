
import tkinter as tk  
from tkinter import ttk

words = "" 
win = tk.Tk()
win.title("Sentance Converter App")
lbl = ttk.Label(win, text = "Skriv in en mening:", anchor='w').grid(column = 0, row = 0) #anchoring fungerar inte
win.geometry("450x300")

def click():   
    #följande labels för att skriva ut svaret i widget
    ttk.Label(win, anchor="w", text = "Ursprunglig textsträng: " + words.get()).grid(columns = 2, row = 3)
    ttk.Label(win, text = "Omvänd ordning på orden: " + reverseOrder(words.get())).grid(columns = 2, column = 0, row = 4)
    ttk.Label(win, text = "Antal ord: " + str(len(words.get().split()))).grid(columns =2 , column = 0, row = 6)
    ttk.Label(win, text = "Antal konsonanter: " + str(countConsonants(words.get()))).grid(columns = 2, column = 0, row = 5)
    

    #följande prints för att skriva ut i prompten istället för i widgeten
    #print("Ursprunglig textsträng: " + name.get()) 
    #print("Omvänd ordning på orden: " + reverseOrder(name.get()))
    #print("Antal konsonanter: " + str(countConsonants(name.get())))
    #print("Antal ord: " + str(len(name.get().split())))

def countConsonants(string):
   num_consonants = 0
   for char in string.lower():
      if char in "bcdfghjklmnpqrstvwxyz": 
         num_consonants += 1
   return num_consonants

def reverseOrder(string):
    s = string.split()[::-1]
    new = ""
    for i in s:
        new+= i+" ";
    return new 
  

words = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 45, textvariable = words).grid(column = 0, row = 1)
button = ttk.Button(win, width = 20, text = "submit", command = click).grid(column = 1, row = 1)  
win.mainloop()  