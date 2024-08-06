import math
a = input("Enter a position (x1,y1) :")
b = input("Enter b position (x2,y2) :")

x1,y1 = a.split(",")
x2,y2 = b.split(",")

print(x1,y1)
print(x2,y2)

A = math.pow((int(x1) - int(x2)),2)
B = math.pow((int(y1) - int(y2)),2)
print(A)
print(B)
L = math.sqrt(int(A) + int(B))
print(L)

print("---------------------------------")

L2 = math.sqrt(math.pow(int(x1)-int(x2),2)+ math.pow(int(y1)-int(y2),2))
print(L2)
 