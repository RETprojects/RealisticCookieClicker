# Realistic Cookie Clicker
# RETprojects
# May 4, 2023
# An incremental game inspired by Cookie Clicker, but with a realistic image of a cookie!
# Photo credit: Evan Amos (https://commons.wikimedia.org/wiki/File:Pep-Farm-Cookie-Alt.jpg)

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

counter = 0

def increment():
    global counter
    counter += 1
    label['text'] = f'{counter} clicks'
    # if the counter goes to a number divisible by 10, show a message
    if counter % 10 == 0:
        messagebox.showinfo("showinfo", "GREAT! Can you click another 10 times?")

root = tk.Tk()
root.title("Realistic Cookie Clicker")
label = tk.Label(root, text='0 clicks', font=('Comic Sans MS', 15))
label.grid(row=4, column=2)
photo = ImageTk.PhotoImage(Image.open("640px-Pep-Farm-Cookie-Alt.png").resize((380, 270)))
tk.Button(root, command=increment, text="Click Me", width=380, height=270, image=photo).grid(row=2, column=2)
root.mainloop()