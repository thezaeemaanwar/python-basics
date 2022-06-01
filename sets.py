mySet = {2, 4, 31, 5, 6, 7, 8, 10, 13, 19, 51}

print("\nGet Even Numbers from set: ")
evenNumbers = set(filter(lambda el: el % 2 == 0, mySet))
print("E = ", evenNumbers)


print("\nPrime Numbers from set: ")
primeNumbers = set(filter(lambda n: n%2 and n%3 and n%5 and n%7, mySet))
print("P = ",primeNumbers)
