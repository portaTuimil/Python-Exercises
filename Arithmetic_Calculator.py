import re

def arithmetic_arranger(listOfOperations, answerRequired):
    for i in range(0, len(listOfOperations)):
        operation = listOfOperations[i]
        result = 0

        if '+' in operation:
            splittedOperation = operation.split('+')
            result = int(splittedOperation[0]) + int(splittedOperation[1])
            operator = '+'
        elif '-' in operation:
            splittedOperation = operation.split('-')
            result = int(splittedOperation[0]) - int(splittedOperation[1])
            operator = '-'
        elif '/' in operation:
            splittedOperation = operation.split('/')
            result = int(splittedOperation[0]) / int(splittedOperation[1])
            operator = '/'
        elif '*' in operation:
            splittedOperation = operation.split('*')
            result = int(splittedOperation[0]) * int(splittedOperation[1])
            operator = '*'

        splittedOperation[0].replace(" ", "")
        splittedOperation[1].replace(" ", "")

        if answerRequired == True:
            print('\n', splittedOperation[0].rjust(20) , '\n', 
                operator.rjust(15), splittedOperation[1].rjust(4), '\n',
                '------'.rjust(20), '\n',
                str(result).rjust(20), '\n')
        else:
            print('\n', splittedOperation[0].rjust(20) , '\n', 
                operator.rjust(15), splittedOperation[1].rjust(4), '\n',
                '------'.rjust(20), '\n')
        


lst = []
while True:
    p0 = input('Introduce an Operation(write <none> if you have finished): ')
    if p0 != 'none':
        lst.append(p0)
    if p0 == 'none':
        break

optResult = input('Do you want result?(True/False): ' )

arithmetic_arranger(lst, optResult)