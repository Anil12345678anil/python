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


user={'anil' : 123456789,'tagore' : 1122,'nandan' : 2233}
uemail=str(input("enter email:"))
upass=int(input("enter password:"))
#uotp=str(input("enter otp:"))
for i in user:
    if (i == uemail):
        if (user[i] == upass):
            print("login success")
        else:
            print("login failed")
'''
user={'s':9876,'z':1234,'a':6789}

uemail=str(input("enter mailid"))
upassword=int(input("enter password")) 
for i in user :
    if(i == uemail):
        if(user[i] == upassword):
            print("Login successfull")

'''
'''if(email == uemail ):
    if(password == upass):
        print("login success")
    else:
        print("login failed due to incorrect password")
else:
    print("login failed due to incorrect email")
'''