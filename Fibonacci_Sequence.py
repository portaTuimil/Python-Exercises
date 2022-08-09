# Fibonacci Sequence

n = int(input('Introduce the number of digits that you want:'))
a = 1
b = 1
c = 0
co = 0
if n <= 0:
    print('Error')
elif n== 1:
    print(a)
else:
    while co < n:
        print(a, end=', ')
        c = a + b
        a = b
        b = c
        co = co + 1