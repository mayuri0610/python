# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

l=[65,45,87,96,35,22,24,87,65,15,34,39,87,46,12]
l1=[]
for i in l:
    if(i%2!=0):
        l1.append(i)
print(l1)