import random

n = int(input("Introduce the lenght of the password: "))

def passwordGenerator(n):
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers='0123456789'
    symbols='!@#$%*'
    
    password = ''

    for i in range(n):
        l = [random.choice(lower), random.choice(upper), random.choice(numbers), random.choice(symbols)] 
        password = password + random.choice(l)

    return password

print(f'Your randomly generated password is: {passwordGenerator(n)}')