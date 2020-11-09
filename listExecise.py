# creates list
ages = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]

# prints list
print(ages)

#Prints highest value
print("Highest age is:",max(ages))

#print altered list
amendAge = dict.fromkeys(ages)
agelist = list(amendAge)

print("List without duplicates:",(agelist)