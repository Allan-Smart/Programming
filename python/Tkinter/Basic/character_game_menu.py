
# Import libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Tkinter main window
root = tk.Tk()
root.geometry('300x500')
root.resizable(False, False)
root.title('Character Selection')
root.config(background = 'grey')

# --------------------------------
#           Functions
# --------------------------------

# Starting class
def starting_class_handler(event):

    selected_class = starting_class_select.curselection()

# Starting gift
def starting_gift_handler(event):

    starting_gift_comboxbox.get()

def displaying_results():

    pass


# --------------------------------
#           Variables
# --------------------------------

name =              tk.StringVar()
gender =            tk.StringVar()  
starting_gift =     tk.StringVar()

# --------------------------------
#           Main Code
# --------------------------------

# Character LabelFrame
character_frame = ttk.Frame(root)
character_frame.pack(pady = 10)

opener = ttk.Label(character_frame, text = 'Character Details:')
opener.pack()

# Enter name details
name_frame = ttk.Frame(root)
name_frame.pack(pady = 10)

enter_name = ttk.Label(name_frame, text = 'Enter Name:')
enter_name.pack(side = 'left')
enter_name_entry = ttk.Entry(name_frame, textvariable = name)
enter_name_entry.pack(side = 'right')

# Select Gender
gender_frame = ttk.Frame(root)
gender_frame.pack(pady = 10)

gender_label = ttk.Label(gender_frame, text = 'Select Gender:')
gender_label.pack()

select_gender_male = ttk.Radiobutton(gender_frame, text = 'Male', value = 'm',  variable = gender)
select_gender_male.pack(side = 'left')

select_gender_female = ttk.Radiobutton(gender_frame, text = 'Female', value = 'f',  variable = gender)
select_gender_female.pack(side = 'right')

# Select class
starting_class_frame = ttk.Frame(root)
starting_class_frame.pack(pady = 10)

starting_class_label = ttk.Label(starting_class_frame, text = 'Select Starting Class:')
starting_class_label.pack()

starting_class = ('Warrior',
                  'Rogue',
                  'Mage',
                  'Vagabond')

starting_class =    tk.StringVar(value = starting_class) 
starting_class_select = tk.Listbox(starting_class_frame, listvariable = starting_class, height = 4)
starting_class_select.pack()

starting_class_select.bind('<<ListboxSelect>>', )

# Starting gift
starting_gift_frame = ttk.Frame(root)
starting_gift_frame.pack(pady = 10)

starting_gift_label = ttk.Label(starting_gift_frame, text = 'Select Starting Gift:')
starting_gift_label.pack()

starting_gift_comboxbox = ttk.Combobox(starting_gift_frame, textvariable = starting_gift, width = 25)
starting_gift_comboxbox['values'] = ('Health Ring - Plus 10 to health',
                                     'Magic Ring - Plus 10 to magic',
                                     '10x Fire Bombs',
                                     'Teleport Ring',
                                     'None')
starting_gift_comboxbox['state'] = 'readonly'
starting_gift_comboxbox.pack()

starting_gift_comboxbox.bind('<<ComboboxSelected>>', starting_gift_handler)

# Displaying Result



# Tkinter mainloop
root.mainloop()

