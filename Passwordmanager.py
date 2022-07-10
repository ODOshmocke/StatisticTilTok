import random
import string
import tkinter.messagebox
import sys
import os
import tkinter as tk
import pyperclip
from tkinter import *
import smtplib, ssl








password = 0
window = tk.Tk()
window.geometry('400x170')

def random_password():
    characters = string.ascii_letters + string.digits
    global password
    password = ''.join(random.choice(characters) for i in range(14))

def copy_password():
    pyperclip.copy(password)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def write_password_to_txt():
    text = safe_entry.get()
    with open('Passwords.txt' , 'a') as f:
        f.write(text + ':' + password)
        f.write('\n')
        f.close()

def get_all_passwords():
    with open('Passwords.txt') as f:
        global password_Text
        password_Text = f.read()
        f.close()

def main_window():
    def all_passwords_text():
        global password_Text
        All_passwords_label.config(text=password_Text)
    All_passwords_label = tkinter.Label(
        window,
        text=password_Text,
        foreground="black",
        background="white",
        width=25,)
    password_label = tkinter.Label(
        text=password,
        foreground="white",
        background="black",
        width=20,)
    new_password_button = tk.Button(
        text='New password?',
        width = 20,
        bg="blue",
        fg="yellow",
        command=restart_program)
    copy_button = tk.Button(
        text='Copy password?',
        width=20,
        bg="white",
        fg="black",
        command=copy_password)
    global safe_entry
    safe_entry = tk.Entry(
        width=20,
        bg="gray",
        fg='black',
        readonlybackground='black',

    )
    save_button = tk.Button(
        text='save',
        width=10,
        cursor='hand1',
        bg='light gray',
        command=lambda:[write_password_to_txt(), All_passwords_label, window.update()]
    )
    refresh_button = tk.Button(
        text='Refresh',
        width=20,
        bg="white",
        fg="black",
        command=all_passwords_text
    )

    All_passwords_label.pack(side='right')
    password_label.pack()
    new_password_button.pack()
    copy_button.pack()
    safe_entry.pack()
    save_button.pack()
    refresh_button.pack()


get_all_passwords()
random_password()
main_window()
window.mainloop()