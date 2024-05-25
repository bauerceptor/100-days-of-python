
# ############### Our Blackjack House Rules #####################

# ## The deck is unlimited in size. 
# ## There are no jokers. 
# ## The Jack/Queen/King all count as 10.
# ## The the Ace can count as 11 or 1.
# ## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# ## The cards in the list have equal probability of being drawn.
# ## Cards are not removed from the deck as they are drawn.
# ## The computer is the dealer.
from random import choice, sample
from art import logo
from replit import clear


# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# player_hand = []
# computer_hand = []
# import random
# player_hand = (random.sample(cards, 2))
# computer_hand = (random.sample(cards, 2))
# score = {
#   "player_total": 0,
#   "computer_total": 0,
# }
# print(player_hand)
# print(computer_hand)
# print(score["player_total"])
# print(score["computer_total"])
# for i1, i2 in zip(player_hand, computer_hand):
#   score["player_total"] += i1
#   score["computer_total"] += i2
# print(score["player_total"])
# print(score["computer_total"])


def lose(player, computer, total):
  print(f"\tYour final hand: {player}, final score: " + str(total["player_total"]))
  print(f"\tComputer's final hand: {computer}, final score: " + str(total["computer_total"]))
  print("You lose ☹️")
  
def win(player, computer, total):
  print(f"\tYour final hand: {player}, final score: " + str(total["player_total"]))
  print(f"\tComputer's final hand: {computer}, final score: " + str(total["computer_total"]))
  print("You win 😉")

def draw(player, computer, total):
  print(f"\tYour final hand: {player}, final score: " + str(total["player_total"]))
  print(f"\tComputer's final hand: {computer}, final score: " + str(total["computer_total"]))
  print("It's a draw 🙄")

def bust(player, computer, total):
  print(f"\tYour final hand: {player}, final score: " + str(total["player_total"]))
  print(f"\tComputer's final hand: {computer}, final score: " + str(total["computer_total"]))
  if total["computer_total"] > 21:
    print("The computer went over.\nYou win 😎")
  elif total["player_total"] > 21:
    print("The player went over.\nYou lose 😕")


def reveal(computer, total):
  if total["computer_total"] >= 17 and total["computer_total"] < 21:
    if total["computer_total"] == total["player_total"]:
      return draw(player=player_hand, computer=computer_hand, total=score)
    elif total["computer_total"] == 21:
      return lose(player=player_hand, computer=computer_hand, total=score)
    elif total["computer_total"] > total["player_total"]:
      return lose(player=player_hand, computer=computer_hand, total=score)
    else:
      return win(player=player_hand, computer=computer_hand, total=score)
  elif total["computer_total"] > 21:
    return bust(player=player_hand, computer=computer_hand, total=score)
  elif total["computer_total"] < 17:
    draw_card = choice(cards)
    if draw_card == 11 and total["computer_total"] > 10:
      draw_card = 1
    computer.append(draw_card)
    total["computer_total"] += draw_card
    reveal(computer=computer_hand, total=score)

def hit(player, computer, total):
  draw_card = choice(cards)
  if draw_card == 11 and total["player_total"] > 10:
    draw_card = 1
  player.append(draw_card)
  total["player_total"] += draw_card
  if total["player_total"] < 21:
    print(f"\tYour cards: {player}, current score: " + str(total["player_total"]))
    print(f"\tComputer's first card: {computer[0]}")
  if total["player_total"] == 21:
    reveal(computer=computer_hand, total=score)
  elif total["player_total"] > 21:
    return bust(player=player_hand, computer=computer_hand, total=score)
  else:
    if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
      hit(player=player_hand,computer=computer_hand, total=score)
    else:
      reveal(computer=computer_hand, total=score)



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

end_game = False
while not end_game:
  begin_game = input("Do you want to play? Type 'y' or 'n': ")
  clear()
  if begin_game == "y":
    print(logo)
    player_hand = []
    computer_hand = []
    
    score = {
      "player_total": 0,
      "computer_total": 0,
    }
    
    player_hand = (sample(cards, 2))
    computer_hand = (sample(cards, 2))
    
    for i1, i2 in zip(player_hand, computer_hand):
        score["player_total"] += i1
        score["computer_total"] += i2
      
    print(f"\tYour cards: {player_hand}, current score: " + str(score["player_total"]))
    print(f"\tComputer's first card: {computer_hand[0]}")
    
    if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
      hit(player=player_hand,computer=computer_hand, total=score)
    else:
      reveal(computer=computer_hand, total=score)
  else:
    end_game = True

    

    

# # blackjack(player=player_hand, computer=computer_hand, total=score)


















































# ##################### Hints #####################

# #Hint 1: Go to this website and try out the Blackjack game: 
# #   https://games.washingtonpost.com/games/blackjack/
# #Then try out the completed Blackjack project here: 
# #   http://blackjack-final.appbrewery.repl.run

# #Hint 2: Read this breakdown of program requirements: 
# #   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# #Then try to create your own flowchart for the program.

# #Hint 3: Download and read this flow chart I've created: 
# #   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# #Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# #11 is the Ace.
# #cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# #user_cards = []
# #computer_cards = []

# #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
# #and returns the score. 
# #Look up the sum() function to help you do this.

# #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

