'''
A Image Viewer GUI application
'''

# import tkinter from gui
import tkinter as tk
# importing listdir from os module
from os import listdir
# importing Gird from Tkinter
from tkinter import Grid
# importing Image and ImageTk from PIL
from PIL import Image, ImageTk


def resize(image):
    '''
    Resizing the size of image
    :return: new image
    '''
    new_img = image.resize((max(300, image.size[0]//2), max(300, image.size[1]//2)))
    return new_img


def back_click():
    '''
    backward a image
    '''
    global CURRENT, IMAGE_LABEL, FORWARD, BACK
    if CURRENT == 0:
        BACK.config(state=tk.DISABLED)
    else:
        FORWARD.config(state=tk.NORMAL)
        CURRENT -= 1

    image = ImageTk.PhotoImage(resize(Image.open('Images/' + images[CURRENT])))
    IMAGE_LABEL.config(image=image)
    IMAGE_LABEL.image = image


def forward_click():
    '''
    forward a image
    '''
    global CURRENT, IMAGE_LABEL, FORWARD, BACK
    if CURRENT == len(images)-2:
        FORWARD.config(state=tk.DISABLED)
    else:
        BACK.config(state=tk.NORMAL)
        CURRENT += 1

    image = ImageTk.PhotoImage(resize(Image.open('Images/' + images[CURRENT])))
    IMAGE_LABEL.config(image=image)
    IMAGE_LABEL.image = image


if __name__ == "__main__":
    # list of all images
    images = listdir('Images')
    # current image
    CURRENT = 0

    # Creating root window
    root = tk.Tk()
    root.wm_minsize(450, 450)
    root.title('IMAGE VIEWER')

    # initial image
    img = Image.open('Images/'+images[CURRENT])
    img = ImageTk.PhotoImage(resize(img))
    # image label
    IMAGE_LABEL = tk.Label(root, image=img)
    IMAGE_LABEL.grid(row=0, column=1, sticky=tk.E+tk.W+tk.N+tk.S)
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 1, weight=1)

    # Back button
    img_back = Image.open('Back_forward_button/back.jpg')
    img_back.thumbnail((100, 50))
    back_img = ImageTk.PhotoImage(img_back)
    BACK = tk.Button(root, image=back_img, command=back_click)
    BACK.grid(row=0, column=0, sticky=tk.W)

    # Forward Button
    img_forward = Image.open('Back_forward_button/forward.jpg')
    img_forward.thumbnail((100, 50))
    forward_img = ImageTk.PhotoImage(img_forward)
    FORWARD = tk.Button(root, image=forward_img, command=forward_click)
    FORWARD.grid(row=0, column=2, sticky=tk.E)

    root.mainloop()
