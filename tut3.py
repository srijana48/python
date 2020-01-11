from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("955x945")
image = Image.open("mypic.jpg")
photo = ImageTk.PhotoImage(image)
mic = Label(image = photo)
mic.pack()
root.mainloop()