# [PACKAGES]
from tkinter import *
from textblob import TextBlob 
import pandas as pd
import re


# [BUTTON-Check]
# This function checks the word input and performs spelling correction
def checkSpelling() -> str | None:
    try:
        # [INPUT] Getting the word user entered
        input_text: str = text.get().strip()
        input_text_includes_character = (re.compile('[@_!#$%^&*()<>?/|}{~:]').search(input_text) is not None)
        input_text_is_numerical = input_text.isdigit() or isinstance(input_text, int) or isinstance(input_text, float)
        input_text_more_than_one_word = len(input_text.split(" ")) >= 2

        """ Implemented error handling to gracefully manage potential issues."""
        # [ERROR]
        # This error msg will be displayed if the user clicks the "Click Me" button without entering any text.
        if len(input_text) == 0:
            raise ValueError("Please enter a word before clicking.")

        # [ERROR]
        # Check if the user's input is numerical
        if input_text_is_numerical:
            raise ValueError("Invalid input. Please enter a word.")

        # [ERROR]
        # User inputs more than one word
        if input_text_more_than_one_word:
            raise Exception("This program only checks a single word")

        if input_text_includes_character:
            raise Exception("The word shouldn't include special characters")

        # Textblob
        blob_text: TextBlob = TextBlob(input_text)  # Getting the object for the word

        # Corrected word
        corrected_word: str = str(blob_text.correct())

        # [SUCCESS]
        # The user input and the suggested correct word is equal
        if input_text.lower() is corrected_word.lower():
            correctedText.set("The spelling is correct.")
            # [RETURN]
            return corrected_word

        # [SUCCESS]
        # The blob package successfully generated the correct word
        else:
            correctedText.set("The corrected word is: " + corrected_word)  # Showing the corrected word
            # [RETURN]
            return corrected_word

    except Exception as e:
        correctedText.set("Error: " + str(e))


# [BUTTON-Clear]
# This function clears the input box and the label
def clearTextbox() -> None:
    try:
        input_text: str = text.get()
        if len(input_text) == 0:
            # [ERROR]
            # This message will be displayed if the user try to clear the textbox and no input word
            raise ValueError(
                "Textbox is Empty!")
        else:
            # Clear the content of the Entry widget
            text.set("")
            # Clear the correctedText label as well
            correctedText.set("")

    except ValueError as ve:
        correctedText.set("Error: " + str(ve))


# [BUTTON-Copy to Clipboard]
# Helper/callback function to store the corrected word in the clipboard
def clipboardCallback() -> None:
    data_frame = pd.DataFrame([checkSpelling().strip()])
    data_frame.to_clipboard(index=False, header=False)


if __name__ == "__main__":

    # Single Style Convention
    component = {
        'primary-bg-color': 'SlateGray1',
        'secondary-bg-color': 'SlateGray4',
        'anchor': 'e',
        'header-font-family': 'Times',
        'header-font-weight': 'bold',
        'header-font-size': 20,
        'body-font-family': 'calibre',
        'body-font-size': 13,
        'body-font-weight': 'normal',
        'position-x': 20,
        'position-y': 10,
        'justify-position': LEFT
    }

    # Creating the window
    tkinterWindow: Tk = Tk()
    tkinterWindow.title("Modified Spell Checker (CS3A-G7)")
    tkinterWindow.geometry('500x250')
    tkinterWindow.config(bg=component['primary-bg-color'])

    # Creating the variables to get the word and set the correct word
    text: StringVar = StringVar(tkinterWindow)
    correctedText: StringVar = StringVar(tkinterWindow)

    # ==== LABELS ====
    # The main label
    (Label(tkinterWindow,
           text='Modified Spell Checker',
           bg=component['primary-bg-color'],
           fg='Blue',
           font=(component['header-font-family'], component['header-font-size'], component['header-font-weight']))
     .place(x=component['position-x'], y=component['position-y']))

    # [LABEL]
    # Getting the input of word from the user
    (Label(tkinterWindow,
           text='Please enter the word:',
           bg=component['primary-bg-color'],
           font=(component['body-font-family'], component['body-font-size'], component['body-font-weight']),
           anchor=component['anchor'],
           justify=component['justify-position'])
     .place(x=component['position-x'], y=component['position-y'] + 60))

    Entry(tkinterWindow, textvariable=text, width=35, font=('calibre', 13, 'normal')).place(x=20, y=110)

    # [LABEL]
    # Label to show the correct word
    (Label(tkinterWindow,
           textvariable=correctedText,
           bg=component['primary-bg-color'],
           anchor="e",
           font=(component['body-font-family'], component['body-font-size'], component['body-font-weight']),
           justify=component['justify-position'])
     .place(x=component['position-x'], y=component['position-y'] + 130))

    # [BUTTON]
    # Button to do the spell check
    (Button(tkinterWindow,
            text="Check",
            bg=component['secondary-bg-color'],
            font=(component['body-font-family'], component['body-font-size'], component['body-font-weight']),
            command=checkSpelling)
     .place(x=component['position-x'], y=component['position-y'] + 180))

    # [BUTTON]
    # Button to clear the input text
    (Button(tkinterWindow,
            text="Clear",
            bg=component['secondary-bg-color'],
            font=(component['body-font-family'], component['body-font-size'], component['body-font-weight']),
            command=clearTextbox)
     .place(x=component['position-x'] + 80, y=component['position-y'] + 180))

    # [BUTTON]
    # Button to copy the text in the clipboard
    (Button(tkinterWindow,
            text="Copy Clipboard",
            bg=component['secondary-bg-color'],
            font=('calibre', 13),
            command=clipboardCallback)
     .place(x=component['position-x'] + 160, y=component['position-y'] + 180))

    # Runs the window till it is closed by the user
    tkinterWindow.mainloop()
