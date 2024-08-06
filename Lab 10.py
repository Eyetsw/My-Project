#count หาว่าเลขนั้นมีกี่ตัว
#print(number2.count(8))

word = input("Add ur word :")
a = 0
e = 0
i = 0
o = 0
u = 0

for x in word :
    if(x) == "a" :
        a += 1
    elif(x)== "e" :
        e += 1
    elif(x)== "i" :
        i += 1
    elif(x)== "o" :
        o += 1
    elif(x)== "u" :
        u +=1
print("a = %d,e = %d,i = %d,o = %d,u = %d" % (a,e,i,o,u))

