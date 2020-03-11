# Didn't fixed width, but it shows 4 image :P
import matplotlib
matplotlib.use('Agg')
from tkinter import *
from tkinter import messagebox as tkMessageBox
from PIL import ImageTk, Image

def photo_browse():
  def add_photo(screen, column_num):
    if not "pic" in globals():
      tkMessageBox.showerror("Error!", "No picture selected!")
      screen.lift ()
    else:
      screen.image = pic
      can = Label(screen, image=pic)
      can.grid(row=0, column=column_num)
      Label(screen, text=chosen_photo).grid (row=1, column=column_num)
  def selection_listbox(evt):
    global chosen_photo
    chosen_photo = str(photo_listbox.get(photo_listbox.curselection()))
    image_location = "Pics/" + chosen_photo
    global pict
    pict = Image.open(image_location)
    global pic
    pic = ImageTk.PhotoImage(pict)
  import glob
  photo_browse_screen = Toplevel()
  photo_browse_screen.title("Photo browse")
  photo_browse_screen.geometry("2000x2000")
  photo_listbox = Listbox(photo_browse_screen, width=50, height=25)
  photo_listbox.grid(columnspan=3)
  photo_listbox.bind('<<ListboxSelect>>', selection_listbox)
  name_list = glob.glob("Pics/*.png")
  name_list = [i[5:] for i in name_list]
  name_list.sort()
  n = 1
  m = 0
  for i in name_list:
    photo_listbox.insert(n, name_list[m])
    n += 1
    m += 1
  Button(photo_browse_screen, text="PIC 1", command=lambda:add_photo(photo_browse_screen, 4)).grid(row=1,column=0)
  Button(photo_browse_screen, text="PIC 2", command=lambda:add_photo(photo_browse_screen, 5)).grid(row=1, column=1)
  Button(photo_browse_screen, text="PIC 3", command=lambda:add_photo(photo_browse_screen, 6)).grid(row=1, column=2)
  Button(photo_browse_screen, text="PIC 4", command=lambda:add_photo(photo_browse_screen, 7)).grid(row=1, column=3)
  Button(photo_browse_screen, text="EXIT", command=photo_browse_screen.destroy).grid(row=1, column=4)
  can_pic_1 = Label(photo_browse_screen, text="Pic 1", font="-weight bold")
  can_pic_1.grid(row=0, column=4, padx=(200, 100), sticky=N)
  can_pic_2 = Label(photo_browse_screen, text="Pic 2", font="-weight bold")
  can_pic_2.grid(row=0, column=5, padx=(100, 150), sticky=N)
  can_pic_3 = Label(photo_browse_screen, text="Pic 3", font="-weight bold")
  can_pic_3.grid(row=0, column=6, padx=(100, 150), sticky=N)
  can_pic_4 = Label(photo_browse_screen, text="Pic 4", font="-weight bold")
  can_pic_4.grid(row=0, column=7, padx=(100, 150), sticky=N)
root = Tk()
root.title("Main menu")
root.geometry("1000x600")
root.resizable(0, 0)
main_menu = Menu(root)
photos_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Photos", menu=photos_menu)
photos_menu.add_command(label="Browse photos", command=photo_browse)
root.config(menu=main_menu)
root.mainloop()
