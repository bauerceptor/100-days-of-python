import random
from replit import clear
import art
from game_data import data


def generate_choice(data, choice1):
    choice2 = random.choice(data)
    while choice1["name"] == choice2["name"]:
        choice2 = random.choice(data)
    return choice2


def print_game_info(choice1, choice2):
    print(f"Compare A. {choice1['name']}, a {choice1['description']}, from {choice1['country']}.")
    print(art.vs)
    print(f"Against B. {choice2['name']}, a {choice2['description']}, from {choice2['country']}.")


def if_correct(data, option1, option2, score):
    clear()
    option1 = option2
    option2 = generate_choice(data, option1)
    score += 1
    return option1, option2, score


def if_false(score):
    clear()
    print(f"Sorry, that's not correct. Your final score: {score}.")
    return False


should_continue = True
score = 0
option1 = random.choice(data)
option2 = generate_choice(data, option1)

while should_continue:
    print(art.logo)
    
    if score > 0:
        print(f"You're right! Current score: {score}.")

    print_game_info(option1, option2)

    # print(f"Psst.. A has {option1['follower_count']} followers and B has {option2['follower_count']} followers.")            # for debugging!!
    
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_answer == 'a':
        if option1['follower_count'] >= option2['follower_count']:
            option1, option2, score = if_correct(data, option1, option2, score)
        else:
            should_continue = if_false(score)
    elif user_answer == 'b':
        if option2['follower_count'] >= option1['follower_count']:
            option1, option2, score = if_correct(data, option1, option2, score)
        else:
            should_continue = if_false(score)