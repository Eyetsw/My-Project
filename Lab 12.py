word = input("Add ur word :")

vowels = {"a" : 0,
          "e" : 0,
          "i" : 0,
          "o" : 0,
          "u" : 0}

for x in word :
    if (x.lower() in vowels) :
        vowels[x.lower()] += 1
print(vowels)