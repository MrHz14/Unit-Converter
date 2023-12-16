import tkinter as tk
from tkinter import ttk

def on_click_button():
    label1.config(text="Hello " + entry.get())

# membuat jendela
root = tk.Tk()
root.title('My Tkinter Program')

# Membuat widget-themed
label = ttk.Label(root, text="Enter your name : ")
label1= ttk.Label(root,text='', font=('Agency FB', 12, 'bold'))
entry = ttk.Entry(root)
button = ttk.Button(root, text='Click', command=on_click_button)

# Menata tampilan
label.grid(column=0, row=0, padx=10, pady=10, columnspan=2)  # Memindahkan label ke baris yang sama dengan button
entry.grid(column=0, row=1, padx=10, pady=10)  # Menempatkan entry di baris berikutnya
button.grid(column=1, row=1, padx=10, pady=10)  # Menempatkan button di baris berikutnya
label1.grid(column=0, row=2, padx=10, pady=10, columnspan=2, )

# Memulai pemanggilan window
root.mainloop()
