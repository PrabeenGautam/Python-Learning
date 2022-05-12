import imp
import random
from hangman_words import word_list
from hangman_art import logo, stages

initial = []
initialString = ''
wrongcount = 0;
alreadyguess = []
stage = stages.reverse()
print(logo)
print(stages[wrongcount])

chosen_word = random.choice(word_list).lower()
count = len(chosen_word)

for n in range(len(chosen_word)):
  initial.append('_')


while(count > 0 and wrongcount != 7):
  initialString = ' '.join(initial)
  print(f'''
  {initialString}

  ''')
  # print(f'count: {count} and wrong count: {wrongcount}')
  guess = input("Guess the letter: ")[0].lower()
  if guess in alreadyguess:
    print("Value is guessed already. Try new values:")
  elif (guess in chosen_word):
    print('\nCorrect Guess! ✅\n')
    alreadyguess.append(guess)
    index = []
    for n in range(0, len(chosen_word)):
      if (chosen_word[n] == guess):
        index.append(n)
        count -= 1

    for value in index:
      initial[value] = guess
    already__guess = ', '.join(alreadyguess)
    print(f'Already Guess Character: {already__guess}')
  else:
    print('\nWrong Guess! Try again 👎\n')
    alreadyguess.append(guess)
    if wrongcount != 7:
      wrongcount += 1
      print(stages[wrongcount])
    already__guess = ', '.join(alreadyguess)
    print(f'Already Guess Character: {already__guess}')
if(wrongcount == 7):
   print('Game Over 😢 \n')  
   print(f'Exact Word is: {chosen_word}') 
if(count == 0):
  initialString = ' '.join(initial)
  print(f'''
  {initialString}

  ''') 

  print('Well done!  😍❤')