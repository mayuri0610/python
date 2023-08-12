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




r=int(input("Enter the row="))
c=int(input("Enter the coloum="))
m=[]
for i in range(r) :
    n=[]
    for j in range(c):
        a1=int(input())
        n.append(a1)
    m.append(n)
print(m)

m1=[]
for i in range(r):
    sum=0
    for j in range(c):
        sum=sum+m[i][j]
    m1.append(sum)
print("Addition of row=",m1)

m2=[]
for i in range(r):
    sum=0
    for j in range(c):
        sum=sum+m[j][i]
    m2.append(sum)
print("Addition of column=",m2)

list1=l1+m1
print(list1)

list2=l2+m2
print(list2)

liste3=[]
listo3=[]
for i in list1:
    if i%2==0:
        liste3.append(i)
    else:
        listo3.append(i)
print("row even number=",liste3)
print("row odd number=",listo3)

liste4=[]
listo4=[]
for i in list2:
    if i%2==0:
        liste4.append(i)
    else :
        listo4.append(i)

print("column even number=",liste4)
print("column odd number=",listo4)



