# Write a Python program to find the list of words that are longer than n from a given list of words.
l = ['mayuri', 'ram', 'om', 'shree','munnu','moksh'] 
new = [] 
n = 3 
for i in l :     
    if len(i) > n :         
        new.append(i)  
print(new)