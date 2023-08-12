# Python program to reverse a three digit number

a=int(input("Enter the 3 digit number="))
n1=int(a%10)
a=int(a/10)
n2=int(a%10)
a=int(a/10)
ans=int(n1*100+n2*10+a)
print("Reverse a three digit number=",ans)



