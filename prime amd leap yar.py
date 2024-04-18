def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        return year % 400 == 0
    else:
        return True


numbers = list(map(int, input("Enter numbers separated by space: ").split()))


for number in numbers:
    prime = is_prime(number)
    leap = is_leap_year(number)
    print(f"{number} is {'a prime number' if prime else 'not a prime number'} and {'a leap year' if leap else 'not a leap year'}.")