import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
password_length = int(input("How long would you like your password to be?\n"))
l_letters = int(input("How many letters would you like in your password?\n"))
s_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, l_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, s_symbols + 1):
    password_list.append(random.choice(numbers))

for char in range(1, n_numbers + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ''.join(password_list)[:password_length]
print(f"Here is your Random Password: {password}")
