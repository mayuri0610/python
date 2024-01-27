

# METHOD OVERRIDING


# If we write method in the both classes, parent class and child class then the parent class’s method is not available to the child class. 
# In this case only child class’s method is accessible which means child class’s method is replacing parent class’s method.
# Method overriding is used when programmer want to modify the existing behavior of a Method.



# Similarly in the sub class, if we write a method with exactly same name as that of super class method, it will override the super class method. This is called method overriding .



class Add:
    def result(self, a, b):
	    print(a+b)
		

class Multi(Add):
    def result(self, a, b):
	    print(a*b)
		
m = Multi()
m.result(10, 20)




# achive method overriding

class Add:
    def result(self, a, b):
	    print(a+b)
		
class Multi(Add):
    def result(self, a, b):
        print(a*b)
        super().result(a,b)

		
m = Multi()
m.result(10, 20)




