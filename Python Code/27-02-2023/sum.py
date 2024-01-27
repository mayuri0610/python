# l=[21,24,14,86,19,37,49,61,58,91,42]

# sum=0

# for i in l :
#     sum=sum+i

# print("total=",sum)

l=[]
n=int(input("Enter number of elements : "))

for i in range(0,n) :
    num=int(input("Enter the number="))
    l.append(num)
    ans=sum(l)

print(l)
print("Sum of all number in list=",ans)