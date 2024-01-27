# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square numbers between 1 and 30 (both included).

l=[]
for i in range(1,31):
	l.append(i**2)
print(l[5:])

[1,2,3,4,5,6,7,8,9,10]