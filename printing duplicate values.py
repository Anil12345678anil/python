anil=[]
n=int(input("list size:"))
for i in range(0,n):
    ele=input("enter list elements:")
    anil.append(ele)
    print(anil)


tagore=[]
n=int(input("list size:"))
for j in range(0,n):
    ele=input("enter list elements:")
    tagore.append(ele)
    print(tagore)

    for i in anil:
        for j in tagore:
            if i==j:
                print(i)