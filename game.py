import random
import time

# Create a list of levels with their corresponding range
levels = {
    "easy": (1, 10),
    "medium": (1, 50),
    "hard": (1, 100)
}

# Create a dictionary to store the high scores
high_scores = {
    "easy": None,
    "medium": None,
    "hard": None
}

# Function to play the guessing game
def play_game(level):
    start_time = time.time()
    # Get the range for the selected level
    level_range = levels[level]
    # Generate a random number within the level range
    number = random.randint(level_range[0], level_range[1])
    # Ask the user to guess the number
    guess = int(input("Guess the number between {} and {}: ".format(level_range[0], level_range[1])))
    # Keep track of the number of guesses
    guesses = 1
    # Loop until the user guesses the correct number
    while guess != number and time.time() - start_time <= 1:
        # Give a hint if the guess is too high or too low
        if guess > number:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")
        # Get the next guess from the user
        guess = int(input("Guess the number between {} and {}: ".format(level_range[0], level_range[1])))
        # Add 1 to the number of guesses
        guesses += 1
    if guess != number and time.time() - start_time > 1:
        print("Time out! The number was ", number)
    else:
        # Print a message to the user indicating that they won
        print("Congratulations! You guessed the number in", guesses, "tries.")
        # Check if the user set a new high score
        if high_scores[level] is None or guesses < high_scores[level]:
            high_scores[level] = guesses
            print("You set a new high score!")
        else:
            print("The current high score is", high_scores[level], "tries.")
    print()

# Main menu function
def menu():
    while True:
        # Print the menu options
        print("Welcome to the guessing game!")
        print("1. Play a game")
        print("2. View high scores")
        print("3. Exit")
        # Get the user's selection
        selection = int(input("Enter your selection: "))
        # Handle the user's selection
        if selection == 1:
            # Ask the user to select a level
            print("Select a level:")
            for i, level in enumerate(levels):
                print("{}. {}".format(i+1, level))
            level_selection = int(input("Enter your selection: "))
            level = list(levels.keys())[level_selection-1]
            play_game(level)
