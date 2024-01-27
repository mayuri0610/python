
# variable length argument 

# Variable length argument is an argument that can accept any number of values. 
# The variable length argument is written with * symbol.
# It stores all the value in a tuple.

def add (x, *num) :
  z = x+num[0]+num[1]
  print(z)

add(3,5,6)


def add (*num) :
  z=num[0]+num[1]+num[2]
  print(z)

add(5, 2, 4)



# dont use for this like

def add (*num,y) :
  z=num[0]+num[1]+y
  print(z)

# add(a=5,b=2,4)          # positional argument follows keyword argument
# add(5,2,4)          


# def add (*num) :
#   z=num[0]+num[1]+num[2]
#   print(z)

# add(a=5,b=2,c=4)          # calling function me kabhi bhi keyword argument nahi dalna 
