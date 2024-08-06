
X = int(input("Enter ur number x : "))
Y = int(input("Enter ur number y : "))
Z = int(input("Enter ur number z : "))

print("X = %d, Y = %d, Z = %d" % (X, Y, Z))

if X > Y :
    if X > Z :
        print(X)
    else :
        print(Z)
else : 
    if Y > Z :
        print(Y)
    else :
        print(Z)
            
points = []  
number = int(input("Enter number of students: "))  
i = 1
for i in range(number): 
    point = int(input("Enter point of student {}: ".format(i+1)))  
    if point < 0 or point > 100:
        print("Please try again")
        continue
    points.append(point) 

print( points)  


i = 1
for j in points :

    if (j >= 80 and j <= 100) :
        print("Student %d A" %i)
        i += 1
    elif (j >=70 and j <= 79):
        print("Student %d B"%i)
        i += 1
    elif (j >=60 and j <= 69):
        print("Student %d C"%i)
        i += 1
    elif (j >=50 and j <= 59):
        print("Student %d D"%i)
        i += 1
    else :
        print("Student %d F"%i)
        i += 1