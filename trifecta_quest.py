from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from os import path
from quiz_data import questions

DIR_NAME = path.dirname(path.abspath(__file__)) #Determine the absolute path of a file

#Main Window Creation
root = CTk()
root.title("Trifecta Quest")

default_geometry_x = 600
default_geometry_y = 500

root.minsize(width=default_geometry_x, height=default_geometry_y)

#Initialising the appearance theme for the program
set_appearance_mode("light")

#Create Global Varibles for Frame Switching
subject_frame = CTkFrame(root)
difficulty_frame = CTkFrame(root)
options_frame = CTkFrame(root)
quiz_frame = CTkFrame(root)
credits_frame = CTkFrame(root)
quiz_progress = CTkFrame(root)
final_score_frame = CTkFrame(root)
global subject_difficulty_text
subject_difficulty_text = ""
check_label1 = None
check_label2 = None
score = 0 #Tracks Quiz Score
quiz_restarted = False #Flag variable indicating whether the quiz has been restarted
# Global Font Style Variable
global_font_style = ("Arial", 15)
font_size_var = StringVar(value="12")
container = CTkFrame(root) #To store the main widgets for simplicity
container.pack(expand=True, fill=BOTH)

global_font_family = "Arial"
global_font_size = 12

answer_radiobuttons = []
selection = IntVar


#Creating a local file access for the image to be imported
arrow_img_path = path.join(DIR_NAME, "Assets", "white arrow.png") #Joins directory with the path of asset, and through the usage of os path it allows for asset to load globally
left_arrow_img_path = path.join(DIR_NAME, "Assets", "left-arrow.png")
atom_img_path = path.join(DIR_NAME, "Assets", "atom_icon.png")


# Define, resize and load the desired smaller size for icons 
small_arrow_size = (20, 20)
arrow_img = Image.open(arrow_img_path).resize(small_arrow_size)
left_arrow_img = Image.open(left_arrow_img_path).resize(small_arrow_size)
small_atom_size = (30, 30)
atom_img = Image.open(atom_img_path).resize(small_atom_size)


# Convert resized image to PhotoImage
v2arrow_img = CTkImage(arrow_img)
v2leftarrow_img = CTkImage(left_arrow_img)
v2atom_img = CTkImage(atom_img)

def apply_theme(theme):
    themes = {
        "Light": "#FFFFFF",
        "Dark" : "#2E2E2E",
        "Blue" : "#87CEEB"
    }
    root.configure(bg=themes[theme])
    for frame in [subject_frame, difficulty_frame, options_frame, quiz_frame, credits_frame, final_score_frame, quiz_progress, container, toggle_menu_frame]:
        frame.configure(bg=themes[theme])


def update_font_size_combobox(event=None):
    global global_font_style, global_font_family
    selected_font_family = font_style_options.get()
    selected_font_size = int(font_size_var.get())
    global_font_family = selected_font_family
    global_font_style = (global_font_family, selected_font_size)
    apply_font_style()
    update_title_font_size()
    
def apply_font_style():
    def update_widget_font(widget):
        if isinstance(widget, (CTkLabel, CTkButton, CTkRadioButton, CTkComboBox)):
            widget.configure(font=global_font_style)
            widget.update()
        for child in widget.winfo_children():
            update_widget_font(child)
    update_widget_font(root)

def make_buttons_bigger():
    main_buttons = [begin_btn, options_btn, credits_btn]
    for button in main_buttons:
        button.configure(font=(global_font_style[0], global_font_style[1] + 8))

def update_title_font_size():
    global title_label, global_font_style
    selected_font_size = int(font_size_var.get())
    title_font = (global_font_style[0], selected_font_size + 12)
    title_label.configure(font=title_font)

quiz_radiobuttons_created = False

# Allows for the recreation of radiobuttons after quiz has been completed / user selects a different frame
def recreate_radiobuttons():
    global answer_radiobuttons, selection
    for radiobutton in answer_radiobuttons: 
        radiobutton.destroy()
        question_label.configure(text="") #Clears the question label, so it does not overlap
    answer_radiobuttons.clear() #Clears previous radiobutton options, so it is not saved

    placement_map = [(0.3, 0.5), (0.6, 0.5), (0.3, 0.7), (0.6, 0.7)]
    for i in range(4):
        radiobutton = CTkRadioButton(quiz_frame, text="", variable=selection, value=i, command=lambda: submit_answer_button.configure(state="normal"))
        radiobutton.configure(font=global_font_style)  # Apply global font style to radio buttons
        answer_radiobuttons.append(radiobutton)
        radiobutton.place(relx=placement_map[i][0], rely=placement_map[i][1], anchor="center")




