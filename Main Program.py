from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk

#Main Window Creation
root = CTk()
root.title("Trifecta Quest")


default_geometry_x = 500
default_geometry_y = 500

set_appearance_mode("light")

arrow_img_path = "C:\\Users\\devth\\OneDrive\\Desktop\\Assignment\\Yr-12-HSC-SDD-Task-2\\arrow-24-24.png"
arrow_img = Image.open(arrow_img_path)

# Define the desired smaller size
small_arrow_size = (20, 20)

# Resize the arrow image
resize_arrow_img = arrow_img.resize(small_arrow_size)

# Convert resized image to PhotoImage
img = ImageTk.PhotoImage(resize_arrow_img)

root.geometry("{width}x{height}".format(width=default_geometry_x, height=default_geometry_y))

# Creating the begin button
begin_btn = CTkButton(master=root, text="Begin", text_color="White", image=img, compound="right")
begin_btn.place(relx=0.5, rely=0.5, anchor="center")







root.mainloop()