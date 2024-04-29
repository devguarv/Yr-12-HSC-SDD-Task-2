from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from os import path

DIR_NAME = path.dirname(path.abspath(__file__)) #Determine the absolute path of a file

#Main Window Creation
root = CTk()
root.title("Trifecta Quest")


default_geometry_x = 600
default_geometry_y = 500

#Initialising the appearance theme for the program
set_appearance_mode("light")

#Creating a local file access for the image to be importedw
arrow_img_path = path.join(DIR_NAME, "Assets", "white arrow.png") #Joins directory with the path of asset, and through the usage of os path it allows for asset to load globally
arrow_img = Image.open("C:\\Users\\devth\\OneDrive\\Desktop\\Assignment\\Yr-12-HSC-SDD-Task-2\\Assets\\white arrow.png")

left_arrow_img_path = path.join(DIR_NAME, "Assets", "left-arrow.png")
left_arrow_img = Image.open("C:\\Users\\devth\\OneDrive\\Desktop\\Assignment\\Yr-12-HSC-SDD-Task-2\\Assets\\left-arrow.png")


# Define the desired smaller size
small_arrow_size = (20, 20)

# Resize the arrow imagew
resize_arrow_img = arrow_img.resize(small_arrow_size)

resize_left_arrow_img = left_arrow_img.resize(small_arrow_size)

# Convert resized image to PhotoImage
v2arrow_img = CTkImage(resize_arrow_img)

v2leftarrow_img = CTkImage(resize_left_arrow_img)

root.geometry("{width}x{height}".format(width=default_geometry_x, height=default_geometry_y))

#Initiliasing the file path for the atom icon
atom_img_path = path.join(DIR_NAME, "Assets", "atom_icon.png")
atom_img = Image.open("C:\\Users\\devth\\OneDrive\\Desktop\\Assignment\\Yr-12-HSC-SDD-Task-2\\Assets\\atom_icon.png")

small_atom_size = (30, 30)

resize_atom_img = atom_img.resize(small_atom_size)

v2atom_img = CTkImage(resize_atom_img)

def to_main_frame():
    global subject_frame, difficulty_frame
    subject_frame.pack_forget()
    difficulty_frame.pack_forget()

   
    container.pack(expand=True, fill=BOTH)



def select_subject():
    global subject_frame
    container.pack_forget() #Removes main container when switched

    subject_frame = CTkFrame(root)
    subject_frame.pack(expand=True, fill=BOTH)

    subject_title_font = ("Arial", 24, UNDERLINE)

    subject_title = CTkLabel(subject_frame, text="Subject Selection", text_color="Black", font=subject_title_font)
    subject_title.place(relx=0.5, rely=0.35, anchor="center")
    
    phys_btn = CTkButton(subject_frame, text="Physics", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=select_difficulty)
    phys_btn.place(relx=0.5, rely=0.5, anchor="center")

    chem_btn = CTkButton(subject_frame, text="Chemistry", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=select_difficulty)
    chem_btn.place(relx=0.5, rely=0.6, anchor="center")

    bio_btn = CTkButton(subject_frame, text="Biology", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=select_difficulty)
    bio_btn.place(relx=0.5, rely=0.7, anchor="center")

    back_btn = CTkButton(subject_frame, text="Back", text_color="White", width=10, image=v2leftarrow_img, compound="left", command=to_main_frame)
    back_btn.place(relx=0.15, rely=0.9, anchor="center")

def select_difficulty():
    global difficulty_frame
    subject_frame.pack_forget() #Removes the previous subject frame

    difficulty_frame = CTkFrame(root)
    difficulty_frame.pack(expand=True, fill=BOTH)

    difficulty_title_font = ("Arial", 24, UNDERLINE)
    difficulty_title = CTkLabel(difficulty_frame, text="Select Difficulty", text_color="Black", font=difficulty_title_font)
    difficulty_title.place(relx=0.5, rely=0.35, anchor="center")

    easy_btn = CTkButton(difficulty_frame, text="Easy", text_color="White", image=v2arrow_img, compound="right", corner_radius=32)
    easy_btn.place(relx=0.5, rely=0.5, anchor="center")

    med_btn = CTkButton(difficulty_frame, text="Medium", text_color="White", image=v2arrow_img, compound="right", corner_radius=32)
    med_btn.place(relx=0.5, rely=0.6, anchor="center")

    hard_btn = CTkButton(difficulty_frame, text="Hard", text_color="White", image=v2arrow_img, compound="right", corner_radius=32)
    hard_btn.place(relx=0.5, rely=0.7, anchor="center")

    back_btn = CTkButton(difficulty_frame, text="Back", text_color="White", width=10, image=v2leftarrow_img, compound="left", command=to_main_frame)
    back_btn.place(relx=0.15, rely=0.9, anchor="center")





def select_options():
    pass


def credits():
    pass

def back_to_main_menu():
    pass


container = CTkFrame(root) #To store the main widgets for simplicity
container.pack(expand=True, fill=BOTH)

#Creating title label
title_font = ("Arial", 30)
title_label = CTkLabel( container, text="Trifecta Quest", text_color="Black", font= title_font, image=v2atom_img, compound="right")
title_label.place(relx=0.5, rely=0.35, anchor="center")

# Creating the begin button
begin_btn = CTkButton(container, text="Begin", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command= select_subject)
begin_btn.place(relx=0.5, rely=0.5, anchor="center")

#Creating options button
options_btn = CTkButton(container, text="Options", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=select_options)
options_btn.place(relx=0.5, rely=0.6, anchor="center")

#Creating the credits button
credits_btn = CTkButton(container, text="Credits", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=credits)
credits_btn.place(relx=0.5, rely=0.7, anchor="center")






root.mainloop()