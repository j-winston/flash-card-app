import tkinter
from tkinter import *
import pandas as pd
import random

CARD_HEIGHT = 526
CARD_WIDTH = 800
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("ariel", 40, "italic")
FLASH_FONT = ("ariel", 60, "bold")

# So that we can kill our after() loops in any method
global after_id


class Cards(PhotoImage, Canvas):
    def __init__(self):
        super().__init__()
        self.cards = self.load_cards()

        # Choose last card from deck
        self.card_number = len(self.cards) - 1
        self.current_card = self.cards[self.card_number]

        # Assigned words that user already knows
        self.removed_list = []

        # Load background for front and back of card
        self.question_image = PhotoImage(file="./images/card_front.png")
        self.answer_image = PhotoImage(file="./images/card_back.png")

        # Draw and position main card canvas
        self.canvas = Canvas(height=CARD_HEIGHT, width=CARD_WIDTH, bg=BACKGROUND_COLOR)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.image_item = self.canvas.create_image(0, 0, image=self.question_image, anchor=tkinter.NW)

        # Draw the first words and the langauge title to screen
        self.title_item = self.canvas.create_text(400, 150, text="French", font=TITLE_FONT)
        self.flash_item = self.canvas.create_text(400, 263, text=self.cards[0][0], font=FLASH_FONT)

    def show_questions(self):

        global after_id
        print("before update", self.current_card)
        self.update_deck()
        print("after update", self.current_card)
        # Show the front of the card
        self.canvas.itemconfig(self.flash_item, text=self.current_card[0], fill="black")
        self.canvas.itemconfig(self.image_item, image=self.question_image)
        self.canvas.itemconfig(self.title_item, text="French")

        # Show the answer after 3 seconds
        after_id = self.canvas.after(3000, self.show_answer)

    def show_answer(self):

        global after_id
        # Show the back of the card
        self.canvas.itemconfig(self.image_item, image=self.answer_image)
        self.canvas.itemconfig(self.flash_item, text=self.current_card[1])
        self.canvas.itemconfig(self.title_item, text="English")

        # Show the next question
        after_id = self.canvas.after(3000, self.show_questions)

    def next_card(self):
        # kill the current loop show the next question
        global after_id
        self.canvas.after_cancel(after_id)
        self.show_questions()

    def remove_word(self):
        # Get current card and remove it from the list
        current_card_index = self.cards.index(self.current_card)
        # Add removed word to list
        self.removed_list.append(self.cards.pop(current_card_index))
        # Write removed words to csv file
        self.write_to_file()
        # Ensure we don't get any index errors
        self.update_deck()
        # Call this to avoid index errors if user presses button multiple times
        self.next_card()

    def update_deck(self):
        self.card_number -= 1

        # Update the current card
        if self.card_number >= 0:
            self.current_card = self.cards[self.card_number]
        # Once the last card is indexed reset the deck and show them all again
        else:
            self.card_number = len(self.cards) - 1
            self.current_card = self.cards[self.card_number]

    def write_to_file(self):
        words_to_learn = pd.DataFrame(self.cards, columns=['French', 'English'])
        words_to_learn.to_csv("./data/words_to_learn.csv", index=False)

    def load_cards(self):
        try:
            with open("./data/words_to_learn.csv", "r") as f:
                pass

        except FileNotFoundError:
            cards_data = pd.read_csv("./data/french_words.csv")
            cards_df = pd.DataFrame(cards_data)
            # Convert df to list
            cards = cards_df.values.tolist()
        else:
            cards_data = pd.read_csv("./data/words_to_learn.csv")
            cards_df = pd.DataFrame(cards_data)
            # Convert df to list
            cards = cards_df.values.tolist()

        finally:
            random.shuffle(cards)

        # Return a list of lists ie; [['oui', 'yes']]
        return cards