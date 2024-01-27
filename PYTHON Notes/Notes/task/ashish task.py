a=[10,50,90,70,50,30]
b=[7,8,10,50,20,60]
a.extend(b)
print(a)
b.clear()
print(b)
for i in a:
    if i not in b:
        b.append(i)
print(b)
l=[]
for i in range(len(b)):
    ans=max(b)
    l.append(ans)
    b.remove(ans)
print(l)



#******************************  MAYURI ********************************************


l1=[35,60,95,10,25,6]
l2=[5,6,7,100,3,7,10]
l3=l1+l2
print(l3)
l=[]
for i in l3:
    if i not in l:
        l.append(i)

print(l)

l4=[]

for i in range(len(l)) :
    ans=min(l)
    l4.append(ans)
    l.remove(ans)

print(l4)















