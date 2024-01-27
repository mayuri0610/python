# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

l=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

l.remove("Yellow")
l.remove("Pink")
l.remove("Red")
print(l)


