# 30. Write a Python program to get the frequency of elements in a list. 

l=[1,4,1,5,7,8,9,6,3,2,5,4,1,2,3,6,5,4,7,8,9,5,4,1,2,3,]
l1=[]
count=0
for i in l:
    if i not in l1:
        l1.append(i)

for i in l1:
    for j in l :
        if i==j :
            count+=1
    print(i,":",count)
    count=0
