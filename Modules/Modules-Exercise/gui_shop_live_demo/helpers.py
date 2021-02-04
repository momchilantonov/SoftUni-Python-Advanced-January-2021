from gui_shop_live_demo.canvas import tk


def clean_screen():
    for el in tk.grid_slaves():
        el.destroy()