# Positional Arguments

def Arithmatic(a,b):
    print(a+b)

Arithmatic(10,20)



def add (**num) :
        z = num["a"]+num["b"]+num["c"]
        print(z)

add(c=3, a=5, b=2)



def add (x, *num) :
        z = x+num[0]+num[1]
        print(z)

add(3,5,6)


def add (*num) :
  z=num[0]+num[1]+num[2]
  print(z)

add(5, 2, 4)
