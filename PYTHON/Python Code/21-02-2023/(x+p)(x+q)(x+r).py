x=int(input("Enter the value of x="))
p=int(input("Enter the value of p="))
q=int(input("Enter the value of q="))
r=int(input("Enter the value of r="))
ans=x**3+(p+q+r)*x**2+(p*q+q*r+r*p)*x+p*q*r
print("(x+p)(x+q)(x+r)=",ans)
