import random 
otp=random.randrange(1000,9999)
print(" your otp is : ",otp)
user_input=int(input(" enter received otp :"))
if otp == user_input:
    print("login succes")
else:
    print("login fail")
    
    