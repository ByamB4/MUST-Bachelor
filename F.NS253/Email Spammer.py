#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
  # Author : Byambadalai Sumiya
  # Date   : 01-03-2020
"""
from tkinter import *
from tkinter import filedialog
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib, sys

"""
  Some valid accounts = {
      [byambatest7@gmail.com, weakpassword123], maybe not works future
      [byambatest8@gmail.com, weakpassword123]  maybe not works future
"""
class GUI(Frame):
  def callback(self, event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
  def OpenFile(self):
    self.statusText.set('Файлаа сонгож байна...')
    tmp = filedialog.askopenfilename(initialdir="/home/l3yam134/Documents",
                           filetypes =(("Image File", "*.jpg"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    self.direc.set(tmp)
    # print(self.direc.get())  
  def finish(self):
    self.msg['From'] = str(self.email_user.get())
    self.msg['Subject'] = str(self.email_subject.get()) 
    self.statusText.set('Спамдаж байна...')
    self.body = self.entryTxt.get("1.0", 'end-1c')
    self.msg.attach(MIMEText(self.body, 'plain'))
    self.filename = self.direc.get()
    if self.filename != '':
      self.attachment = open(self.filename, 'rb')
      self.part = MIMEBase('application','octet-stream')
      self.part.set_payload((self.attachment).read())
      encoders.encode_base64(self.part)
      self.part.add_header('Content-Disposition',"attachment; filename= " + self.filename)
      self.msg.attach(self.part)
    
    self.text = self.msg.as_string()
    if self.req.get() is 1:
      self.server = smtplib.SMTP('smtp.gmail.com', 587)
    else:
      self.server = smtplib.SMTP('smtp.yahoo.com', 25)
    self.server.starttls()
    try:
      self.server.login(self.email_user.get(), self.email_password.get())
      self.email_send = self.victim.get()
      for i in range (1, self.scale.get() + 1):
        self.server.sendmail(self.email_user.get(), self.email_send, self.text)
        self.statusText.set('Спамминг мейл ' + str(i) + '...')
    except Exception as e:
      print('Run time error : ', e)
      sys.exit(0)
    self.server.quit()
  
  def testScene(self):
    print(self.victim.get())
  def doNothing(self):
    print('Sorry i cant now')
  def newFile(self):
    self.entrySenderMail.delete(0, 'end')
    self.entrySenderPassword.delete(0, 'end')
    self.entrySubject.delete(0, 'end')
    self.entryTxt.delete('1.0', END)
    self.entryVictim.delete(0, 'end')
    self.direc.set('')

  def __init__(self):
    self.direc = StringVar()
    self.statusText = StringVar()
    self.msg = MIMEMultipart()
    self.statusText.set('Ажиллаж байна...')
    
    super().__init__()
    self.initUI()

  def initUI(self):  
    self.master.title("Mail Spammer #l3yam134")
    self.pack(fill=BOTH, expand=True)
    self.label = StringVar()
    # **************** Main Frames *******************
    frame1 = Frame(self)
    frame1.pack(fill=BOTH)
    frame2 = Frame(self)
    frame2.pack(fill=BOTH)
    frame3 = Frame(self)
    frame3.pack(fill=BOTH)
    frame4 = Frame(self)
    frame4.pack(fill=BOTH)
    frame5 = Frame(self)
    frame5.pack(fill=BOTH)
    frame8 = Frame(self)
    frame8.pack(fill=BOTH)
    frame9 = Frame(self)
    frame9.pack(fill=BOTH)
    frame6 = Frame(self)
    frame6.pack(fill=BOTH)
    frame7 = Frame(self)
    frame7.pack(fill=BOTH)
    
    # **************** Frame 1 ************************
    lbl1 = Label(frame1, text='Илгээгчийн Мейл Хаяг      : ', width=25)
    lbl1.pack(side=LEFT, padx=5, pady=5)
    self.email_user = StringVar()
    self.entrySenderMail = Entry(frame1, bd=1, text='Your name', width=30, textvariable=self.email_user)
    self.entrySenderMail.pack(side=LEFT)
    self.entrySenderMail.bind('<Control-KeyRelease-a>', self.callback)
    # **************** Frame 2 ************************
    lbl2 = Label(frame2, text='Илгээгчийн Мейл Нууц Үг : ', width=25)
    lbl2.pack(side=LEFT, padx=5, pady=2)
    self.email_password = StringVar()
    self.entrySenderPassword = Entry(frame2, bd=1, text='Your password', width=30, show='*', textvariable=self.email_password)
    self.entrySenderPassword.pack(side=LEFT)
    self.entrySenderPassword.bind('<Control-KeyRelease-a>', self.callback)
    # **************** Frame 3 ************************
    lbl3 = Label(frame3, text='Сэдэв', width = 6)
    lbl3.pack(side=LEFT, padx=5, pady=5)
    self.email_subject = StringVar()
    self.entrySubject = Entry(frame3, width=44, textvariable=self.email_subject)
    self.entrySubject.pack(side=LEFT, padx=45, pady=5)
    self.entrySubject.bind('<Control-KeyRelease-a>', self.callback)
    # **************** Frame 4 ************************
    lbl4 = Label(frame4, text='Мэндчилгээ', width=10)
    lbl4.pack(side=LEFT, padx=10, pady=5, anchor=N)
    self.entryTxt = Text(frame4, width=44, height=20)
    self.entryTxt.pack(side=LEFT, pady=5, padx=5)
    self.entryTxt.bind('<Control-KeyRelease-a>', self.callback)
    # **************** Frame 5 ************************
    btt5 = Button(frame5, text='Файл сонгох', command=self.OpenFile, relief=RAISED)
    btt5.pack(side=LEFT, padx=5, pady=5)
    lbl5 = Label(frame5, textvariable=self.direc)
    lbl5.pack(side=LEFT, pady=5, padx=5)
    # **************** Frame 8 ************************
    lbl6 = Label(frame8, text='Спам тоо ', width=10)
    lbl6.pack(side=LEFT, padx=5)
    self.scale = Scale(frame8, orient='horizontal', from_=1, to=50)
    self.scale.pack(side=LEFT, padx=0, pady=0)
    # **************** Frame 9 ************************
    lbl9 = Label(frame9, text='Хохирогч ', width=10)
    lbl9.pack(side=LEFT, padx=5)
    self.victim = StringVar()
    self.entryVictim = Entry(frame9, textvariable=self.victim, width=30)
    self.entryVictim.bind('<Control-KeyRelease-a>', self.callback)
    self.entryVictim.pack(side=LEFT)
    # chk = Button(frame9, command=self.testScene)
    # chk.pack(side=LEFT)
    # **************** Frame 6 ************************
    self.req = IntVar()
    r1 = Radiobutton(frame6, text='Gmail', variable=self.req, value=1)
    r1.invoke()
    r1.pack(side=LEFT, padx=5, pady=5)
    r2 = Radiobutton(frame6, text='Yahoo', variable=self.req, value=2)
    r2.pack(side=LEFT, padx=5, pady=5)
    
    # **************** Frame 7 ************************
    lastButton = Button(frame7, text='СПАМ', command=self.finish, bd=3)
    lastButton.pack(side=LEFT, padx=220, pady=10)
    
    # **************** Menu Bar **********************
    menu = Menu(self)
    window.config(menu=menu)
    subMenu = Menu(menu)
    menu.add_cascade(label='Файл', menu=subMenu)
    subMenu.add_command(label='Шинэ файл...', command=self.newFile)
    subMenu.add_command(label='Хадгалах', command=self.doNothing)
    subMenu.add_separator()
    subMenu.add_command(label='Гарах', command=self.doNothing)
    editMenu = Menu(menu)
    menu.add_cascade(label='Засварлах', menu=editMenu)
    editMenu.add_command(label='Буцах', command=self.doNothing)
    editMenu.add_command(label='Дахин хийх', command=self.doNothing)
    editMenu.add_command(label='Хуулбарлах', command=self.doNothing)
    editMenu.add_command(label='Хуулах', command=self.doNothing)
    # **************** Status Bar ********************
    status = Label(self, textvariable=self.statusText, bd=1, relief=SUNKEN, anchor=W, width=40)
    status.pack(side=BOTTOM, anchor=W, expand=True, fill=X)
if __name__ == '__main__':
  window = Tk()
  window.geometry("600x660")
  app = GUI()
  window.mainloop()
