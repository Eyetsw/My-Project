wordA = input("Enter wordA :")
wordB = input("Enter wordB :")

setA = set(wordA)
setB = set(wordB)

print("same %s" % "".join(setA.intersection(setB)))
print("differ %s" % "".join(setA.difference(setB)))
