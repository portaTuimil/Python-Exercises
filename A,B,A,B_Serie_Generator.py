# Serie A B A B A B
# w = interruptor

n = int(input('Introduce the number of repetitions that you want:'))
w = 0
for i in range(1,2*n+1):
    if w==0:
        print('A', end=', ')
        w = w + 1
    else:
        print('B', end=', ')
        w = w - 1