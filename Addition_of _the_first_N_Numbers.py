# The addition of the first n numbers

n = int(input('Introduce a number: '))
suma = 0
for i in range(1, n+1):
    suma = suma + i
print(f'The addition of the first {n} numbers is: ',suma)