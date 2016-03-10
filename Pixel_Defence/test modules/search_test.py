def linearSearch(myItem, myList):
    found = False
    position = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position = position + 1
    return found

theList = ["apple", "banana", "orange"]
theItem = "apple"
isFound = linearSearch(theItem, theList)
if isFound:
    print("Found")
else:
    print("Not found")
