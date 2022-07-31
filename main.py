#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

pw_letter = []
pw_symbols = []
pw_numbers = []

for character in range (0,nr_letters):
    x = random.randint(0,51)
    pw_letter.append(letters[x])

for character in range (0,nr_symbols):
    x = random.randint(0,8)
    pw_symbols.append(symbols[x])
  
for character in range (0,nr_numbers):
    x = random.randint(0,9)
    pw_numbers.append(numbers[x])

password_comb = pw_letter + pw_symbols + pw_numbers

comb_list = []

for sublist in password_comb:
  for character in sublist:
    comb_list.append(character)

password_final = random.sample(comb_list,len(comb_list))

password_str = ''.join(password_final)

print(password_str)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P