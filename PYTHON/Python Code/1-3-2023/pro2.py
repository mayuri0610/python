# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum(a) :
    total=0
    for i in a :
        total+=i

    return total

l=(8,2,6,9,8,4)
ans=sum(l)
print(ans)
