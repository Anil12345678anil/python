email="anil"
password="1234567890"
otp="1234"
uemail=str(input("enter email:"))
upass=str(input("enter password:"))
uotp=str(input("enter otp:"))
if(email == uemail ):
    if(password == upass):
        print("login succes")
        if(otp == uotp):
            print("transaction succesfull")
        else:
            print("tranction failed")
    else:
        print("login failed due to incorrect password")
else:
    print("login failed due to incorrect email")
