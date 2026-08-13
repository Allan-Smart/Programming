import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from forex_python.converter import CurrencyRates 

# Tkinter main window
root = tk.Tk()
root.title('Currency Converter')
root.resizable(False, False)
root.geometry('350x350')
root.config(background='lawn green')

def currency_conversion_calculation():
    pass

# Currency pairs
currency_1 = tk.IntVar()
currency_2 = tk.IntVar()
currency_exchange_rate = tk.IntVar()

# Currency List box

currency_listbox = tk.Listbox(root, 
                              height=10, 
                              width=15, 
                              bg='grey', 
                              font=('Times New Roman', 12))

# Currencies inserted into listbox
currency_listbox.insert(tk.END, 'USD')
currency_listbox.insert(tk.END, 'EUR')
currency_listbox.insert(tk.END, 'GBP')
currency_listbox.insert(tk.END, 'AUD')
currency_listbox.insert(tk.END, 'NZD')
currency_listbox.insert(tk.END, 'JPY')
currency_listbox.insert(tk.END, 'CAD')

# Place widgets
currency_listbox.pack(pady=20)

# Tkinter main window
root.mainloop()

