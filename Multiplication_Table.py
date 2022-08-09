# Multiplication Table

n = int(input('Introduce the number you want to multiplicate: '))
p = int(input('Introduce the number of multiplications you want: '))
for i in range(1,p+1):
    print(n,'x',i, '=',n*i)