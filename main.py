from tkinter import *
from card import Cards
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
PAD_Y = 50
PAD_X = 50


# --------UI Setup-----------------#


# SETUP PARENT WINDOW
root = Tk()
root.title("Fast French")
root.columnconfigure(3, weight=1)
root.rowconfigure(3, weight=1)
root.config(padx=PAD_X, pady=PAD_Y, bg=BACKGROUND_COLOR)

# MAIN CARD CLASS
cards = Cards()

# BUTTONS
wrong_img = PhotoImage(height=100, width=99, file="./images/wrong.png")
wrong_button = Button(root, image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=cards.next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(height=100, width=100, file="./images/right.png")
right_button = Button(root, image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=cards.remove_word)
right_button.grid(row=1, column=1)

# MAIN LOOP


cards.show_questions()
root.mainloop()
