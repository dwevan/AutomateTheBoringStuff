# Random number game

import random
secretNumber = random.randint(0, 20)
print('I am thinking of a number between 1 and 20, you have 6 attempts')

# Player guesses modules
for guessesTaken in range(1, 7):
    print('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('guess is too low')
    elif guess > secretNumber:
        print('guess is too high')
    else:
        break  # They got it right!

if guess == secretNumber:
    print('well done, you got it in ' + str(guessesTaken) + ' guesses!')
else:
    print('Sorry I was thinking of ' + str(secretNumber))
