values=[2,4,1,-3,-5,11]
negative_value=min(i for i in values if i<0)
positive_value=max(j for j in values if j%2 == 0)
odd_values=sum(k for k in values if k%2 != 0 and k>0)
print(negative_value,positive_value,odd_values)
#print(positive_value)
#print(odd_values)









