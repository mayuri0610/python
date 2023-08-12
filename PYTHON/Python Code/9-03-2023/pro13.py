# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

print("[")
for i in range(0,3) :
    print("[")

    for j in range(0,4) :
        print("[")

        for k in range(0,6) :
            num="'*'"
            print(num,",")

        print("]")
        if j in range(0,3):
            print(",")

    print("]")
    if i in range(0,2) :
        print(",")       
print("]") 

