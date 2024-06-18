import time
import random


# TODO: create globals

MAX_ROUNDS = 6
FEEDBACK_STACK = []

# takes user input, repeats through each round calling the checker function
def main():
    while True:
        print("Welcome to the Wordle game!")
        opt = input("Please enter one of the following commands to start: \n1. Wordle Classic\n2. Wordle (Less Guesses)\n3. Quit\n> ")
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



def select_word():
    with open("wordlist.txt", "r") as word_file:
        lines = word_file.read().splitlines()
        random_word = random.choice(lines)
        return random_word
    


def check_input(true_word, input_word):
    feedback_arr = []
    is_solved = False
    temp = true_word.split()
    for i in range(len(input_word)):
        if input_word[i] == true_word[i]:
            feedback_arr.append("\U0001F7E2")
            is_solved = True
            continue
        elif input_word[i] in temp:
            feedback_arr.append("\U0001F534")
            is_solved = False
        else:
            feedback_arr.append("\U000026AB")
            is_solved = False
    print("".join(feedback_arr))
    return is_solved
    

        

def wordle(rounds):
    word = select_word()
    for round in range(1, rounds + 1):
        print(f"Round {round}")
        input_word = input("Your guess > ")
        is_solved = check_input(word, input_word)
        if is_solved == True:
            print(f"You solved it! It took you just {round} rounds.")
            break
        else:
            print("Try again!")
        



if __name__ == "__main__":
    main()