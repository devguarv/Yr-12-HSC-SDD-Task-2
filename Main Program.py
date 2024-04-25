from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from os import path

DIR_NAME = path.dirname(path.abspath(__file__)) #Determine the absolute path of a file

def select_subject():
    pass

def select_options():
    pass


def credits():
    pass


#Main Window Creation
root = CTk()
root.title("Trifecta Quest")


default_geometry_x = 600
default_geometry_y = 500

#Initialising the appearance theme for the program
set_appearance_mode("light")

#Creating a local file access for the image to be imported
arrow_img_path = path.join(DIR_NAME, "arrow-24-24.png") #Joins directory with the path of asset, and through the usage of os path it allows for asset to load globally
arrow_img = Image.open(arrow_img_path)

# Define the desired smaller size
small_arrow_size = (20, 20)

# Resize the arrow imagew
resize_arrow_img = arrow_img.resize(small_arrow_size)

# Convert resized image to PhotoImage
v2arrow_img = ImageTk.PhotoImage(resize_arrow_img)

root.geometry("{width}x{height}".format(width=default_geometry_x, height=default_geometry_y))

#Initiliasing the file path for the atom icon
atom_img_path = path.join(DIR_NAME, "atom_icon-removebg-preview.png")
atom_img = Image.open(atom_img_path)

small_atom_size = (30, 30)

resize_atom_img = atom_img.resize(small_atom_size)

v2atom_img = ImageTk.PhotoImage(resize_atom_img)

#Creating title label
title_font = ("Arial", 30)
title_label = CTkLabel(master=root, text="Trifecta Quest", text_color="Black", font= title_font, image=v2atom_img, compound="right")
title_label.place(relx=0.5, rely=0.35, anchor="center")

# Creating the begin button
begin_btn = CTkButton(master=root, text="Begin", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=select_subject)
begin_btn.place(relx=0.5, rely=0.5, anchor="center")

#Creating options button
options_btn = CTkButton(master=root, text="Options", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=select_options)
options_btn.place(relx=0.5, rely=0.6, anchor="center")

#Creating the credits button
credits_btn = CTkButton(master=root, text="Credits", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=credits)
credits_btn.place(relx=0.5, rely=0.7, anchor="center")






root.mainloop()