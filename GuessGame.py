# This the guess the Random Number Game

import random

PlayerName = input('Hello Player!, What is your Good Name? : ')
print(f'Well, {PlayerName}. I am Thinking of a num between 1 and 20 can u take a Guess?')

SecretNum = random.randint(1,20)

for GuessesTaken in range(1,11):
  print(f'{PlayerName}, Take a Guess')
  Guess = int(input())
  if Guess < SecretNum: print(f'it is too low {PlayerName}')
  elif Guess > SecretNum: print(f'it is too high {PlayerName}')
  else: break     # correct Guess
    
if Guess == SecretNum: print(f'Bravo!, Congo {PlayerName} win you guessed my num in {str(GuessesTaken)} guesses!')
else: print(f'Ooops! Wrong guess. The num I thinking was {str(SecretNum)}')


print(f'{PlayerName}, You took {str(GuessesTaken)} guesses')
