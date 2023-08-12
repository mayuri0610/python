# 27. Write a Python program to find the second smallest number in a list. 
l=[1, 1, 1, 0, 0, 0, 2, -2, -2]
l1=[]

for i in l:
    if i not in l1:
        l1.append(i)
l1.sort()
print(l1[1])



# s=set(l)
# l=list(s)
# l.sort()
# print(l)
# print(l[1])