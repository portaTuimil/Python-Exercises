def arithmetic_arranger(listOfNumber, boolOfAnswer):
    listlen = len(listOfNumber)

    for i in range(0, listlen):
        listOfIteration = listOfNumber[i].split()

        n0 = len(listOfIteration[0])
        if n0 >= 4:
            n0 = 3
        elif n0 == 3:
            n0 = 4
        elif n0 == 2:
            n0 = 5
        elif n0 == 1:
            n0 = 6

        n2 = len(listOfIteration[2])
        if n2 >= 4:
            n2 = 0
        elif n2 == 3:
            n2 = 1
        elif n2 == 2:
            n2 = 2
        elif n2 == 1:
            n2 = 3

        
        if boolOfAnswer == 'True':
            if listOfIteration[1] == '+':
                result = int(listOfIteration[0]) + int(listOfIteration[2])
            if listOfIteration[1] == '-':
                result = int(listOfIteration[0]) - int(listOfIteration[2])
        else:
            break
        
        lenresult = len(str(result))

        if lenresult == 8:
            nr = 0
        elif lenresult == 7:
            nr = 1
        elif lenresult == 6:
            nr = 2
        elif lenresult == 5:
            nr = 3
        elif lenresult == 4:
            nr = 4
        elif lenresult == 3:
            nr = 5
        elif lenresult == 2:
            nr = 6
        else:
            nr = 7

        print(' '*n0, listOfIteration[0], '\n', listOfIteration[1], ' '*n2,  listOfIteration[2], '\n', '--------')

        print(' '*nr, result, '\n')
       
lst = []

while True:
    p0 = input('Introduce an Operation(write <none> if you have finished): ')
    if p0 != 'none':
        lst.append(p0)
    if p0 == 'none':
        break

optResult = input('Do you want result?(True/False): ' )

arithmetic_arranger(lst, optResult)