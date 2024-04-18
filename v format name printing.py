name = input("Enter your name: ")
length = len(name)
for i in range(length):
    for j in range(length*2-1):
        if j == i or j == (length*2-2-i):
            print(name[i], end='')
        else:
            print(' ', end='')
    print()

