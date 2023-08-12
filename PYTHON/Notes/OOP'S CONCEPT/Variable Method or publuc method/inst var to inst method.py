# class Arithmetic:
#     def __init__(self) -> None:
#         self.a="mayuri"
#         self.b="moksh"
#         print(self.a,self.b)
#     def add(self):
#         print(self.a,self.b)

# obj=Arithmetic()
# obj.add()

class Arithmetic:
    def __init__(self,x,y) -> None:
        self.a=x                               #instance variable
        self.b=y
        # print(self.a,self.b)
    def add(self):                              #instance method
        print(self.a,self.b)

obj=Arithmetic(10,20)
obj.add()
