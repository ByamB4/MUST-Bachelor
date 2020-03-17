#!/usr/bin/env python3

from tkinter import *
from PIL import ImageTk, Image
from skimage.measure import compare_ssim
import cv2
import numpy as np
 
# Global items
IMAGE_1 = 'nature.jpg'
IMAGE_2 = 'nature-fixed.jpg'

class Window():
  def __init__(self, master):
    self.master = master
    master.geometry('930x700')
    master.resizable(0, 0)
    master.title('l3yam134')
    master.configure(background='#293151')
    self.initUI()

  def initUI(self):
    LeftTopLabelText = Label(self.master, text='Зураг 1')
    LeftTopLabelText.config(font=('Lato', 20))
    LeftTopLabelText.place(x=130, y=10)

    self.LeftImage = ImageTk.PhotoImage(Image.open('./Images/' + IMAGE_1).resize((400, 400)))
    LeftTopLabelText = Label(self.master, image=self.LeftImage)
    LeftTopLabelText.place(x=20, y=80)

    RightTopLabelText = Label(self.master, text='Зураг 2')
    RightTopLabelText.config(font=('Lato', 20))
    RightTopLabelText.place(x=650, y=10)

    self.RightImage = ImageTk.PhotoImage(Image.open('./Images/' + IMAGE_2).resize((400, 400)))
    self.RightTopLabelText = Label(self.master, image=self.RightImage)
    self.RightTopLabelText.place(x=500, y=80)

    BottomFrame = Frame(self.master, background='green', width=110, height=10)
    BottomFrame.place(x=20, y=500)

    self.Texts = Text(BottomFrame, height=20, width=110)
    self.Texts.pack(side=LEFT)

    RunButton = Button(self.master, height=1, width=3, command=self.process, text='Run')
    RunButton.place(x=430, y=450)

  def process(self):
    self.Texts.insert(END, '[+] Working...')
    before = cv2.imread('./Images/' + IMAGE_1)
    after = cv2.imread('./Images/' + IMAGE_2)

    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)
    (score, diff) = compare_ssim(before_gray, after_gray, full=True)

    diff = (diff * 255).astype("uint8")
    self.Texts.insert(END, '\n[+] Image similarity: ' + str(score))
    self.Texts.insert(END, '\n[+] Diff: ' + str(diff))

    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV |
    cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    mask = np.zeros(before.shape, dtype='uint8')
    filled_after = after.copy()
    for c in contours:
      area = cv2.contourArea(c)
      if area > 40:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(before, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.rectangle(after, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.drawContours(mask, [c], 0, (0,255,0), -1)
        cv2.drawContours(filled_after, [c], 0, (0,255,0), -1)
    cv2.imwrite('out.jpg', after)
    self.Texts.insert(END, '\n[+] File saved name: out.jpg')
    self.Texts.insert(END, '\n[+] Trying to change image')
    self.updatedImage = ImageTk.PhotoImage(Image.open('out.jpg').resize((400, 400)))
    self.RightTopLabelText.configure(image=self.updatedImage)
    self.RightTopLabelText.image = self.updatedImage
    self.Texts.insert(END, '\n[+] Changed successfully')
if __name__ == '__main__':
  root = Tk()
  window = Window(root)
  root.mainloop()
