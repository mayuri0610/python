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



# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# ['a', 'b', 'c', 1, 2, 3]


# ************************* Slising ********************************************************************************************************


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# ['apple', 'blackcurrant', 'watermelon', 'cherry']




# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']



# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])
# print(thislist[0:4])      

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