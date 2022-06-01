from cgi import print_arguments
from ssl import OP_NO_RENEGOTIATION


print("\n ====== Dictionary ======\n")

myDict = {
    "name": "Zaeema Anwar",
    "age": 21,
    "email": "thezaeemaanwar@gmail.com",
    "address": "26 westwood colony Canal Rd Lahore"
}
print(myDict)

print("\nLength of dictionary: ", len(myDict))

print("\nName attribute in dictionary: ", myDict["name"])

print("\nAll keys of dictionary: ", myDict.keys())

myDict.update({"name": "Ehmad Saeed"})
print("\nUpdate Dict Values: ", myDict)

myDict["gender"] = "male"
print("\nAdding Item in dict: ", myDict)

print("\nLoop over whole dict: \n---------------------")
for el in myDict:
    print(el, ": ", myDict[el])

print("\nValues only: \n------------")
for el in myDict.values():
    print(el)

print("\nKeys only: \n---------")
for key in myDict.keys():
    print(key)

print("\nBoth key values: \n----------------")
for key, value in myDict.items():
    print(key, ": ", value)

myDict.pop("age")
print("\nRemoving age from dict: ", myDict)

myDict.popitem()
print("\nRemove last inseted item: ", myDict)

myDict.clear()
print("\nClear whole dictionary: ", myDict)
