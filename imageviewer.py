from tkinter import *
from tkinter import filedialog, messagebox
import PIL, time
from PIL import Image, ImageTk

global img 
root = Tk(className="Image viewer")
root.config(bg="grey")
root.geometry("1280x720")
Label(text='Before:                                                                                                                          After:', font='Arial 14', width=10000, height=1).pack()

def compress(path):
    picture = Image.open(path)
    picture.save("path.jpg",optimize=True,quality=1)

def browseFile():
    global path 
    path = filedialog.askopenfilename()
    compress(path)
    showImages()

def showImages():
    print(path)
    pastImg = ImageTk.PhotoImage(Image.open(path).resize((640, 360), Image.ANTIALIAS))
    panelPast = Label(root, image=pastImg, bg="grey")
    panelPast.pack(side = "left", fill = "both", expand = "yes")
    presentImg = ImageTk.PhotoImage(Image.open("path.jpg").resize((640, 360), Image.ANTIALIAS))
    panelPresent = Label(root, image=presentImg, bg="grey")
    panelPresent.pack(side = "right", fill = "both", expand = "yes")
    root.mainloop()
  
button = Button(root,text="Open",command=browseFile)
button.pack(side=BOTTOM)

root.mainloop()