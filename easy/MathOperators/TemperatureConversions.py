mode = input ("select the conversion type FC or CF :")

if mode == "FC":
    celcius = input (" provide celcius degrees : ")
    fahrenheit = (int(celcius) * 9/5) + 32
    print(str(fahrenheit) + " " + "fahrenheit")
elif mode == "CF":
    fahrenheit = input (" provide fahrenheit degrees : ")
    celcius = (int(fahrenheit) - 32) * 5/9
    print(str(celcius) + " " + "celcius")
else:
    print("invalid entry")
    