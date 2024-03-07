import tkinter as tk

def change_bg_color_red():
    root.configure(bg='red')

def change_bg_color_blue():
    root.configure(bg='blue')

root = tk.Tk()

red_button = tk.Button(root, text="Change to Red", command=change_bg_color_red)
red_button.pack()

blue_button = tk.Button(root, text="Change to Blue", command=change_bg_color_blue)
blue_button.pack()

root.mainloop()

