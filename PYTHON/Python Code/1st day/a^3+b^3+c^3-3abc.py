a=int(input("Enter the value of a="))
b=int(input("Enter the value of b="))
c=int(input("Enter the value of c="))
ans=(a+b+c)*(a**2+b**2+c**2-a*b-b*c-c*a)
print("a^3+b^3+c^3-3abc=",ans)