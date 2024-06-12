from random import randint
#from art import logo

def check_answer(answer, guess, attempts):
  if attempts != 0 and guess > answer:
    print(f"Too high.\nYou have {attempts} turns left.\nGuess again.")
    guess = int(input("Make a guess: "))
  elif attempts != 0 and guess < answer:
    print(f"Too low.\nYou have {attempts} turns left.\nGuess again.")
    guess = int(input("Make a guess: "))

answer = randint(1, 100)
#print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Select the difficulty level. Type 'hard' or 'easy': ")
if difficulty == "hard":
  attempts = 5
  print(f"You have {attempts} attempts remaining to guess the number.")
else:
  attempts = 10
  print(f"You have {attempts} attempts remaining to guess the number.")

end_game = False
guess = int(input("Make a guess: "))
while not end_game:  
  if attempts == 0:
    print("You could not guess the number. You lose.")
    end_game = True
  elif answer > guess:
    attempts -= 1
    check_answer(answer, guess, attempts)
  elif answer < guess:
    attempts -= 1
    check_answer(answer, guess, attempts)
  else:
    print(f"You got it. The number I was thinking of was {answer}")
    end_game = True
