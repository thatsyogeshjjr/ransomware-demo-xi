import tkinter
from tkinter import *
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--image',help="image to display")
parser.add_argument('-t','--text',help="text to display with image")
option = parser.parse_args()
# to use option.image
print(option.text)

win = Tk()
file = option.image
info = Image.open(file)
frames = info.n_frames
print(frames)
im = [tkinter.PhotoImage(file=file,format=f'gif -index {i}')for i in range(frames)]

anim=None
count=0
def animation(count):
    im2 = im[count]
    gif_label.configure(image=im2)
    count+=1
    if count == frames:
        count=0

    anim = win.after(30,lambda:animation(count))

Label(win,text=option.text,font="Arial 30").pack()
gif_label = Label(image="")
gif_label.pack()
animation(count)


win.mainloop()