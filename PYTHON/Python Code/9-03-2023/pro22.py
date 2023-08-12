# Write a Python program to find the index of an item in a specified list.

l=[1,8,5,6,9,7,4,2,3]
n=int(input("Enter the number in list="))
for i in l:
    if i==n :
        print(l.index(i))