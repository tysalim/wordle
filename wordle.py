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



def select_word():
    with open("wordlist.txt", "r") as word_file:
        lines = word_file.read().splitlines()
        random_word = random.choice(lines)
        return random_word

def wordle(true_word, rounds):
    FEEDBACK_STACK = []
    length = len(true_word)

    for i in range(rounds):
        feedback_arr = ["\U000026AB" for _ in range(length)]
        temp = true_word
        print(f"\nRound {i + 1}")
        input_word = ""
        while len(input_word) != length:
            input_word = input("Your Guess > ").strip()
        
        for j in range(length):
            if input_word[j] == temp[j]:
                feedback_arr[j] = ("\U0001F7E2") # green-circle
                temp = temp.replace(input_word[j], "-", 1)
        
        for k in range(length):
            if input_word[k] in temp and feedback_arr[k] == "\U000026AB":
                feedback_arr[k] = ("\U0001F7E1") # yellow-circle
                temp = temp.replace(input_word[k], "-", 1)
        
        FEEDBACK_STACK.append("".join(feedback_arr))
        for lines in FEEDBACK_STACK:
            print(lines)
        is_correct = check_output(feedback_arr)
        if is_correct == True:
            print(f"You got it after {i + 1} tries!\n")
            return
        else:
            print("Try again!")
            time.sleep(0.5)
    print(f"The correct answer was {true_word}!")
    

def check_output(feedback_arr):
    for i in range(len(feedback_arr)):
        if feedback_arr[i] == "\U0001F7E1" or feedback_arr[i] == "\U000026AB":
            return False
    return True


if __name__ == "__main__":
    main()