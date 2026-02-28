from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("HeroMaker")
root.geometry("500x500") 
 
def click():
    window = Tk()
    window.title("Новое окно")
    window.geometry("250x200")
 
button = ttk.Button(text="Автоматический режим", command=click)
button.pack(anchor=CENTER, expand=1)
button = ttk.Button(text="Ручная сборка", command=click)
button.pack(anchor=CENTER, expand=2)
 
root.mainloop()