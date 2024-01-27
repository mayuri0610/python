# 1. Write a Python function to find the maximum of three numbers. 


# positional argument


# def max_of_3(a,b,c) :

#     if(a>b and a>c) :
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
    
# ans=max_of_3(10,30,20)
# print(ans)


# Default argument

# def max_of_3(a=0,b=0,c=0) :

#     if(a>b and a>c) :
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
    
# ans=max_of_3(10,20)
# print(ans)

# keyword argument

def max_of_3(a=0,b=0,c=0) :

    if(a>b and a>c) :
        return a
    elif(b>a and b>c):
        return b3
    else:
        return c
    
ans=max_of_3(c=10,a=20,b=6)
print(ans)


