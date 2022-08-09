# Factorial

n = int(input('Introduce a number: '))
factorial = 1

for i in range (1, n+1):
    factorial = factorial * i
print(f'The facatorial of {n} is:', factorial)