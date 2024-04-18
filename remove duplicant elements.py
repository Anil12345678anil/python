list1=[10,20,30,50,20,30,40]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
        
print(list2)