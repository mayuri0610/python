# my_tuple = (1, 2, 3, 4, 5)
# result = my_tuple[1:4:2]
# print(result)

# (2, 4)



# l=['abc', 'xyz', 'aba', '1221','a']
# count=0

# for i in l:
#     if len(i)>=2 and i[0]==i[-1]:
#         count=count+1

# print(count)



# str ="pynative"
# print(str[1:3])



# l=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # l=[10,4,5,7,8,10,5,99]

# l=set(l)
# print(l)
# l=list(l)
# print(l)




# l=[4,5,8]

# count=0
# for i in l:
#     count+=1  
# if count==0:
#     print("list is empty")
# else:
    # print("list is not empty  ")






# ****************************  LIST ****************************


# List – A list represents a group of elements. 
# A list can store different types of elements which can be modified. 
# Lists are dynamic which means size is not fixed. 
# Lists are represented using square bracket [ ].


# Feature of List:=

# Order wise data (we can say objects)
# Heterogeneous data are possible in list           exa: l = ["string", "integer", "boolean", "float", "double"]
# List represented by [ ] square bracket
# Duplicate data are also allowed
# List by nature it is growable  
# Mutable or changeable




# List Items

# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.



# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# If you add new items to a list, the new items will be placed at the end of the list.


# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.


# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:














# l1=[10,20,30,40,50,60,70,80,90]
# l2=[]
# for i in l1:
#     l2.append(i)
    
# print(l2)

# [10, 20, 30, 40, 50, 60, 70, 80, 90]


# l=["ankush","Shatrupa","Mansi","Yogeshwar","Ayush"]

# str1=input("Enter a string : ")    # mayuri  
# str1len=len(str1)               #6

# for i in l:
#     if len(i)>str1len:
#         pass
#     else:
#         l.remove(i)
# print(l)



# x=[7, 8, 9, 5, 6, 0, 1]
# for i in range(len(x)):
#     # calculate square of each number
#     square = x[i] * x[i]
#     x[i] = square
    

# print(x)

# [49, 64, 81, 25, 36, 0, 1]



#*******************************  range    ****************



# for x in range(1,6):
#   print(x) 

# 1
# 2
# 3
# 4
# 5


# for x in range(6):
# for x in range(1,6):
# for x in range(0,6,2):
#   print(x) 

# 0
# 1
# 2
# 3
# 4
# 5


# 1
# 2
# 3
# 4
# 5


# 0
# 2
# 4



# x=[5, 5, 6, 9, 8, 4, 1, 0, 6, 5, 3, 2, 7]
# print(len(x))

# for i in range(len(x)):             # range(13)  means range(0,13)   means range chalegi 0 to n-1
#     print(x[i])                     
#     print(i)                     


#*******************************  sort    ****************


# cars = ['Ford', 'BMW', 'Volvo']

# cars.sort()

# print(cars)

# ['BMW', 'Ford', 'Volvo']




#*******************************  append    ****************




# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# ['a', 'b', 'c', 1, 2, 3]




#*******************************  insert    ****************


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# ['apple', 'orange', 'banana', 'cherry']



#*******************************  extend    ****************



# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']




#*******************************  clear    ****************


# fruits = ["apple", "banana", "cherry"]

# fruits.clear()

# print(fruits)

# []


#*******************************  pop    ****************


# fruits = ['apple', 'banana', 'cherry']
# fruits.pop(1)
# fruits.pop()
# print(fruits)

# ['apple', 'cherry']
# ['apple', 'banana']

# Optional. A number specifying the position of the element you want to remove, default value is -1, which returns the last item



#*******************************  remove    ****************


# fruits = ['apple', 'banana', 'cherry']

# fruits.remove("banana")

# print(fruits)

# ['apple', 'cherry']


# list.remove(elmnt)
# elmnt =	Required. Any type (string, number, list etc.) The element you want to remove



#*******************************  type    ****************


# fruits = ['apple', 'banana', 'cherry']

# fruitstype=type(fruits)

# print(fruitstype)

# <class 'list'>




#*******************************  max    ****************


# l = [254,6,5,9,189,354,687,4896,12]

# lmax=max(l)

# print(lmax)

# 4896




#*******************************  min    ****************


# l = [254,6,5,9,189,354,687,4896,12]

# lmin=min(l)

# print(lmin)

# 5



#*******************************  len   ****************



# fruits = ['apple', 'banana', 'cherry',1,4,8,0]

# fruitslen=len(fruits)

# print(fruitslen)

# 7


#*******************************  index    ****************



# fruits = ['apple', 'banana', 'cherry']
# x = fruits.index("cherry")

# print(x)

# 2

# fruits = [4, 55, 64, 32, 16, 32]
# x = fruits.index(32)

# print(x)

# 3

# list.index(elmnt)
# elmnt =	Required. Any type (string, number, list, etc.). The element to search for





#******************************* count  ****************


# fruits = ["apple", "banana", "cherry", 1,4,7,9,2,2,7,7,7,7]
# x = fruits.count(7)

# print(x)

# 5

# list.count(value)
# value =	Required. Any type (string, number, list, tuple, etc.). The value to search for.



#*******************************  reverse    ****************


# fruits = ['apple', 'banana', 'cherry']

# fruits.reverse()

# print(fruits)

# ['cherry', 'banana', 'apple']


#*******************************  copy    ****************


# fruits = ["apple", "banana", "cherry",1,4,7,8,4]
# x = fruits.copy()

# print(x)

# ["apple", "banana", "cherry",1,4,7,8,4]



#*******************************  replace indexing    ****************



# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"

# print(thislist)

# ['apple', 'blackcurrant', 'cherry']


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# ['apple', 'blackcurrant', 'watermelon', 'cherry']


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']





#******************************  Negetive and Positive inedxing or sliceing    ****************



# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# ['orange', 'kiwi', 'melon']

#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,




# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])                   # 0 to 3 tak chalega means (n-1)

# ['apple', 'banana', 'cherry', 'orange']

#This will return the items from index 0 to index 4.

#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included
#positive indexing means starting from the front of the list.
# Remember that the first item has the index 0,



# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# ['cherry', 'orange', 'kiwi', 'melon', 'mango']

#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third 




# x = [7,2,3,5,6,0,1]
# y=x[2:5]
#y= x[2:5:-1]
# print(y)

# []

# x = [7,2,3,5,6,0,1,4,8,9,6,5,5]
# y=x[::-1]
# print(y)

# [5, 5, 6, 9, 8, 4, 1, 0, 6, 5, 3, 2, 7]


# x = [7,2,3,5,6,0,1,4,8,9,6,5,5]
# y=x[-3:-8]
# print(y)

# []

# x = [7,2,3,5,6,0,1,4,8,9,6,5,5]
# print(range(len(x)))
# for i in range(len(x)):
#     print('We are printing one element at a time:',x[i])






