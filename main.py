# pip install Pillow
from tkinter import *
from tkinter import filedialog
from PIL import Image


def convert():
    img = Image.open(path_to_png.get())
    img.save('output.ico')


root = Tk()
root.title('Конвертор png2ico')
root.geometry('500x200')
root.resizable(0, 0)
root['bg'] = 'green'

path_to_png = Entry(root, width=50, font='Arial 10 bold')
path_to_png.pack(pady=30)

btn_convert = Button(root, text='Конвертировать в ICO', font='Arial 15 bold', command=convert)
btn_convert.pack(pady=40)

root.mainloop()
