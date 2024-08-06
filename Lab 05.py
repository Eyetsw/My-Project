
#size M (THB) = 65
#size L (THB) = 80
#Add Bubble (THB) = size + 10
#Have ownglass (THB) = size - 5


size = input("Enter your size : ")
bubble = input("Wanna add bubble : ")
ownglass = input("Have own glass : ")

price = 0

if (size == "M") :
    price += 65 
    if (bubble == "Y") :
        price += 10
       
elif (size == "L"):
    price += 80 
    if (bubble == "Y") :
        price += 10
        
if (ownglass == "Y"):
            price -= 5       

print("Your bill is : %d THB" % (price))    