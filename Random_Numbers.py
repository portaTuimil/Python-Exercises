#Calculate random numbers between two numbers

n = int(input("Introduce the amount of numbers that you want: "))
f = int(input("They will be between: "))
l = int(input("And: "))

import random
def random_vector(n):
    vector = [0]*n
    for i in range(n):
        vector[i] = random.randint(f, l)
    return vector

results = random_vector(n)
print(results)