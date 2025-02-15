string = input ("provide string to calculate frequency : ")

frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1 
print(frequency)