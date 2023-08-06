import tkinter as tk


root = tk.Tk()

myLabel = tk.Label(root, text='Moo Moo Cow')
mylabel1 = tk.Label(root, text='My name is Vurchas')
mylabel2 = tk.Label(root, text='')
mylabel3 = tk.Label(root, text='')
mylabel4 = tk.Label(root, text='')

myLabel.grid(row= 0, column= 0)
mylabel1.grid(row= 1, column= 5)
mylabel2.grid(row= 1, column= 2)
mylabel3.grid(row= 1, column= 2)
mylabel4

root.mainloop()
