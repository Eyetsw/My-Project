def drawline(number) :
    i = 1
    while i <= number :
        print("*",end = "")
        i += 1
    print("")
    
def drawsquare(number) :
    for i in range(1,(number + 1),1) :
        for j in range(1,(number + 1),1) :
            print("+",end = "")
        print("")   

def drawtriangle(number) :
    for i in range(1,(number + 1),1) :
        for j in range(1,(i+ 1),1) :
            print("&",end = "")
        print("")   
    

number = int(input("Enter ur number :"))
drawline(number)
number = int(input("Enter ur number :"))
drawsquare(number)
number = int(input("Enter ur number :"))
drawtriangle(number)   
