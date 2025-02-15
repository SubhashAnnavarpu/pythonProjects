import re
password = input("please provide password : ")

if re.match("^[a-zA-Z0-9]{8}$",password):
    print("valid password")
else:
    print("invalid password")
