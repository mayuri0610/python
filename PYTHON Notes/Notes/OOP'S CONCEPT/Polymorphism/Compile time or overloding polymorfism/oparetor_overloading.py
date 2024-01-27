



class example:
 
    def __init__(self):
        print("One")
 
    def __init__(self):
        print("Two")
 
    def __init__(self):
        print("Three")
 
 
e = example()




class complex:
    def __init__(self, a, b ,c):
        self.a = a
        self.b = b
        self.c = c

     # adding two objects
    def __sub__(self, other):
        return self.a + other.a, self.b + other.b ,self.c + other.c
 
Ob1 = complex(1, 2, 3)
Ob2 = complex(2, 3, 3)
Ob3= Ob1 + Ob2 
print(Ob3)