def place_quiz_widgets():
    global question_label, answer_radiobuttons, quiz_frame, selection, submit_answer_button, subject_difficulty_text, selected_font_size

    quiz_frame.pack(expand=True, fill=BOTH)
    toggle_menu_frame.place_forget()

    selected_font_size = int(font_size_var.get())

    subject_difficulty_font = (global_font_style[0], selected_font_size + 12, "roman", "underline")

    subject_difficulty_label = CTkLabel(quiz_frame, text=subject_difficulty_text, font=subject_difficulty_font)
    subject_difficulty_label.place(relx=0.2, rely=0.2, anchor="center")

    question_lbl_font = (global_font_style[0], selected_font_size + 4)

    question_label = CTkLabel(quiz_frame, text="", font=question_lbl_font)
    question_label.place(relx=0.5, rely=0.35, anchor="center")

    submit_answer_button = CTkButton(quiz_frame, text="Submit", command=on_submit, state="disabled")
    submit_answer_button.place(relx=0.5, rely=0.9, anchor="center")

    selection = IntVar()
    placement_map = [(0.3, 0.5), (0.6, 0.5), (0.3, 0.7), (0.6, 0.7)]

    answer_radiobuttons = []
    for i in range(4):
        radiobutton = CTkRadioButton(quiz_frame, text="", variable=selection, value=i, command=lambda: submit_answer_button.configure(state="normal"))
        radiobutton.configure(font=global_font_style)  # Apply global font style to radio buttons
        answer_radiobuttons.append(radiobutton)
        radiobutton.place(relx=placement_map[i][0], rely=placement_map[i][1], anchor="center")

    apply_font_style()  # Apply font style after


def hide_toggle_menu_frame():
    global toggle_menu_frame
    if toggle_menu_frame is not None:
        toggle_menu_frame.pack_forget()


def hide_all_frames_except(frame_to_show):
    global subject_frame, difficulty_frame, options_frame, quiz_frame, credits_frame, final_score_frame, toggle_menu_frame
    frames = [subject_frame, difficulty_frame, options_frame, quiz_frame, credits_frame, final_score_frame, toggle_menu_frame]
    for frame in frames:
        if frame != frame_to_show:
            frame.pack_forget()

def to_main_frame():
    global subject_frame, difficulty_frame, options_frame, answer_radiobuttons
    container.pack(expand=True, fill=BOTH)
    hide_toggle_button()
    hide_all_frames_except(subject_frame)
    hide_check_labels()
    
    
    if subject_frame is not None:
        subject_frame.pack_forget()

    if difficulty_frame is not None:
        difficulty_frame.pack_forget()

    if options_frame is not None:
        options_frame.pack_forget()

    if credits_frame is not None:
        credits_frame.pack_forget()

    hide_toggle_menu_frame()
    toggle_menu_button.configure(text="☰")  # Reset the toggle button text

def to_subject_frame():
    global subject_frame, difficulty_frame, options_frame
    subject_frame.pack(expand=True, fill=BOTH)
    show_toggle_button()

    if difficulty_frame is not None:
        difficulty_frame.pack_forget()

    if options_frame is not None:
        options_frame.pack_forget()

    hide_toggle_menu_frame()
    toggle_menu_button.configure(text="☰")  # Reset the toggle button text

