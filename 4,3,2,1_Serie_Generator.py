# Serie 4,3,2,1,4,3,2,1,

n = int(input('Introduce the number of repetitions that you want:'))
c = 0
w = 4
while c < 4*n:
    print(w, end=', ')
    if w > 1:
        w = w - 1
    else:
        w = 4
    c = c + 1
