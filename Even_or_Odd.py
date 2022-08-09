# Seperate in even or odd

n = int(input('Introduce the amount of numbers that you want to clasificate:'))
list = []
for i in range(1, n+1):
    p = int(input('Introduce a number:'))
    list.append(p)

def separate_list(list):
    list.sort()
    even = []
    odd = []
    for i in list:
        if i % 2 ==0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

even, odd = separate_list(list)

print('The even numbers are:',even)
print('The odd numbers are:',odd)