def select_options():
    global options_frame, font_style_options
    container.pack_forget()  # Removes the main container that holds the 3 options = Begin, Options, Credits
    show_toggle_button()

    hide_all_frames_except(options_frame)

    options_frame = CTkFrame(root)
    options_frame.pack(expand=True, fill=BOTH)

    font_style_lbl_settings = (global_font_style[0], 15, UNDERLINE)
    options_title_lbl_settings = (global_font_style[0], 24, UNDERLINE)

    options_lb = CTkLabel(options_frame, text="Options", text_color="Black", font=options_title_lbl_settings)
    options_lb.place(relx=0.3, rely=0.2)

    font_style_label = CTkLabel(options_frame, text="Font Style:", font=font_style_lbl_settings, text_color="Black")
    font_style_label.place(relx=0.37, rely=0.3)

    font_style_options = CTkComboBox(options_frame, values=["Arial", "Calibri", "Times New Roman"], command=update_font_size_combobox)
    font_style_options.place(relx=0.5, rely=0.3)

    font_size_label = CTkLabel(options_frame, text="Font Size:")
    font_size_label.place(relx=0.37, rely=0.4)

    font_size_options = CTkComboBox(options_frame, values=[str(i) for i in range(8, 21, 2)], variable=font_size_var)
    font_size_options.place(relx=0.62, rely=0.42, anchor="center")

    theme_label = CTkLabel(options_frame, text="Theme:")
    theme_label.place(relx=0.37, rely=0.5)

    theme_options = CTkComboBox(options_frame, values=["Light","Dark","Blue"], command=apply_theme)
    theme_options.place(relx=0.5, rely=0.5)

    # Bind the font size option change directly to update_font_size function
    font_size_options.bind("<<ComboboxSelected>>", update_font_size_combobox)

    font_size_options.bind("<<ComboboxSelected>>", lambda event: update_title_font_size())

    back_btn = CTkButton(options_frame, text="Back", text_color="White", width=10, image=v2leftarrow_img, compound="left", command=to_main_frame)
    back_btn.place(relx=0.15, rely=0.9, anchor="center")

    # Adjust position of the toggle menu frame to the left
    toggle_menu_frame.pack(fill=Y, side=LEFT)

    hide_toggle_menu_frame()
    toggle_menu_button.configure(text="☰")  # Reset the toggle button text

    apply_font_style()  # Apply font style after creating options frame

def to_credits():
    global credits_frame, quiz_frame
    # Remove Initial Frame

    if quiz_frame.winfo_ismapped():
        quiz_frame.pack_forget()
    if subject_frame.winfo_ismapped():
        subject_frame.pack_forget()
    if difficulty_frame.winfo_ismapped():
        difficulty_frame.pack_forget()

    container.pack_forget()
    show_toggle_button()

    credits_frame = CTkFrame(root)
    credits_frame.pack(expand=True, fill=BOTH)

    title_font = ("Arial", 24, UNDERLINE)
    credits_title_lbl = CTkLabel(credits_frame, text="Credits", text_color="Black", font=title_font, anchor="center")
    credits_title_lbl.place(relx=0.2, rely=0.1)

    status_lbl = CTkLabel(credits_frame, text="Status of Program: Open Source", text_color="Green", anchor="center")
    status_lbl.place(relx=0.37, rely=0.04)

    job1_lbl = CTkLabel(credits_frame, text="Lead Developer: ", text_color="Black", anchor="center")
    job1_lbl.place(relx=0.2, rely=0.2)

    job2_lbl = CTkLabel(credits_frame, text="Project Manager: ", text_color="Black", anchor="center")
    job2_lbl.place(relx=0.2, rely=0.3)

    job3_lbl = CTkLabel(credits_frame, text="UI Designer: ", text_color="Black", anchor="center")
    job3_lbl.place(relx=0.2, rely=0.4)

    job4_lbl = CTkLabel(credits_frame, text="System Designer: ", text_color="Black", anchor="center")
    job4_lbl.place(relx=0.2, rely=0.5)

    job5_lbl = CTkLabel(credits_frame, text="Data Analyst: ", text_color="Black", anchor="center")
    job5_lbl.place(relx=0.2, rely=0.6)

    job6_lbl = CTkLabel(credits_frame, text="Scrum Master: ", text_color="Black", anchor="center")
    job6_lbl.place(relx=0.2, rely=0.7)

    devprakash_lbl = CTkLabel(credits_frame, text="Dev Prakash", text_color="Black", anchor="center")
    devprakash_lbl.place(relx=0.4, rely=0.2)

    devprakash1_lbl = CTkLabel(credits_frame, text="Dev Prakash", text_color="Black", anchor="center")
    devprakash1_lbl.place(relx=0.4, rely=0.3)

    devprakash2_lbl = CTkLabel(credits_frame, text="Dev Prakash", text_color="Black", anchor="center")
    devprakash2_lbl.place(relx=0.4, rely=0.4)

    devprakash_lbl3 = CTkLabel(credits_frame, text="Dev Prakash", text_color="Black", anchor="center")
    devprakash_lbl3.place(relx=0.4, rely=0.5)

    devprakash_lbl4 = CTkLabel(credits_frame, text="Dev Prakash", text_color="Black", anchor="center")
    devprakash_lbl4.place(relx=0.4, rely=0.6)

    devprakash_lbl5 = CTkLabel(credits_frame, text="Dev Prakash", text_color="Black", anchor="center")
    devprakash_lbl5.place(relx=0.4, rely=0.7)

    back_button = CTkButton(credits_frame, text="Back", width=10, image=v2leftarrow_img, compound="left",
                             text_color="White", command=to_main_frame)
    back_button.place(relx=0.15, rely=0.9, anchor="center")

    apply_font_style()

