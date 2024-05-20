#Step 1 
from random import random, shuffle

word_list: list[str] = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

shuffle(word_list)
chosen_word:str = word_list[1]

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess: str = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


if guess in chosen_word:
    print (f"The letter {guess} is in the chosen word which was {chosen_word}.")
else:
    print (f"The letter {guess} is not in the chosen word which was {chosen_word}.")