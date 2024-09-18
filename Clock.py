from tkinter import *
from PIL import Image, ImageTk
from time import strftime

def close_window():
    root.destroy()

root = Tk()
root.geometry('875x500')
root.resizable(False, False)
root.title('Spectral Seconds')

icon = PhotoImage(file='img/skull.png')
root.iconphoto(False, icon)

img = Image.open('img/bg2.png')
img = img.resize((875,500))
img = ImageTk.PhotoImage(img)

canvas = Canvas(root, width = 875, height = 500, highlightthickness = 0)
canvas.place(x = 0, y = 0)
canvas.create_image(0, 0, image = img, anchor = 'nw')
clock_time = canvas.create_text(420,250, font = ('YouMurderer BB', 115), fill = '#7e7c67')

def update_time():
    curr_time = strftime('%I:%M:%S %p')
    canvas.itemconfig(clock_time, text=curr_time)
    root.after(1000, update_time)

update_time()

root.mainloop()