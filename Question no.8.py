list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
i=0
c=[]
while i<len(list1):
    b=list1[i]
    if b in list1:
        c.append(b)
    i=i+1
print(c)
