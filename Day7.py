from words import *
import random as r
# Day 7 Project: Hangman

guessed_letters = []
board = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Exercise 7.1: checking if letter is in the word

# Step 1
print(logo)
# word_list = ["aardvark", "baboon", "camel"]

# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# word = r.choice(word_list)

# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter:\t").lower()

# # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in word:
#     print(letter == guess)

# Day 7.2 Exercise
# Step 2

# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = r.choice(word_list)

# # Testing code
# # print(f'Pssst, the solution is {chosen_word}.')

# # TODO-1: - Create an empty List called display.
# # For each letter in the chosen_word, add a "_" to 'display'.
# # So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# display = []
# guess = input("Guess a letter: ").lower()
# for letter in chosen_word:
#     display.append("_")
# print(''.join(display))
# # TODO-2: - Loop through each position in the chosen_word;
# # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# index = 0
# for letter in chosen_word:
#     if letter == guess:
#         display[index] = letter
#         print("Right")
#         index += 1
#     else:
#         print("Wrong")
#         index += 1

# # TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# # Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# print(''.join(display))

# # Step 3

# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = r.choice(word_list)
# word_length = len(chosen_word)

# # Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# # Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# # TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# while "_" in display:
#     guess = input("Guess a letter: ").lower()

# # Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         print(
#             f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     print(display)

# This is exercise 7.3
# Step 4

end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
chosen_word = r.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
print(word_length)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    if guess in guessed_letters:
        print(
            f"Looks like you already picked a {guess}, Please try another letter")
    elif guess not in chosen_word:
        lives -= 1
        guessed_letters.append(guess)
        print(f"You guessed the letter {guess} and that is not in the word")
        print(board[lives])
    else:
        guessed_letters.append(guess)

    if lives == 0:
        print("You lost!!!")
        end_of_game = True
