name = input("Enter your name: ")
length = len(name)
for i in range(length):
    for j in range(length):
        if i == 0 or length-1 == i or (i + j) == length - 1:
            print(name[j], end='')
        else:
            print(' ', end='')
    print()

