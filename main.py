import random
from ascii import stages
from ascii import logo
from hangmanwords import word_list

display = []
game = False
game2 = False


# print(f'Pssst, the solution is {chosen_word}.')


while not game:
    game = False
    game2 = False
    display = []
    chosen_word = random.choice(word_list)
    lives = 6
    print(logo)
    print(f'Pssst, the solution is {chosen_word}.')
    print(stages[lives])
    for i in chosen_word:
        display.append("_")

    while not game2:


        guess = input("Guess a letter: ").lower()
        if guess in display:
            print(f"You've already guessed {guess}")
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:

                display[position] = guess
                print(display)
        if guess not in chosen_word:
            lives -= 1
            print(f"Sorry. Try again. Your lives left: {lives}")
            print(stages[lives])
        if lives == 0:
            answer = input("You lost. Want to play again? y/n ")
            if answer == "n":
                game = True
                game2 = True
            else:
                game2 = True


        if "_" not in display:
            answer = input("You won! Want to play again? y/n ")
            if answer == "n":
                game = True
                game2 = True
            else:
                game2 = True