def toggle_menu():
    global toggle_menu_frame

    if toggle_menu_frame.winfo_ismapped():
        toggle_menu_frame.place_forget()
    else:
        toggle_menu_frame.place(x=10,y=40)

toggle_menu_button = CTkButton(root, text="☰", width=10, command=toggle_menu)

def create_toggle_menu():
    global toggle_menu_frame
    toggle_menu_frame = CTkFrame(root, width=200, fg_color="Gray")
    

    menu_label = CTkLabel(toggle_menu_frame, text="Side Menu", text_color="White", font=("Arial", 24))
    menu_label.pack(pady=10)
    
    home_label = CTkButton(toggle_menu_frame, text="Home",  command=lambda: (to_main_frame(), recreate_radiobuttons())) #User goes to main frame, and radiobuttons and q label is cleared
    home_label.pack(pady=10)
    
    options_label = CTkButton(toggle_menu_frame, text="Options",command=lambda: (select_options(),recreate_radiobuttons()))
    options_label.pack(pady=10)

    credits_label = CTkButton(toggle_menu_frame, text="Credits",command=lambda: (to_credits, recreate_radiobuttons()))
    credits_label.pack(pady=10)

    toggle_menu_button.place(x=10, y=10)
    apply_font_style()

create_toggle_menu()
   
def show_toggle_button():
    toggle_menu_button.place(x=10, y=10)

def hide_toggle_button():
    global toggle_menu_frame
    if toggle_menu_frame is not None:
        toggle_menu_frame.place_forget()
  


def update_font_size():
    global global_font_style
    selected_font_size = int(font_size_var.get())
    global_font_style (global_font_style[0], selected_font_size)
    apply_font_style()

def select_subject():
    global subject_frame, difficulty_frame, options_frame, quiz_frame, credits_frame
    hide_all_frames()  # Hides other frames when switched to this frame
    hide_check_labels()  # Hides the wrong and right labels from quiz
    container.pack_forget()  # Removes main container when switched
    subject_frame.pack(expand=True, fill=BOTH)
    show_toggle_button()  # Show the toggle button when switched to subject frame

    subject_title_font = (global_font_style[0], 24, UNDERLINE)

    subject_title = CTkLabel(subject_frame, text="1. Select Subject", text_color="Black", font=subject_title_font)
    subject_title.place(relx=0.5, rely=0.35, anchor="center")

    phys_btn = CTkButton(subject_frame, text="⚫ Physics", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=lambda: select_difficulty("Physics"))
    phys_btn.place(relx=0.5, rely=0.5, anchor="center")

    chem_btn = CTkButton(subject_frame, text="⚫ Chemistry", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=lambda: select_difficulty("Chemistry"))
    chem_btn.place(relx=0.5, rely=0.6, anchor="center")

    bio_btn = CTkButton(subject_frame, text="⚫ Biology", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=lambda: select_difficulty("Biology"))
    bio_btn.place(relx=0.5, rely=0.7, anchor="center")

    back_btn = CTkButton(subject_frame, text="Back", text_color="White", width=10, image=v2leftarrow_img, compound="left", command=to_main_frame)
    back_btn.place(relx=0.15, rely=0.9, anchor="center")

    apply_font_style()  # Apply font style after creating subject frame

def select_difficulty(subject):
    global difficulty_frame, toggle_menu_button
    hide_all_frames_except(difficulty_frame)
    hide_check_labels()
    difficulty_frame.pack(expand=True, fill=BOTH)
    show_toggle_button()
    hide_toggle_menu_frame()

    toggle_menu_frame.place_forget()



    difficulty_title_font = ("Arial", 24, UNDERLINE)
    difficulty_title = CTkLabel(difficulty_frame, text="2. Select Difficulty", text_color="Black", font=difficulty_title_font)
    difficulty_title.place(relx=0.5, rely=0.35, anchor="center")

    easy_btn = CTkButton(difficulty_frame, text="⚫ Easy", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command = lambda: start_quiz(subject, "Easy"))
    easy_btn.place(relx=0.5, rely=0.5, anchor="center")

    med_btn = CTkButton(difficulty_frame, text="⚫ Medium", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command =  lambda: start_quiz(subject, "Medium"))
    med_btn.place(relx=0.5, rely=0.6, anchor="center")

    hard_btn = CTkButton(difficulty_frame, text="⚫ Hard", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command =  lambda: start_quiz(subject, "Hard"))
    hard_btn.place(relx=0.5, rely=0.7, anchor="center")

    back_btn = CTkButton(difficulty_frame, text="Back", text_color="White", width=10, image=v2leftarrow_img, compound="left", command=to_subject_frame)
    back_btn.place(relx=0.15, rely=0.9, anchor="center")

    apply_font_style()

  
