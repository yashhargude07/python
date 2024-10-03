import tkinter as tk

parent = tk.Tk()
parent.title("Welcome to India")
parent.geometry("800x400")

my_label = tk.Label(parent, text="Hello Tejas", font=("Arial Bold", 90))

my_label.grid(column=0, row=0)

parent.mainloop()

