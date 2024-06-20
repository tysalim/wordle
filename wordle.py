import time
import random
import os

MAX_ROUNDS = 6
PERSONAL_RECORD = 0

# takes user input, repeats through each round calling the checker function
def main():
    while True:
        print("Welcome to the Wordle game!")
        time.sleep(1)
        opt = input("Please enter one of the following commands to start: \n1. Wordle Classic\n2. Wordle (Less Guesses)\n3. Quit\n> ")
        print("Your option has been noted. Loading...")
        time.sleep(1)
        if opt == "1":
            wordle(6)
        elif opt == "2":
            wordle(3)
        elif opt == "3":
            print("Thanks for playing! Play again soon!")
            break
        else:
            print("Invalid input...")
            continue
        continuation = input("Would you like to continue? Press ENTER for yes, and any other key to quit.")
        if continuation == "\n":
            continue
        else:
            exit(1)



def select_word():
    with open("wordlist.txt", "r") as word_file:
        lines = word_file.read().splitlines()
        random_word = random.choice(lines)
        return random_word
    
# TODO: Fix issues with duplicate letters

def check_input(true_word, input_word, FEEDBACK_STACK):
    feedback_arr = []
    temp = [x for x in true_word]
    for i in range(len(input_word)):
        if input_word[i] == true_word[i]:
            feedback_arr.append("\U0001F7E2") # green-circle
            continue
        elif input_word[i] in temp:
            feedback_arr.append("\U0001F7E1") # yellow-circle
        else:            
            feedback_arr.append("\U000026AB") # black-circle
    FEEDBACK_STACK.append("".join(feedback_arr))
    for lines in FEEDBACK_STACK:
        print(lines)
    if "\U0001F534" not in feedback_arr and "\U000026AB" not in feedback_arr:
        return True
    else:
        return False
    

        

def wordle(rounds):
    word = select_word()
    os.system("clear")
    record = PERSONAL_RECORD
    FEEDBACK_STACK = []
    for round in range(1, rounds + 1):
        print(f"Round {round}")
        input_word = input("Your guess > ")
        time.sleep(0.5)
        is_solved = check_input(word, input_word, FEEDBACK_STACK)
        time.sleep(0.5)
        if is_solved == True:
            print(f"You solved it! It took you just {round} rounds.")
            if record == 0 or round < record:
                record = round
            print(f"Personal Best: {record}")
            return
        else:
            print("Try again!")
    print(f"You didn't solve the word in time! The word was {word}! Better luck next time!")
    
        



if __name__ == "__main__":
    main()