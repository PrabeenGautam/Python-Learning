# fruits = ['Mango', 'Apple', 'Pineapple', 'Litchi']

# # for fruit in fruits:
# #   print(fruit)

# for n in range(0, len(fruits)):
#   print(fruits[n])

# for n in range(1, 101):
#   if n % 3 == 0 and n % 5 == 0:
#     print('FizzBuzz')
#   elif n % 3 == 0:
#     print('Fizz')
#   elif n % 5 == 0:
#     print('Buzz')
#   else:
#     print(n)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print('Welcome to PyPassword Generator')
no_letters = int(input('How many letters would you like in your password? \n'))
no_symbols = int(input('How many symbols would you like in your password? \n'))
no_number = int(input('How many numbers would you like in your password? \n'))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ''
# for n in range(0, no_letters):
#   password += letters[random.randint(0, len(letters) - 1)]

# for n in range(0, no_symbols):
#   password += symbols[random.randint(0, len(symbols) - 1)]

# for n in range(0, no_number):
#   password += numbers[random.randint(0, len(numbers) - 1)]

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
password = ''

for char in range(0, no_letters):
  password_list += random.choice(letters)

for char in range(0, no_symbols):
  password_list += random.choice(symbols)

for char in range(0, no_number):
  password_list += random.choice(numbers)
  
for n in range(0, len(password_list)):
  character =  random.choice(password_list)
  password += character
  password_list.remove(character)

print(f'Here is the password: {password}')
