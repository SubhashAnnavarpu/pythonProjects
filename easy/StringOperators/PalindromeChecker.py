string = input("provide a word to check palindrome : ")

if string == string[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
