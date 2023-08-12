class Arithmetic:
    a=10                        #class variable
    @classmethod                #class method
    def add(cls):
        print(cls.a)


Arithmetic.add()

obj=Arithmetic()
obj.add()

