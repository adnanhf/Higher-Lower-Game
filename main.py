from game_data import data
import random as rnd
from os import system

#Created 1st
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

#Created 2nd
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

#Created 4th
def get_random_choice():
  return rnd.choice(data)

#created 5th
def format_data(choice):
  '''
  Format choice into printable format:
  name, description and country
  '''
  name = choice["name"]
  description = choice["description"]
  country = choice["country"]
  
  # This is a line for spoiling answer
  # print(f'{name}: {account["follower_count"]}')
  
  return f"{name}, a {description}, from {country}"

#created 6th
def check_answer(player_guess, a_followers, b_followers):
  '''
  Checks followers against player's guess 
  and returns True if they got it right
  or False if they got it wrong. 
  '''
  if a_followers > b_followers:
    return player_guess == "a"
  else:
    return player_guess == "b"

#Created 3rd
def game():
  print(logo)
  
  score = 0
  game_should_continue = True
  
  #Step 1: Get 2 random choice from game_data.py
  choice_a = get_random_choice()
  choice_b = get_random_choice()

  while game_should_continue:
    '''
    Quick notes:
    Line 47 and 48 are for swapping choice between B and A in
    each round. This preventing a situation where the number
    of followers of choice A keeps going up over the course
    of the game. The reason for doing this is because everything
    in the game_data.py has fewer followers than Instagram.
    '''
    choice_a = choice_b
    choice_b = get_random_choice()

    '''
    To prevent similar choice between A and B,
    we're checking on value equality. If they're
    equal, B would get new choice from game_data.py
    '''
    while choice_a == choice_b:
      choice_b = get_random_choice()

    #Step 2: Show A and B
    print(f"Compare A: {format_data(choice_a)}.")
    print(vs)
    print(f"Against B: {format_data(choice_b)}.")

    #Step 3: Player start guessing
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    #To prevent player type other than 'A' or 'B'
    while guess != 'a' and guess != 'b':
      guess = input("You chose nothing, choose again!\nWho has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = choice_a["follower_count"]
    b_follower_count = choice_b["follower_count"]

    #Step 4: Check player's answer
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #Step 5: Clear the console, whether the answer is right or wrong
    system('cls')

    '''
    If player guess the right answer, the game will show another round.
    If player got the wrong answer, the game will ended. Logo printed
    regardless of player's guess
    '''
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
