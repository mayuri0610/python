
# Keyword Arguments

# These arguments are passed to the function with name-value pair so keyword arguments can identify the formal argument by their names. 
# The keyword argument’s name and formal argument’s name must match.




def Arithmatic(a=0,b=0):
    print(a+b)

Arithmatic(a=10)

def Arithmatic(a=1000,b=0):
    print(a+b)

Arithmatic(b=20)


def Arithmatic(a=0,b=0):
    print(a+b)

Arithmatic(b=20,a=10)


# def Arithmatic(a=0,b=0,c,d):          #dont write that

def Arithmatic(a,b,c=0,d=0):
    print(a+b+c+d)

Arithmatic(c=30,b=20,a=10,d=60)


def Arithmatic(a,b,c,d):
    print(a+b+c+d)

Arithmatic(30,20,d=10,c=60)



# dont  write that like


def Arithmatic(a,b,c,d):
    print(a+b+c+d)

# Arithmatic(60,30,b=20,a=10)           # Arithmatic() got multiple values for argument 'a'
# Arithmatic(60,30,a=10,b=20)           # Arithmatic() got multiple values for argument 'a'
# Arithmatic(b=20,a=10,60,30)           # positional argument follows keyword argument
# Arithmatic(30,20,d=10,60)             # positional argument follows keyword argument

# Arithmatic(d=10,c=60,30,20)           # positional argument follows keyword argument

