# 3. Write a Python function to multiply all the numbers in a list. 
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336


def multi(a) :
    total=1
    for i in a :
        total*=i
    return total

l=(8, 2, 3, -1, 7)
ans=multi(l)
print(ans)
