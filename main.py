import random

with open('words.txt', 'r') as f:
    lines = f.readlines()
random.shuffle(lines)

game_life = 8
guesses = []

for line in lines:
    question, answer = line.strip().split(':')
    print("Guess the answer to the following question:")
    print(question)

    word = answer.lower()
    display_word = ['_' if letter.isalpha() else letter for letter in word]

    done = False
    while not done:
        # Display the current state of the word
        print(' '.join(display_word))

        # Get user input
        guess = input(f'Your game life is {game_life}, Guess a letter: ').lower()

        # Check if the input is a single alphabetical character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        # Check if the guess has already been made
        if guess in guesses:
            print("You've already guessed that letter. Try another one.")
            continue

        # Add the guess to the list of guesses
        guesses.append(guess)

        # Check if the guess is in the word
        if guess in word:
            # Update the display word with the correct guesses
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
        else:
            # Decrement game life for incorrect guess
            game_life -= 1
            print("Incorrect guess!")
            print(f"Remaining game life: {game_life}")
            if game_life == 0:
                break

        # Check if the word has been completely guessed
        if '_' not in display_word:
            done = True

    # Check if the game is over
    if done:
        print(f'Congrats you found the word! The word is {word}.')
    else:
        print(f'Game over! Try Again! The word was {word}.')
