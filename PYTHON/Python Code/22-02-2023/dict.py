
l={0,20,30,40}

d={1:"amit" , 2:{1:"amit" , 2: 'ashish',3:"ashmita",4:"durga"} ,3:"ashmita",4:"durga"}
print(d[2][2][4])

# ****can i use list as key in dictionary python 

# Duplicate keys are not allowed.
# Second, a dictionary key must be of a type that is immutable. 
# For example, you can use an tuple integer, float, string, or Boolean as a dictionary key.
# However, neither a list nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutable.
# becuase list have store dublicate value means the  address is not same for duplicate value
# tuple address are same for dublicate value 

# ******marge
# fruits = ["Apple", "Pear", "Peach", "Banana"]
# prices = [0.35, 0.40, 0.40, 0.28]

# fruit_dictionary = dict(zip(fruits, prices))

# print(fruit_dictionary)
# Our code returns:

# {'Apple': 0.35, 'Pear': 0.4, 'Peach': 0.4, 'Banana': 0.28}






