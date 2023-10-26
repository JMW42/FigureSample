#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk





# GUI
#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("1200x600")

#Create a canvas
canvas= Canvas(win, width= 600, height= 600)
canvas.pack()

#Load an image in the script
img = Image.open("testimages/sine.png")
resized_image= img.resize((600,600), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10,anchor=NW,image=new_image)

win.mainloop()
