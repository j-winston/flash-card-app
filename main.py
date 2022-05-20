from tkinter import *
from card import Cards
import random
import pandas as pd




BACKGROUND_COLOR = "#B1DDC6"
# TITLE_FONT = ("ariel", 40, "italic")
# FLASH_FONT = ("ariel", 60, "bold")
# WINDOW_HEIGHT = 526
# WINDOW_WIDTH = 800
#
PAD_Y = 50
PAD_X = 50
#
# LANGUAGE = "French"
#
# cards_data = pd.read_csv("./data/french_words.csv")
# cards = pd.DataFrame(cards_data)
#
#
# def choose_card():
#     # choose a random row from dataframe
#     card = cards.sample()
#     card = card.values.tolist()
#
#     return card
#
#
# def display_question():
#     global after_id
#
#     card = choose_card()
#     question = card[0][0]
#
#     canvas.itemconfig(flash_item, text=question, fill="black")
#     canvas.itemconfig(title_item, text="French", fill="black")
#
#     after_id = root.after(3000, display_answer, card)
#
#
# def display_answer(current_card):
#     global after_id
#     # display the answer side of the card
#     answer = current_card[0][1]
#
#     canvas.itemconfig(image_item, image=card_back_img)
#     canvas.itemconfig(title_item, text="English", fill="white")
#     canvas.itemconfig(flash_item, text=answer, fill="white")
#
#     after_id = root.after(3000, display_question)
#
#
# def wrong():
#     # go to the next word if they click the red x
#     root.after_cancel(after_id)
#     display_question()
#
#
#
# def right():
#     # TODO if user clicks here, remove the word from current word list and save to `words_to_learn.csv`
#
#     pass
#

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
#
# right_img = PhotoImage(height=100, width=100, file="./images/right.png")
# right_button = Button(root, image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=)
# right_button.grid(row=1, column=1)
# #
# # SETUP CARD FACE
# canvas = Canvas(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, bg=BACKGROUND_COLOR)
# canvas.grid(row=0, column=0, columnspan=2)
#
# card_face_img = PhotoImage(file="./images/card_front.png")
# card_back_img = PhotoImage(file="./images/card_back.png")
#
# image_item = canvas.create_image(0, 0, image=card_face_img, anchor=NW)
# title_item = canvas.create_text(400, 150, text=LANGUAGE, font=TITLE_FONT)
# flash_item = canvas.create_text(400, 263, text="", font=FLASH_FONT)
# # SETUP CARD
#

# MAIN LOOP


cards.show_cards()

root.mainloop()
