from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk

#Main Window Creation
root = CTk()
root.title("Trifecta Quest")


default_font_name = "Arial"
default_font_size = 9
default_geometry_x = 500
default_geometry_y = 500 

set_appearance_mode("light")

arrow_img_path = "C:\\Users\\devth\\OneDrive\\Desktop\\Assignment\\Yr-12-HSC-SDD-Task-2\\right-arrow.png"
arrow_img = Image.open(arrow_img_path)
arrow_img = ImageTk.PhotoImage(arrow_img)
resize_arrow_img = arrow_img.resize((100,100))

root.geometry("{width}x{height}".format(width=default_geometry_x, height=default_geometry_y))

#Creating the begin button
begin_btn = CTkButton(master=root, text="Begin", image=arrow_img)
begin_btn.place(relx = 0.5, rely=0.5, anchor="center")







root.mainloop()