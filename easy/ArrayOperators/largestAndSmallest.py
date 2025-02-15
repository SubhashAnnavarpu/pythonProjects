list = input ("provide the list of numbers :")


# for i in range(len(list)):
#    for j in range(i+1,len(list)):
#        if list[i] > list[j]:
#            print ("the largest number is :", i)
#            print ("the smallest number is :", j)
#       elif list[i]  list[j]:
#            print ("the largerst number is :",  j)
#            print ("the smallest number is :",  i)
#        else:
#             print("invalid input")
largest = max(list)
smallest = min(list)
print("largestmnumber : " + largest)