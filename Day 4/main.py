# from random import randint, random, seed
# # Eandomization

# import random
# # print(random.seed(10))

# number = random.randint(0,1)
# if(number == 0):
#   print("Tails")
# else:
#   print("Heads")

# print("Hello World".count('o'))
# fruits = ['Apple', 'Mango']
# print(fruits)

# array = [1, 2, 3, 4, 5, 6, 7, 8]
# new_array = array.remove(5)
# print(array)

# 🚨 Don't change the code below 👇
# import random
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# index = random.randint(0, len(names) - 1)
# print(index)
# name = names[index]
# print(f'{name} is going to buy the meal today!') 

# 🚨 Don't change the code below 👇
# from turtle import pos


# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f'''


# {row1}\n{row2}\n{row3}


# ''')

# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
# #Write your code below this row 👇
# column = int(position[0]) - 1
# row = int(position[1]) - 1;

# selected_row = map[row]
# selected_row[column] = 'x'
# map[row] = selected_row

# #Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f'''


# {row1}\n{row2}\n{row3}


# ''')

import random
from secrets import choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
standard_input = '2'
choices = int(input("What do you choose? 0 for Rock,  1 for Paper or 2 for Scissors"))
map = [rock, paper, scissors]
print(f'''

{map[choices]}

''')

computer_choices = random.randint(0, 2)
print('Computer choices')
print(f'''

{map[computer_choices]}

''')

if (choices == 0 and computer_choices == 2) or  (choices == 1 and computer_choices == 0) or (choices == 2 and computer_choices == 1):
  print("You wins")
elif choices == computer_choices:
  print("Draw")
else:
  print("Computer wins")