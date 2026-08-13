"""
Temperature Converter

Purpose
-------
To calculate either celsius or fahrenheit when the other temperature 
is inserted.

Author
------
Allan Smart
Blackbit Analytics © 2026

"""
# Basic temperature converter created in Python's Tkinter

# Import Library
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Tkinter main window
root = tk.Tk()
root.title('Temperature Coverter')
root.geometry('350x450')
root.resizable(False, False)

#---------------------------------------------
#           Helper Functions
#---------------------------------------------

# Celsius to fahrenheit conversion
def celsius_to_fahrenheit():

    """
    Converting celsius temperature into degrees fahrenheit

    When a temperature is inserted into the entry box, it uses the 
    celsius to fahrenheit conversion calculation. It enforces strict
    type validation on the temperature.

    Raises
    ------
    TyperError
        If the provided temperature is not an integer through a 
        showerror message box.
    """

    try:
        to_fahrenheit = (c_2_f.get() * (9/5)) + 32
        fahrenheit_result.config(text = f'Conversion: {to_fahrenheit:.2f} degrees fahrenheit')
    except tk.TclError:
        messagebox.showerror('Input Error', 'Please enter valid numbers only')
        c_2_f.set(0) 

# Fahrenheit to celsius conversion
def fahrenheit_to_celsius():

    """
    Converting fahrenheit temperature into degrees celsius

    When a temperature is inserted into the entry box, it uses the 
    fahrenheit to celsius conversion calculation. It enforces strict
    type validation on the temperature.

    Raises
    ------
    TyperError
        If the provided temperature is not an integer through a 
        showerror message box.
    """

    try:
        to_celsius = (f_2_c.get() - 32) * (5/9)
        celsius_result.config(text = f'Conversion: {to_celsius:.2f} degrees')
    except tk.TclError:
        messagebox.showerror('Input Error', 'Please enter valid numbers only')
        f_2_c.set(0)

#---------------------------------------------
#           Logic Function
#---------------------------------------------
def clear_screen():

    """
    Clears the entire screen

    Temperatures entered into the box conversion boxes are set to 0, and 
    the result of the calculation are set back to the default value
    """

    c_2_f.set(0)
    f_2_c.set(0)

    fahrenheit_result.config(text = 'Conversion: 0 degrees fahreneheit')

    celsius_result.config(text = 'Conversion: 0 degrees celsius')

# Temperature variables
c_2_f = tk.IntVar()
f_2_c = tk.IntVar()

title = ttk.Label(root, text = 'Temperature', font = ('Times New Roman', 20))
title.pack(pady = 10)

#---------------------------------------------
#           Main Code
#---------------------------------------------


# Celsius to Fahrenheit Frame


# Celsius to fahrenheit label frame
celsisus_to_fahrenheit_frame = ttk.LabelFrame(root)
celsisus_to_fahrenheit_frame.pack(pady = 10)

# Celsius to fahrenheit title
celsius_to_fahrenheit_title = ttk.Label(celsisus_to_fahrenheit_frame, text = 'Celsius to Fahrenheit')
celsius_to_fahrenheit_title.pack(pady = 10)

# Celsius to fahrenheit entry
celsius_to_fahrenheit_entry = tk.Entry(celsisus_to_fahrenheit_frame, text = 'Celsius', textvariable = c_2_f)
celsius_to_fahrenheit_entry.pack(pady = 2)

# Celsius to fahrenheit button
celsisus_to_fahrenheit_button = ttk.Button(celsisus_to_fahrenheit_frame, text = 'Click', command = celsius_to_fahrenheit)
celsisus_to_fahrenheit_button.pack(pady = 2)

# Celisus to fahrenheit result
fahrenheit_result = ttk.Label(celsisus_to_fahrenheit_frame, text = 'Conversion: 0 degrees fahreneheit')
fahrenheit_result.pack(pady = 2)


#Fahrenheit to celsius Frame


# Fahrenheit to celsius label frame
fahrenheit_to_celsius_frame = ttk.LabelFrame(root)
fahrenheit_to_celsius_frame.pack(pady = 10)

# Fahrenheit to celsius title
fahrenheit_to_celsius_title = ttk.Label(fahrenheit_to_celsius_frame, text = 'Fahrenheit to Celsius')
fahrenheit_to_celsius_title.pack(pady = 10)

# Fahrenheit to celsius entry
fahrenheit_to_celsius_entry = tk.Entry(fahrenheit_to_celsius_frame, text = 'Fahrenheit', textvariable = f_2_c)
fahrenheit_to_celsius_entry.pack(pady = 2)

# Fahrenheit to celsius button
fahrenheit_to_celsius_button = ttk.Button(fahrenheit_to_celsius_frame, text = 'Click', command = fahrenheit_to_celsius)
fahrenheit_to_celsius_button.pack(pady = 2)

# Fahrenheit to celsius result
celsius_result = ttk.Label(fahrenheit_to_celsius_frame, text = 'Conversion: 0 degrees celsius')
celsius_result.pack(pady = 2)

# Clear screen and exit buttons


# Clear screen
clear_screen_button = ttk.Button(root, text = 'Clear Screen', command = clear_screen)
clear_screen_button.pack(pady = 10)

# Exit button
exit_button = ttk.Button(root, text = 'Exit', command = root.destroy)
exit_button.pack(pady = 10)

# Tkinter mainloop
root.mainloop()





