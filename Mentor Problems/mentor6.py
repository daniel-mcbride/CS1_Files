def filterDuplicates(unfilteredList):
    uniqueList = []

    for item in unfilteredList:
        if item not in uniqueList:
            uniqueList.append(item)

    return uniqueList

testList = [1, 1, 2, 3, 4, 5, 5, 6, 78]

print(filterDuplicates(testList))
