# 19. Write a Python program to calculate the difference between the two lists.

l1=[1, 3, 5, 7, 9]
l2=[1, 2, 4, 6, 7, 8]

s1=set(l1)
s2=set(l2)

s3=s1.difference(s2)
print(s3)
s4=s2.difference(s1)
print(s4)
s5=s3.union(s4)
l=list(s5)
print(l)