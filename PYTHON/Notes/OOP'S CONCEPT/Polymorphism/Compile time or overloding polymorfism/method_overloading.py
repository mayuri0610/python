

# METHOD OVERLOADING

# When more than one method with the same name is defined in the same class, it is known as method overloading. 
# In python, If a method is written such that it can perform more than one task, it is called method overloading. 




# class Arithmetic():

#     # def add(self, a,b):
#     #     print(a + b)

#     # def add(self, a,b,c):
#     #     print(a + b +c)


#     def add(self, a=0, b=0, c=0, d=0):
#         if (c == None and d== None  ):
#             print(a + b )
#         elif(d == None ):
#             print(a + b + c)
#         elif(a != None and b != None and c != None and d != None):
#             print(a + b + c+d)


#     # def add(self, *a):
#     #     length = len(a)
#     #     j=0
#     #     k=1
#     #     if length <3:
#     #         for i in range(length):
#     #             j=j+i

#     #         print(j)
#     #     elif length > 3:
#     #         for i in range(length):
#     #             k=k+i
#     #         print(k)

# obj=Arithmetic()
# obj.add(1,2,3)



class Strikers:
    def add(self, *args):
        if len(args) < 2:
            self.ans = 1  # Change initial value to 1
            for i in args:
                self.ans *= i  # Multiply instead of 0 to maintain product

            print(self.ans)
        elif 2 <= len(args) < 5:  # Corrected condition
            self.ans = 0  # Change initial value to 0
            for i in args:
                self.ans += i

            print(self.ans)
        elif len(args) >= 5:  # Corrected condition
            # Add your code for this case here
            pass

obj=Strikers()
obj.add(1,2,3)


