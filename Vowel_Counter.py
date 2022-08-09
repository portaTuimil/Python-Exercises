#Vowel counter

phrase = str(input('Introduce a phrase: '))
vowels = 'aeiouAEIOU'
c = 0
for i in phrase:
    if i in vowels:
        c = c + 1
print('The number of vowels is: ',c)
