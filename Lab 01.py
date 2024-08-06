
Name = input("Enter your Name : ")
Weight = int(input("Enter your Weight (Kg) : "))
Height = int(input("Enter your Height (CM) : "))
Bmi = float(Weight/((Height/100)**2))
print(" %s. Your Bmi is :%f" % (Name, Bmi))

