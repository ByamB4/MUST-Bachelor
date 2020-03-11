import matplotlib
matplotlib.use('Agg')
from tkinter import *
from tkinter import messagebox as TkMessageBox
from PIL import ImageTk, Image
import os

def photo_browse():
  def add_photo(screen, column_num):
    if not 'pic' in globals():
      TkMessageBox.showerror('Error!', 'No picture selected!')
      screen.lift()
    else:
      screen.image = pic
      can = Label(screen, image=pic)
      can.grid(row=0, column=column_num)
      Label(screen, text=chosen_photo).grid(row=1, column=column_num)
  def selection_listbox(evt):
    global chosen_photo
    chosen_photo = str(photo_listbox.get(photo_listbox.curselection()))
    image_location = 'Pics/' + chosen_photo
    global pict
    pict = Image.open(image_location)
    global pic
    pic = ImageTk.PhotoImage(pict)
  import glob

  photo_browse_screen = Toplevel()
  photo_browse_screen.title('Photo browse')
  photo_browse.geometry('1000x600')
  photo_browse.resizeable(0, 0)
  photo_listbox = Listbox(photo_browse_screen, width=50, height=35)
  photo_listbox.grid(columnspan=3)
  photo_listbox.bind('<<ListboxSelect>>', selection_listbox)
  name_list = glob.glob('Pics/*.png')
  name_list = [i[5:] for i in name_list]
  name_list.sort()
  n = 1
  m = 0
  for i in name_list:
    photo_listbox.insert(n, name_list[m])
    n += 1
    m += 1
  Button(photo_browse_screen, text='PIC 1', command=lambda: add_photo(photo_browse_screen, 4)).grid(row=1, column=0)
  Button(photo_browse_screen, text='PIC 2', command=lambda: add_photo(photo_browse_screen, 5)).grid(row=1, column=1)
  Button(photo_browse_screen, text='EXIT', command=photo_browse_screen.destroy).grid(row=1, column=2)
  can_pic_1.grid(row=0, column=4, padx=(200, 100), sticky=N)
  can_pic_2 = Label(photo_browse_screen, text='Pic 2', font='-weight bold')
  can_pic_2.grid(row=0, column=5, padx=(100, 150), sticky=N)

root = Tk()
root.title('Main menu')
root.geometry('1000x600')
root.resizeable(0, 0)
main_menu = Menu(root)
photos_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Photos', menu=photos_menu)
photos_menu.add_command(label='Browse photos', command=photo_browse)
root.config(menu=main_menu)
root.mainloop()
