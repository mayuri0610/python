row=int(input("Enter the row="))
col=int(input("Enter the coloum="))
l=[]
for i in range(row):
    a=[]
    for j in range(col):
        ans=int(input())
        a.append(ans)
    l.append(a)
print(l)

l1=[]
for i in range(row):
    sum=0
    for j in range(col):
        sum=sum+l[i][j]
    l1.append(sum)

print("Addition of row=",l1)

l2=[]
for i in range(col):
    add=0
    for j in range(row):
        add=add+l[j][i]
    l2.append(add)

print("Addition of column=",l2)

