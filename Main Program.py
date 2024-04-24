from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk

#Main Window Creation
root = CTk()
root.title("Trifecta Quest")


default_geometry_x = 500
default_geometry_y = 500

#Initialising the appearance theme for the program
set_appearance_mode("light")

#Creating a local file access for the image to be imported
arrow_img_path = "C:\\Users\\devth\\OneDrive\\Desktop\\Assignment\\Yr-12-HSC-SDD-Task-2\\arrow-24-24.png"
arrow_img = Image.open(arrow_img_path)

# Define the desired smaller size
small_arrow_size = (20, 20)

# Resize the arrow imagew
resize_arrow_img = arrow_img.resize(small_arrow_size)

# Convert resized image to PhotoImage
img = ImageTk.PhotoImage(resize_arrow_img)

root.geometry("{width}x{height}".format(width=default_geometry_x, height=default_geometry_y))

#Initiliasing the file path for the atom icon
atom_img_path = "C:\\Users\\devth\\OneDrive\\Desktop\\Assignment\\Yr-12-HSC-SDD-Task-2\\atom_icon-removebg-preview.png"
atom_img = Image.open(atom_img_path)

small_atom_size = (30, 30)

resize_atom_img = atom_img.resize(small_atom_size)

v2atom_img = ImageTk.PhotoImage(resize_atom_img)

#Creating title label
title_font = ("Arial", 30)
title_label = CTkLabel(master=root, text="Trifecta Quest", text_color="Black", font= title_font, image=v2atom_img, compound="right")
title_label.place(relx=0.5, rely=0.35, anchor="center")

# Creating the begin button
begin_btn = CTkButton(master=root, text="Begin", text_color="White", image=img, compound="right", corner_radius=32)
begin_btn.place(relx=0.5, rely=0.5, anchor="center")

#Creating options label
title_font




root.mainloop()