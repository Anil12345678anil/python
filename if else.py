'''if(5>10):
    print("yes")
else:
    print("no")'''
"""email=(input("enter age1:"))
age2=int(input("enter age2:"))
if(age1>age2):
    age3=age1+age2
    print("my age added",age3)
else:
    age3=age1-age2
    print("my age sub",age3)"""



email="anil"
password="1234567890"
uemail=str(input("enter email:"))
upass=str(input("enter password:"))
if(email == uemail ):
    if(password == upass):
        print("login success")
    else:
        print("login failed due to incorrect password")
else:
    print("login failed due to incorrect email")
