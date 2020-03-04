import tkinter as tk
from random import randint

root = tk.Tk()
root.title("Task - 1")
root.geometry("200x300")

def def_listbox():
  lb = tk.Listbox(frame1)
  lb.pack(side="left", expand=1, fill=tk.BOTH)

  for n in range(49):
    rnd = str(randint(1, 100))
    lb.insert(tk.END, rnd)
  return lb

frame1 = tk.Frame(root)
frame1.pack(expand=1, fill=tk.BOTH)
lb1 = def_listbox()

root.mainloop()
