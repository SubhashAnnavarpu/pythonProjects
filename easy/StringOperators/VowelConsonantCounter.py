string = input ( "provide a string to count the consonants and vowels : ")

vowels = 0
consonants = 0

for i in string:
    vowels += i in "aeiouAEIOU"
    consonants += i not in "aeiouAEIOU"
print("Total vowels :", vowels)
print("Total consonants :", consonants)
