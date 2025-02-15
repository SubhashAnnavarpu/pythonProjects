light = input ("Provide the light color: ")
obstacle = input ("provide if obstacle is present or not Y/N : ")

if light == "Green" and obstacle == "N": 
    print ("GO")
elif light == "Green" and obstacle == "Y": 
    print ("STOP")
elif light == "Red" and obstacle == "N": 
    print ("STOP")
elif light == "Red" and obstacle == "Y": 
    print ("STOP")
elif light == "Yellow" and obstacle == "N": 
    print ("GO SLOW")
elif light == "Yellow" and obstacle == "Y": 
    print ("STOP")
else:
    print ("invalid entry")

