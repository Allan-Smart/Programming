"""

Basic Calculator

Purpose
-------
To calculate the sum of two numbers using basic arithmetic functions 
such as:
    - Addition
    - Subtraction
    - Multiplication
    - Division

Author
------
Allan Smart
Blackbit Analytics © 2026

"""

# Import library
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Tkinter main window
root = tk.Tk()
root.geometry('350x300')
root.resizable(False, False)
root.title('Calculator')
root.config(background='light blue')

# ----------------------------------------------
#           Helper Functions
# ----------------------------------------------
def addition():
    try:
        total = num1.get() + num2.get()
        results.config(text = f'Results: {total:.2f}')
    except tk.TclError:
        messagebox.showerror('Input Error', 'Please enter valid numbers only')

def subtraction():
    try:
        total = num1.get() - num2.get()
        results.config(text = f'Results: {total:.2f}')
    except tk.TclError:
        messagebox.showerror('Input Error', 'Please enter valid numbers only')

def multiplication():
    try:
        total = num1.get() * num2.get()
        results.config(text = f'Results: {total:.2f}')
    except tk.TclError:
        messagebox.showerror('Input Error', 'Please enter valid numbers only')
        
def division():
    try:   
        
        dividend = num1.get()
        divisor = num2.get()
        
        if divisor == 0:
            messagebox.showerror('Warning', 'Cannot divide by zero')
            results.config(text = 'Result: Error')
            return
            
        total = dividend / divisor
        results.config(text = f'Results: {total:.2f}')
        
    except tk.TclError:
        messagebox.showerror('Input Error', 'Please enter valid numbers only')

# ----------------------------------------------
#           Logic Functions
# ----------------------------------------------
def calculation():

    if add.get():
        addition()
    elif sub.get():
        subtraction()
    elif mul.get():
        multiplication()
    elif div.get():
        division()
    else:
        messagebox.showerror('Warning', 'Please select an arithmetic function to calculate')

# Ensure only one option can be selected
def only_one_selected(selected_var):
    for var in all_vars:
        if var != selected_var:
            var.set(0)

def clear_screen():
    
    num1.set(0.0)
    num2.set(0.0)
    
    for var in all_vars:
        var.set(False)
        
    results.config(text='Results: 0')

# ----------------------------------------------
#           Variables
# ----------------------------------------------

# Number variables
num1 = tk.DoubleVar()
num2 = tk.DoubleVar()

# Arithmetic variables
add = tk.BooleanVar(value = False)
sub = tk.BooleanVar(value = False)
mul = tk.BooleanVar(value = False)
div = tk.BooleanVar(value = False)


all_vars = [add, sub, mul, div]

# ----------------------------------------------
#           Main Code
# ----------------------------------------------

# Title
calculator_title_frame = ttk.Frame(root)
calculator_title_frame.pack(pady = 10)

calculator = ttk.Label(calculator_title_frame, text = 'Calculator')
calculator.config(font = ('Times New Roman', 20), background = 'light blue')
calculator.pack()

# Arithmetic buttons
arithmetic_frame = ttk.Frame(root)
arithmetic_frame.pack(pady = 10)

add_button = ttk.Checkbutton(arithmetic_frame, text = 'Addition', variable = add, command = lambda: only_one_selected(add))
add_button.grid(column = 0, row = 0)

sub_button = ttk.Checkbutton(arithmetic_frame, text = 'Subtraction', variable = sub, command = lambda: only_one_selected(sub))
sub_button.grid(column = 1, row = 0)

mul_button = ttk.Checkbutton(arithmetic_frame, text = 'Multiplication', variable = mul, command = lambda: only_one_selected(mul))
mul_button.grid(column = 2, row = 0)

div_button = ttk.Checkbutton(arithmetic_frame, text = 'Division', variable = div, command = lambda: only_one_selected(div))
div_button.grid(column = 3, row = 0)

# Number Entry 
numberone_entry_label_frame = ttk.Frame(root)
numberone_entry_label_frame.pack(pady = 10)

num1_label = ttk.Label(numberone_entry_label_frame, text= 'Number 1', padding=(10,0))
num1_label.pack(side = 'left')
num1_entry = tk.Entry(numberone_entry_label_frame, textvariable= num1)
num1_entry.pack(side = 'left')

numbertwo_entry_label_frame = ttk.Frame(root)
numbertwo_entry_label_frame.pack(pady = 1)

num2_label = ttk.Label(numbertwo_entry_label_frame, text = 'Number 2', padding = (10,0))
num2_label.pack(side = 'left')
num2_entry = tk.Entry(numbertwo_entry_label_frame, textvariable = num2)
num2_entry.pack(side = 'left')

# Submit button
equal_frame = ttk.Frame(root)
equal_frame.pack(pady = 10)

submit_button = ttk.Button(equal_frame, text= 'Press to Calculate', command = calculation)
submit_button.pack(side = 'left')

results = ttk.Label(equal_frame, text= 'Results: 0', padding=(10,0))
results.pack(side = 'right')

# Clear screen
clear_screen_frame = ttk.Frame(root)
clear_screen_frame.pack(pady = 10)
clear_screen_label  = ttk.Label(clear_screen_frame, text = 'Clear Screen:', padding = (10,0))
clear_screen_label.pack(side = 'left')
clear_screen_button = ttk.Button(clear_screen_frame, text = 'Press to Reset', command = clear_screen)
clear_screen_button.pack(side = 'right')

# Exit button
exit_button_frame = ttk.Frame(root)
exit_button_frame.pack(pady = 10)
exit_button = ttk.Button(exit_button_frame, text = 'Exit', command = root.destroy)
exit_button.pack(side = 'bottom')

# Tkinter mainloop
root.mainloop()
