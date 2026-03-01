from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("HeroMaker")
root.geometry("1200x600") 
 
def click():
    window = Tk()
    window.title("Новое окно")
    window.geometry("250x200")
 
button = ttk.Button(text="Вперед", command=click)
button.pack(anchor=E, expand=1)
button = ttk.Button(text="Назад", command=click)
button.pack(anchor=E, expand=2)
 
root.mainloop()