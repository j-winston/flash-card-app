import tkinter
from tkinter import *
import pandas as pd
import random

CARD_HEIGHT = 526
CARD_WIDTH = 800
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("ariel", 40, "italic")
FLASH_FONT = ("ariel", 60, "bold")


class Cards(PhotoImage, Canvas):
    def __init__(self):
        super().__init__()
        # Read in CSV and create dataframe
        self.cards_data = pd.read_csv("./data/french_words.csv")
        self.cards_df = pd.DataFrame(self.cards_data)

        # Convert df to list
        self.cards = self.cards_df.values.tolist()

        # Shuffle deck
        random.shuffle(self.cards)

        # Choose last card from deck
        self.card_number = len(self.cards) - 1
        self.current_card = self.cards[self.card_number]

        # Load background images
        self.question_image = PhotoImage(file="./images/card_front.png")
        self.answer_image = PhotoImage(file="./images/card_back.png")

        # Draw and position card image canvas
        self.canvas = Canvas(height=CARD_HEIGHT, width=CARD_WIDTH, bg=BACKGROUND_COLOR)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.image_item = self.canvas.create_image(0, 0, image=self.question_image, anchor=tkinter.NW)

        # Initialize flash card text
        self.title_item = self.canvas.create_text(400, 150, text="French", font=TITLE_FONT)
        self.flash_item = self.canvas.create_text(400, 263, text=self.cards[0][0], font=FLASH_FONT)

    def flip_card(self, direction):
        if direction == "back":
            self.canvas.itemconfig(self.image_item, image=self.answer_image)

    def show_cards(self, end_loop=False):
        # Pick the next card from deck
        if self.card_number > 0:
            self.card_number -= 1
            self.current_card = self.cards[self.card_number]

            # Update flash text
            self.canvas.itemconfig(self.flash_item, text=self.current_card[0], fill="black")
            after_id = self.after(3000, self.show_cards, False)
            # Execute this code if user clicks the red 'x' button to kill the loop
            if end_loop:
                self.after_cancel(after_id)

    def next_card(self):
        self.show_cards(end_loop=True)

