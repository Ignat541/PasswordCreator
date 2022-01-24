import random

choice_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h',
               'i', 'I', 'g', 'G', 'k', 'K', 'l', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't',
               'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', 'H']
password_length = int(input('Put your password length: '))
def password(x):
    return random.sample(choice_list, k=x)


tuple_password = password(password_length)
for num in tuple_password:
    print(num, end='')
