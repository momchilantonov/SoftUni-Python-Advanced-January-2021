import json
import os

from tkinter import Button, Label

from gui_shop_live_demo.canvas import tk
from gui_shop_live_demo.helpers import clean_screen
from PIL import Image, ImageTk


base_folder = os.path.dirname(__file__)


def buy_product(button):
    _, product_id = button.cget("text").split()
    product_id = int(product_id)
    current_logged_in_user = None
    with open("db/current_user.txt", "r") as file:
        current_logged_in_user = file.read()

    # Render view again for products
    with open("db/users.txt", "r+") as file:
        users = file.readlines()
        file.seek(0)
        for user in users:
            user_as_dict = json.loads(user)
            if user_as_dict.get("username") == current_logged_in_user:
                user_as_dict["products"].append(product_id)
            file.write(json.dumps(user_as_dict))
            file.write("\n")

    with open("db/products.txt", "r+") as file:
        products = file.readlines()
        file.seek(0)
        for product in products:
            product_as_dict = json.loads(product)
            if product_as_dict["id"] == product_id:
                product_as_dict["count"] -= 1
            file.write(json.dumps(product_as_dict))
            file.write("\n")

    render_products()




def render_products():
    clean_screen()
    with open("db/products.txt", "r") as file:
        products = file.readlines()
        column_counter = 0
        for product in products:
            current_product = json.loads(product)
            Label(text=current_product.get('name')).grid(row=0, column=column_counter)

            image = Image.open(os.path.join(os.path.join(base_folder, "images"), current_product.get("img_path")))
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            img_label = Label(image=photo)
            img_label.image = photo
            img_label.grid(row=1, column=column_counter)

            button = Button(tk, text=f"Buy {current_product.get('id')}")
            button.configure(command=lambda b=button: buy_product(b))
            button.grid(row=3, column=column_counter)
            Label(text=current_product.get('count')).grid(row=2, column=column_counter)
            column_counter += 1