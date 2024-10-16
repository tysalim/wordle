import time
import random
import os

RECORD = 0

# takes user input, repeats through each round calling the checker function
def main():
    while True:
        print("Welcome to the Wordle game!")
        time.sleep(1)
        opt = input("Please enter one of the following commands to start: \n1. Wordle Classic\n2. Wordle (Less Guesses)\n3. Quit\n> ").strip()
        print("Your option has been noted. Loading...")
        word = select_word()
        time.sleep(1)
        os.system("clear")
        if opt == "1":
            wordle(word, 6)
        elif opt == "2":
            wordle(word, 3)
        elif opt == "3":
            print("Thanks for playing! Play again soon!")
            break
        else:
            print("Invalid input...")
            continue
        continuation = input("Would you like to continue? Press ENTER for yes, and any other key to quit. ")
        if continuation != "":
            print("Thanks for playing! Play again soon!")
            exit(1)


# Function to select a word from the valid Wordle word list
def select_word():
    with open("wordlist.txt", "r") as word_file:
        lines = word_file.read().splitlines()
        random_word = random.choice(lines)
        return random_word

# Function to run main game
def wordle(true_word, rounds):
    FEEDBACK_STACK = []
    length = len(true_word)

    # Iterates per round 
    for i in range(rounds):
        feedback_arr = ["\U000026AB" for _ in range(length)]
        temp = true_word
        print(f"\nRound {i + 1}")
        input_word = ""

        # Checks input to make sure it has valid length
        while len(input_word) != length:
            input_word = input("Your Guess > ").strip()
        
        # First Iteration: Check for matching words
        for j in range(length):
            if input_word[j] == temp[j]:
                feedback_arr[j] = ("\U0001F7E2") # green-circle
                temp = temp.replace(input_word[j], "-", 1)
        
        # Second Iteration: Check for wrongly-positioned/absent words (prevents duplicates)
        for k in range(length):
            if input_word[k] in temp and feedback_arr[k] == "\U000026AB":
                feedback_arr[k] = ("\U0001F7E1") # yellow-circle
                temp = temp.replace(input_word[k], "-", 1)
        
        # Generates stack which will be printed to user
        FEEDBACK_STACK.append("".join(feedback_arr))
        for lines in FEEDBACK_STACK:
            print(lines)
        
        # Checks if the input is correct
        is_correct = check_output(feedback_arr)
        if is_correct == True:
            print(f"You got it after {i + 1} tries!\n")
            return
        else:
            print("Try again!")
            time.sleep(0.5)
    print(f"You ran out of rounds! The correct answer was {true_word}! Try again next time!")
    
# Checks feedback-array if the word had been guessed or not
def check_output(feedback_arr):
    for i in range(len(feedback_arr)):
        if feedback_arr[i] in ["\U000026AB", "\U0001F7E1"]:
            return False
    return True


if __name__ == "__main__":
    main()