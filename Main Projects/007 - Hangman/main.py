#Step 5
from replit import clear
import random
import hangman_art
import hangman_words

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
hangman_logo = hangman_art.logo
print(hangman_logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    if guess not in display:
      for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
          display[position] = letter
    else:
      print(f"You have already guessed '{guess}'\n\n")
    #Check if user is wrong.
    if guess not in chosen_word:
      lives -= 1
      print(f"The letter '{guess}', is not in the word. You lose a life!\n\nLives remaning: {lives}\n\n")
      #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
      if lives == 0:
        end_of_game = True
        print(f"\n\nYou lose!!!!!\n\n\n\nThe word you could not guess was '{chosen_word}'\n\n")
      elif lives == 2:
        hint = ""
        for n in range(3):
          hint += chosen_word[n]
        print(f"Since you are down to 2 lives sucker, here is a free hint for you:\n\nThe first three letters of the word are: {hint}\n\n")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.\n\n")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    stage_art = hangman_art.stages
    print(stage_art[lives])