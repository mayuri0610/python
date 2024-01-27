

# keyword variable length argument :

# Keyword Variable length argument is an argument that can accept any number of values provided in the form of key-value pair. 
# The keyword variable length argument is written with ** symbol.
# It stores all the value in a dictionary in the form of key-value pair.



dictationary = {"a": 1, "b": 2, "c":3}

print(dictationary["b"])



def add (**num) :
        z = num["a"]+num["b"]+num["c"]
        print(z)

add(c=3, a=5, b=2)


def add (x, **num) :
        z = x+num["a"]+num["b"]
        print(z)

add(3,a=5,b=6)

# dont use that like 

# add(3,5,6)        #add() takes 1 positional argument but 3 were given  (i.e. 1 hi positional argument lena chahiye but yaha pe 3no hi positional argument liye hai)






