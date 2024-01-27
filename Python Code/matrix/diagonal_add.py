r=int(input("Enter the row="))
c=int(input("Enter the column="))
l1=[]
for i in range(r):
    l2=[]
    for j in range(c):
        a=int(input())
        l2.append(a)
    l1.append(l2)
print(l1)

# l3=[]

# for i in range(r):
#     for j in range(c):
#         if i==j :
#             l3.append(l1[i][j])
# print(l3)
# ans=sum(l3)
# print("Addition of daigonal=",ans)

sum=0
for i in range(r):
    for j in range(c):
        if i==j :
            sum=sum+l1[i][j]

print("Addition of daigonal=",sum)




