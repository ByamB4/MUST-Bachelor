#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

# creates Tkinter window
root = Tk()
# creates window title
root.title('Caesar Cipher')
# allows for window to be resized
root.resizable(True,True)
# window background
root.configure(background='blue')
root.frame_header = ttk.Frame()
ttk.Label(root.frame_header, text = 'Caesar Cipher', style ='Header.TLabel').grid(row = 0, column = 1)
ttk.Label(root.frame_header, text = 'Enter Number (1-25):', style ='Header.TLabel').grid(row = 1, column = 0)
ttk.Label(root.frame_header, text = 'Text:', style ='Header.TLabel').grid(row = 2, column = 0)
ttk.Label(root.frame_header, text='Encrypted/Decrypted/Text:',style='Header.TLabel').grid(row=4, column=0)
# seperated the .grid as it was causing a None type error
enc_dec_text = Text(root.frame_header, width=50, height=20)
enc_dec_text.grid(row=4,column=1)
# cipher shift drop down
cipher_shift_menu = StringVar()
Spinbox(root.frame_header,from_=1, to=25,
textvariable=cipher_shift_menu).grid(row=1, column=1)
# text entry
# seperated the .grid as it was causing a None type error
text_entry = ttk.Entry(root.frame_header, width=100)
text_entry.grid(row=2,column=1)
def encrypt_text():
  stringtoencrypt = text_entry.get()
  stringtoencrypt = str(stringtoencrypt)
  stringtoencrypt=stringtoencrypt.upper()
  ciphershift = cipher_shift_menu.get()
  ciphershift=int(ciphershift)
  stringencrypted=""
  for character in stringtoencrypt:
    position = letters.find(character)
    newposition = position+ciphershift
  if character in letters:
    stringencrypted = stringencrypted + letters[newposition]
  else:
    stringencrypted = stringencrypted + character
    enc_dec_text.insert(0, stringencrypted)
def decrypt_text():
  stringtodecrypt = text_entry.get()
  stringtodecrypt = str(stringtodecrypt)
  stringtodecrypt=stringtodecrypt.upper()
  ciphershift = int(cipher_shift_menu.get())
  for i in range(1, 26):
    stringdecrypted=""
    for character in stringtodecrypt:
      position = letters.find(character)
      newposition = position-i
      if character in letters:
        stringdecrypted = stringdecrypted + letters[newposition]
      else:
        stringdecrypted = stringdecrypted + character
    enc_dec_text.insert(END, str(i + 1) + ': ' + stringdecrypted + '\n')
# buttons to encrypt / decrypt
encrypt_button = ttk.Button(root.frame_header,text='Encrypt',command=lambda: encrypt_text()).grid(row=3,column=0)
decrypt_button = ttk.Button(root.frame_header,text='Decrypt',command=lambda: decrypt_text()).grid(row=3,column=1)
root.frame_header.pack()
root.mainloop()
