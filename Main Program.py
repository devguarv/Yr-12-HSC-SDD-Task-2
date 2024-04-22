from tkinter import *
from customtkinter import *


#Main Window Creation
root = CTk()
root.title("Trifecta Quest")


default_font_name = "Arial"
default_font_size = 9
default_geometry_x = 500
default_geometry_y = 500 


root.geometry("{width}x{height}".format(width=default_geometry_x, height=default_geometry_y))

#Creating the begin button
begin_btn = CTkButton(master=root, text="Begin")
begin_btn.place(relx = 0.5, rely=0.5, anchor="center")







root.mainloop()