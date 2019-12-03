def first_last(intList):
    first = intList[0]
    last = intList[-1]

    if first == last:
        return True
    else:
        return False


myList = [5, 7, 28, 90, 6]

print(first_last(myList))
