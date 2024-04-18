def prime_num(num):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

def leap_num(num):
    if num>1:
        if num%4 == 0:
            if num%100 == 0:
                if num%400 ==0:
                    print(num,'is a leap year')
                else:
                    print(num,'is not a leap year')
            else:
                print(num,'is a leap year')
        else:
            print(num,'is not a leap year')
    else:
        print(num,'is not a leap year')



numbers = input('enter numbers separated by space :').split()
numbers = [int(num) for num in numbers]
for num in numbers:
    leap_num(num)
    prime_num(num)