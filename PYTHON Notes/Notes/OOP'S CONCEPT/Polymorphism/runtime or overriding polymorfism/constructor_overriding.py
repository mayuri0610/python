

# a constructor wrritten in both class parent class and clild class with same parameters. This is called constructor overriding. 

# That means the sub class constructor is replacing the super class constructor. This is called constructor overriding . 


# constructor overriding

print("*********************************************************************************************************************************************************")


# EXAMPLE 1


class Player:
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
        print(self.a1+self.b1)



class Strikers(Player):
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
        print(self.a1*self.b1)
        


strker=Strikers(10,20)




# achive constructor overriding

class Player:
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
        print(self.a1+self.b1)


class Strikers(Player):
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
        print(self.a1*self.b1)
        super().__init__(a,b)


strker=Strikers(10,20)


print("*********************************************************************************************************************************************************")

# EXAMPLE 2


#  constructor overriding

class Player:
    def __init__(self,name1):
        self.name1=name1
        print(self.name1)


class Strikers(Player):
    def __init__(self,name):
        self.name1=name
        print(self.name1)

strker=Strikers("MOKSH")



# achive constructor overriding



class Player:
    def __init__(self,name1):
        self.name1=name1
        print(self.name1)


class Strikers(Player):
    def __init__(self,name):
        self.name1=name
        print(self.name1)
        super().__init__(name)

strker=Strikers("MOKSH")



print("*********************************************************************************************************************************************************")

# EXAMPLE 3

#  error

# class Player:
#     def __init__(self,name):
#         self.name1=name

#     def bbb(self):
#         print(self.name1)


# class Strikers(Player):
#     def __init__(self,name):
#         self.name=name
        
#     def Aaaa(self):
#         print(self.name)

# strker=Strikers("mayuri")

# strker.Aaaa()
# strker.bbb()





class Player:
    def __init__(self,name):
        self.name1=name

    def bbb(self):
        print(self.name1)


class Strikers(Player):
    def __init__(self,name):
        super().__init__(name)
        self.name=name
        
    def Aaaa(self):
        print(self.name)

strker=Strikers("mayuri")

strker.Aaaa()
strker.bbb()





print("*********************************************************************************************************************************************************")


# EXAMPLE 4


# achive constructor overriding

class Player:
    def __init__(self,name,last):
        self.name=name
        self.last=last

    def bbb(self):
        print(self.name,self.last)


class Strikers(Player):
    def __init__(self,name,last):
        self.name=name
        self.last=last

    def aaa(self):
        print(self.name,self.last)

strker=Strikers("MUNNU","SONWANE")

strker.aaa()
strker.bbb()



