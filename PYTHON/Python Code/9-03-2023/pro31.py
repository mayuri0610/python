# 31. Write a Python program to count the number of elements in a list within a specified range. 

l=[10,4,1,5,4,74,8,5,62,14,25,36,47,58,69,12,23,56,45,78,98,65,324,17,5,72,41,1,10,30,80,9,30,60,40]
count=0
for i in l:
    if ((i<=200) and (i>=25)) :
        count+=1
print(count)
