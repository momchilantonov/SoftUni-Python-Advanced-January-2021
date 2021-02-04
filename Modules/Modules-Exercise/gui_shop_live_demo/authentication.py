import json

from tkinter import Button, Entry, Label
from gui_shop_live_demo.canvas import tk
from gui_shop_live_demo.helpers import clean_screen
from gui_shop_live_demo.products import render_products


def login(username, password):
    with open("db/user_credentials_db.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            usern, psword = line[:-1].split(", ")
            if usern == username and psword == password:
                with open("db/current_user.txt", "w") as current_user_file:
                    current_user_file.write(username)
                render_products()
                return

        render_login(errors=True)


def register(**user):
    user.update({"products": []})
    user.update({"is_admin": False})

    with open("db/users.txt", "a") as file:
        file.write(json.dumps(user))
        file.write("\n")

    with open("db/user_credentials_db.txt", "a") as file:
        file.write(f"{user.get('user')}, {user.get('password')}")
        file.write("\n")
    render_login()


def render_login(errors=None):
    clean_screen()
    Label(text="Enter your username").grid(row=0, column=0)
    username = Entry(tk)
    username.grid(row=1, column=0)
    password = Entry(tk, show="*")
    Label(text="Enter your password").grid(row=2, column=0)
    password.grid(row=3, column=0)
    Button(tk, text="Enter", bg="green",
           command=lambda: login(username.get(), password.get())).grid(row=5, column=0)
    if errors:
        Label(text="Invalid username or password").grid(row=6, column=0)


def render_register():
    clean_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk, show="*")
    password.grid(row=1, column=0)
    first_name = Entry(tk)
    first_name.grid(row=2, column=0)
    last_name = Entry(tk)
    last_name.grid(row=3, column=0)
    Button(tk, text="Register", bg="green",
           command=lambda: register(
               username=username.get(),
               password=password.get(),
               first_name=first_name.get(),
               last_name=last_name.get())).grid(row=4, column=0)


def render_main_enter_screen():
    Button(tk, text="Login", bg="green", fg="white", command=render_login).grid(row=0, column=0)
    Button(tk, text="Register", bg="yellow", command=render_register).grid(row=0, column=1)