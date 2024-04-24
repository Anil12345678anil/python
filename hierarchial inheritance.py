class A:
    def prime_num(self,n):
        if n <= 1:
        print (n,'is not a magical prime number')
        elif n <= 3:
            print (n,'is a magical prime number')
        elif n % 2 == 0 or n % 3 == 0:
            print (n,'is not a magical prime number')
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    print(n,'is not a magical prime number')
                i += 6
                print(n,'is not a magical prime number')
class B(A):
    def neon_num(self):
        neon_num=(0,1,9)
        user=int(input("enter a number (0-9) : "))
        if user in neon_num:
            print(user,"is a neon number")
        else:
            print(user," is not a neon number")

class C(A):
    def x_format(self):
        name=str(input("enter name:"))
        length=len(name)
        for i in range(length):
            for j in range(length):
                if i==j or i+j == length-1:
                    print(name[i],end=' ')
                else:
                    print(' ',end=' ')
            print()

class D(A):
    def rev_string(self):
        name=str(input("enter name : "))
        print(name[::-1])
class E(B,C):
    def banking(self):
        def withdraw(account, amount):
            if amount > account['balance']:
                print("Insufficient funds!")
            else:
                account['balance'] -= amount
                account['transactions'].append(f"Withdrawal: ${amount}")
                print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

        def deposit(account, amount):
            account['balance'] += amount
            account['transactions'].append(f"Deposit: ${amount}")
            print(f"Deposit successful. Remaining balance: ${account['balance']}")

        def get_balance(account):
            return account['balance']

        def get_transaction_history(account):
            return account['transactions']

        # Create an account dictionary
        account = {
            'balance': 1000,
            'transactions': []
        }

        email="anil@gmail.com"
        password="1234"
        uemail=str(input("enter email:"))
        upass=str(input("enter password:"))
        if(email == uemail ):
            if(password == upass):
                print("login success")
            
        # Dictionary to map user choices to functions
                choices = {
                    '1': deposit,
                    '2': withdraw,
                    '3': get_balance,
                    '4': get_transaction_history
                }

                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Exit")

                    choice = input("Enter your choice: ")

                    if choice == '5':
                        print("Exiting program.")
                        break

                    if choice in choices:
                        if choice == '1' or choice == '2':
                            amount = float(input("Enter amount: "))
                            choices[choice](account, amount)
                        else:
                            print(choices[choice](account))
                    else:
                        print("Invalid choice. Please try again.")
        else:
            print("login failed")

obj1=D()
obj2=E()
obj1.prime_num(-5)
obj2.neon_num()
obj1.rev_string()
obj2.x_format()
obj2.banking()
