import math
from typing import final

# print(math.ceil(4.6))
# print(math.gcd(10, 25, 60))
# def prime_number(number):
#   for n in range(2, number + 1):
#     if n == number :
#       print(f'{number} is a prime number')
#     elif number % n == 0:
#       print(f'{number} is not a prime number')
#       break;
    
# prime_number(11)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
# # if(direction != 'encode' or direction != 'decode'):
    
# #     exit()

# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(text_message, shift_number):
#   finalmessage = ''
#   for letter in text_message:
#     index = alphabet.index(letter)  
#     finalmessage += alphabet[(index + shift_number + len(alphabet)) % len(alphabet)]
#   return finalmessage

# def decrypt(text_message, shift_number):
#   finalmessage = ''
#   for letter in text_message:
#     index = alphabet.index(letter)  
#     finalmessage += alphabet[(index - shift_number + len(alphabet)) % len(alphabet)]
#   return finalmessage


# if direction == 'encode':
#   print(encrypt(text, shift))
# elif direction == 'decode':
#   print(decrypt(text, shift))
# else:
#   print('Wrong direction')

