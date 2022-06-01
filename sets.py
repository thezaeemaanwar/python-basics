mySet={2,4,31,5,6,7,8,10}

print("\nGet Even Numbers from set: ")
evenNumbers = set(filter(lambda el:el%2==0, mySet))
print("E = ", evenNumbers)