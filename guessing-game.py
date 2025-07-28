#Guessing  Game - Jennie Cruz Ramirez

import  random

def  generate_random_number():
    return random.randint(1, 100)
# ^^^ generates random number between 1-100

#
# Step 3
def get_user_guess():
    #Keeps asking the player to guess a number between 1-100 
    while True:
        user_input = int(input("Please guess a number between 1 through 100:"))
        if  user_input >= 1 and user_input <= 100:
            return user_input
        else:
            print("Invalid input")

# Step 4
def playing_guessing_game():
    #Starts the game and picks a secret number.
    #It keeps track of how many times the player has guessed.
    #And after the player guessed a number it tells the user if their guess is too high or too low.
    #Then it keeps asking the player to guess until they get it right.
    print("Welcome to the Guessing Game!")
    secret_number = generate_random_number()
    guesses = 0

    while True:
        user_guess = get_user_guess()
        guesses += 1

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again")
        else:
            print(f"Your guess is correct! It took you {guesses} guesses!")
            break

#Step 5
def game_loop(): 
    #Keeps playing the game until the player wants to stop playing.
    while True:
        playing_guessing_game()
        play_again = input("Would you like to play again? yes/no: ").lower()
        if play_again == "yes":
            playing_guessing_game()
        if play_again == "no":
            print("Thanks for playing! Goodbye!")
            break #Stops playing if the player says no


#Step 6
#This makes sure the game starts when you run the file.
if __name__ == "__main__": 
    game_loop()

