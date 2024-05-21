from tkinter import BOTH
from customtkinter import *
from PIL import Image
from os import path

DIR_NAME = path.dirname(path.abspath(__file__))  # Determine the absolute path of a file

# Main Window Creation
root = CTk()
root.title("Trifecta Quest")

default_geometry_x = 600
default_geometry_y = 500

# Initializing the appearance theme for the program
set_appearance_mode("light")

# Global variables for frames
subject_frame = None
difficulty_frame = None
options_frame = None

# Creating a local file access for the images
arrow_img_path = path.join(DIR_NAME, "Assets", "white arrow.png")
left_arrow_img_path = path.join(DIR_NAME, "Assets", "left-arrow.png")
atom_img_path = path.join(DIR_NAME, "Assets", "atom_icon.png")

# Load and resize images
small_arrow_size = (20, 20)
arrow_img = Image.open(arrow_img_path).resize(small_arrow_size)
left_arrow_img = Image.open(left_arrow_img_path).resize(small_arrow_size)
small_atom_size = (30, 30)
atom_img = Image.open(atom_img_path).resize(small_atom_size)

# Convert resized image to CTkImage
v2arrow_img = CTkImage(arrow_img)
v2leftarrow_img = CTkImage(left_arrow_img)
v2atom_img = CTkImage(atom_img)

root.geometry(f"{default_geometry_x}x{default_geometry_y}")

def to_main_frame():
    global subject_frame, difficulty_frame, options_frame
    container.pack(expand=True, fill=BOTH)
    
    if subject_frame is not None:
        subject_frame.pack_forget()
    if difficulty_frame is not None:
        difficulty_frame.pack_forget()
    if options_frame is not None:
        options_frame.pack_forget()

def select_subject():
    global subject_frame
    container.pack_forget()  # Removes main container when switched

    subject_frame = CTkFrame(root)
    subject_frame.pack(expand=True, fill=BOTH)

    subject_title_font = ("Arial", 24, "underline")

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
    subject_frame.pack_forget()  # Removes the previous subject frame

    difficulty_frame = CTkFrame(root)
    difficulty_frame.pack(expand=True, fill=BOTH)

    difficulty_title_font = ("Arial", 24, "underline")
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
    global options_frame
    container.pack_forget()  # Removes the main container that holds the 3 options = Begin, Options, Credits

    options_frame = CTkFrame(root)
    options_frame.pack(expand=True, fill=BOTH)

    font_size_label = CTkLabel(options_frame, text="Font Size", text_color="White", bg_color="#3B8ED0")
    font_size_label.place(relx=0.4, rely=0.5)

    font_size_options = CTkComboBox(options_frame, values=["Arial", "Times New Roman"], command=update_font_size)
    font_size_options.place(relx=0.5, rely=0.5)

    back_btn = CTkButton(options_frame, text="Back", text_color="White", width=10, image=v2leftarrow_img, compound="left", command=to_main_frame)
    back_btn.place(relx=0.15, rely=0.9, anchor="center")

def update_font_size(value):
    print(f"Font size updated to: {value}")

def credits():
    pass

def back_to_main_menu():
    pass

container = CTkFrame(root)  # To store the main widgets for simplicity
container.pack(expand=True, fill=BOTH)

# Creating title label
title_font = ("Arial", 30)
title_label = CTkLabel(container, text="Trifecta Quest", text_color="Black", font=title_font, image=v2atom_img, compound="right")
title_label.place(relx=0.5, rely=0.35, anchor="center")

# Creating the begin button
begin_btn = CTkButton(container, text="Begin", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=select_subject)
begin_btn.place(relx=0.5, rely=0.5, anchor="center")

# Creating options button
options_btn = CTkButton(container, text="Options", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=select_options)
options_btn.place(relx=0.5, rely=0.6, anchor="center")

# Creating the credits button
credits_btn = CTkButton(container, text="Credits", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=credits)
credits_btn.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()