

# CONSTRUCTOR OVERLOADING


# If the constructor is written two times with different signatures OR parameter, we call constructor overloading.
# Signature means a different number of parameters. 








# constructor overloading

# class Strikers():
   
    # def __init__(self,a,b,c):
    #     self.a=a
    #     self.b=b
    #     self.c=c

#     def __init__(self,*a):
#         if len(a)<3:
#             self.sss= sum(len(a))

#         if len(a)>=3 and len(a)<6:
#             self.sss= sorted(len(a))

#     def aaa(self):
#         # print(self.a+self.b)
#         print(self.sss)



# objects = Strikers(1,2,3)
# objects.aaa()

# class Strikers:
#     def __init__(self, *args):
#         if len(args) < 2:
#             self.ans = 1  # Change initial value to 1
#             for i in args:
#                 self.ans *= i  # Multiply instead of 0 to maintain product

#             print(self.ans)
#         elif 2 <= len(args) < 5:  # Corrected condition
#             self.ans = 0  # Change initial value to 0
#             for i in args:
#                 self.ans += i

#             print(self.ans)
#         elif len(args) >= 5:  # Corrected condition
#             # Add your code for this case here
#             pass



# obj = Strikers(1, 2)



class Strikers:
    def __init__(self, a=0, b=0, c=0, d=0):
        if (a is not None and b is not None and c is  None and d is None):
            print(a + b )
        elif(a is not None and b is not None and c is not None and d is None):
            print(a * b * c)
        

obj = Strikers(1, 2,5)

