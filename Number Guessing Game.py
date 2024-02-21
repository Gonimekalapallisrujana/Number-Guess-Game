from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0


#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")


#Make function to set difficulty.
def set_difficulty():
  levels = input("Choose a difficulty. Type 'easy' or 'hard': ")
  level = levels.lower()
  if level == "easy":
    global turnshard
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("Think of a number between 1 and 100.")
  answer = randint(1, 100)
  

  turns = set_difficulty()

  guess = 0
  while guess != answer:
    print(f"you have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


#Track the number of turns and reduce by 1 if they get it wrong.
game()
#repeat the guessing functionality if they get it wrong.
