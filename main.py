word = 'Football'
game_life = 8
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print('')

    guess = input(f'Your game life is {game_life}, Guess letter: ')
    guesses.append(guess.lower())
    if guess.lower() not in word:
        game_life -= 1
        if game_life == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f'Congrats you found the word! The word is {word}.')
else:
    print(f'Game over! Try Again! The word was {word}.')