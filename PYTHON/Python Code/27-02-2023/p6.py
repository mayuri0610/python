# Write a Python program to get a list, sorted in increasing order by the last element
# in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]



l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
for i in range(len(l)):     
    for j in range(i, len(l)):         
        if l[i][1] > l[j][1]:             
            temp = l[i]             
            l[i] = l[j]             
            l[j] = temp  

print(l)
