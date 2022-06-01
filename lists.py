print("\n====== LISTS ======\n")

myList = [4, 6, 3, 0, 3, 1, 46]
print("List: ", myList, "\n")

myList.sort()
print("Sorted List: ", myList, "\n")

print("Iterate through List:")
for el in myList:
    print(el)

print("\nIterate with index List:")
for idx, el in enumerate(myList):
    print(idx, ". ", el)

print("\nCopy a list:")
copiedList = myList.copy()
print(copiedList)

print("\nNumber of elements in list: ", len(myList))

print("\nAppend to list: ")
myList.append(4)
myList.append(4)
print("Updated List: ", myList)

print("\nNumber of 4s in list: ", myList.count(4))

anotherList = [2, 4, 5, 6]
print("\nAdd another list to the end: ")
myList.extend(anotherList)
print("Updated List", myList)

print("\nIndex of 6: ", myList.index(6))

print("\nRemove 46 from the list (Using pop)")
myList.pop(myList.index(46))
print("Updated List: ", myList)

print("\nRemove first 3 fron list (using remove)")
myList.remove(3)
print("updated List: ", myList)

myList.sort()
myList.reverse()
print("\nDescending order of list: ", myList)

print("\nSlicing list inde 2 to 6 ", myList[2:6])

