__author__ = "Casey Mockbee"

# imports

import os, random
from colorama import Fore
from words import list_of_words, US_KEYBOARD

# Global vairables

lettersDict={}
guess_count=0
is_correct=False
answer=""
guesses=[]
continue_playing=True



def init():
    global lettersDict, guess_count, is_correct, answer, guesses
    lettersDict.clear()
    # Fill Letter dictionary
    for letter in US_KEYBOARD:
        lettersDict[letter] = Fore.WHITE
    # reset guess count & end flag & guesses
    guess_count = 0
    is_correct = False
    answer = random.choice(list_of_words).upper()
    guesses = []


def check_answer(guess: str):
    global answer, lettersDict
    temp = []
    is_correct = True
    for i, c in enumerate(guess):
        if c == answer[i]:
            temp.append(Fore.GREEN + c)
            lettersDict[c] = Fore.GREEN
        elif c in answer:
            temp.append(Fore.YELLOW + c)
            is_correct = False
            if lettersDict[c] != Fore.GREEN:
                lettersDict[c] = Fore.YELLOW
        else:
            temp.append(Fore.RED + c)
            is_correct = False
            lettersDict[c] = Fore.LIGHTBLACK_EX
    return {
        'answer': ''.join(temp),
        'is_correct': is_correct
        }

def printAll(guesses: list):
    title = 'Available letters:'
    letterString = [color + character for character, color in lettersDict.items()]
    print(Fore.CYAN + 'Available letters:')
    print(Fore.CYAN + '-' * len(title))
    print(' '.join(letterString[:10]))
    print(' ' + ' '.join(letterString[10:19]))
    print('  ' + ' '.join(letterString[19:]))
    for guess in guesses:
        print(guess)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    global guess_count, is_correct, answer, letters, guesses, continue_playing
    while continue_playing:
        clear_screen()
        init()
        while guess_count < 6 and not is_correct:
            guess = input(Fore.RESET + 'Your Guess: ').strip().upper()
            # guess = guess.strip().upper()
            while len(guess) != 5:
                guess = input('Your guess must be 5 letters: ').strip().upper()
            clear_screen()
            guess_count += 1
            checked_answer = check_answer(guess)
            guesses.append(checked_answer['answer'])
            printAll(guesses)
            if checked_answer['is_correct']:
                is_correct = True
                print(Fore.RESET + f'You won! It only took you {guess_count} {"try" if guess_count == 1 else "tries"}')
        if not is_correct:
            print(Fore.RED + 'You lose :(')
            print("The answer was: " + answer)
        play_again = input(Fore.RESET + 'Play again? [y/n]').strip().upper()
        if play_again == 'N' or play_again == 'NO':
            continue_playing = False
    exit()

if __name__ == '__main__':
    main()