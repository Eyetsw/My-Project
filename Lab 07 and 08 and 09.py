#สี่เหลี่ยม
# Number = int(input("Enter ur number: "))

#for i in range(1,(Number + 1),1):
 #   for j in range(1,(Number + 1),1) :
 #      print("*",end = "")
 #   print("")

#สามเหลี่ยม
#Number = int(input("Enter ur number: "))

#for i in range(1,(Number + 1),1) :
#   for j in range(1,(i + 1),1) :
#      print("*",end ="")
#   print("")
 
 
Number = int(input("Enter ur number: ")) 

for i in range(2,(Number +1),1) :
   for j in range(2,i,1):
      if (i % j == 0) :
         break
   else :
      print(str(i) + "")
 
 