def on_submit():
    global score
    qset = question_set[0]
    check_answer(qset)

    next_set = next_question(question_set)
    if not next_set: #User is done
        quiz_frame.pack_forget()
        show_final_score()
        
        return
    
    reconfigure_question_info(next_set)
    submit_answer_button.configure(state="disabled")

def hide_all_frames():
    global subject_frame, difficulty_frame, options_frame, quiz_frame, credits_frame, final_score_frame, toggle_menu_frame
    frames = [subject_frame, difficulty_frame, options_frame, quiz_frame, credits_frame, final_score_frame, toggle_menu_frame]
    for frame in frames:
        frame.pack_forget()

def check_answer(qset):
    global check_label1, check_label2, score

    font_checklbl = ("Arial", 16)

    #Initialise check_label1, check_label2
    if check_label1 is None:
        check_label1 = CTkLabel(root, text="", bg_color="#dbdbdb", font=font_checklbl, text_color="Green")
    if check_label2 is None:
        check_label2 = CTkLabel(root, text="", bg_color="#dbdbdb", font=font_checklbl, text_color="Red")

    #place labels off screen
    check_label1.place(relx=-1000, rely=-1000)
    check_label2.place(relx=-1000, rely=-1000)

    if qset[1][selection.get()] == qset[2]:
        #Update the correct label
        score = score + 1 
        check_label1.configure(text="Right ✓")
        check_label1.place(relx=0.75, rely=0.5)
        check_label2.place_forget()
        
    else:
        check_label2.configure(text="Incorrect ✗")
        check_label2.place(relx=0.75, rely=0.5)
        check_label1.place_forget()
    

def reconfigure_question_info(qset):

    #Changes the question label and options based on current item in qset
    question_label.configure(text=qset[0])

    for i, button in enumerate(answer_radiobuttons):
        button.configure(text=qset[1][i])
    selection.set(-1) #Removes the user radiobutton selection

    apply_font_style()

def next_question(qset):
    #Deletes the current question and returns the qset array
    global score

    del qset[0]
    if not qset:
        show_final_score()
        return None
    return qset[0]

def hide_check_labels():
    global check_label1, check_label2
    if check_label1 is not None:
        check_label1.place_forget()
    if check_label2 is not None:
        check_label2.place_forget()

def show_final_score():
    global score, final_score_frame, check_label1, check_label2

    hide_all_frames()

    #Frames to hold final score
    final_score_frame = CTkFrame(root)
    final_score_frame.pack(expand=True, fill=BOTH)

    final_score_label = CTkLabel(final_score_frame, text=f"Your final score is: {score}/20", font=("Arial", 24))
    final_score_label.place(relx=0.5, rely=0.5, anchor="center")

    back_to_subject_btn = CTkButton(final_score_frame, text="Back To Subject", image=v2leftarrow_img, compound="left", command=lambda:(back_to_subject(), recreate_radiobuttons()))
    back_to_subject_btn.place(relx=0.5, rely=0.7)

    apply_font_style()

def restart_quiz():
    global score
    score=0
    select_subject()

def back_to_subject():
    global quiz_restarted
    #Checks if quiz has been restarted
    if quiz_restarted:
        return
    quiz_restarted=True #Set flag variable to true after first restart

    final_score_frame.pack_forget()
    select_subject()

def start_quiz(subject, difficulty):
    global question_set, subject_difficulty_text
    difficulty_frame.pack_forget()
    show_toggle_button()
    hide_toggle_menu_frame()

    question_set = [*questions[subject][difficulty]] #Assigns the questions based of subject and difficulty

    subject_difficulty_text = f"{subject.capitalize()} - {difficulty.capitalize()}" #update the subject_difficulty text with selected subject and difficulty

    place_quiz_widgets() #Places new base widgets for each qeustion

    reconfigure_question_info(question_set[0]) #Initiliase question info




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
credits_btn = CTkButton(container, text="Credits", text_color="White", image=v2arrow_img, compound="right", corner_radius=32, command=to_credits)
credits_btn.place(relx=0.5, rely=0.7, anchor="center")




root.mainloop()