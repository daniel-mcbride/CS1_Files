def middle_elements(list1, list2):
    if len(list1) % 2 == 0 or len(list2) % 2 == 0:
        return "One or both lists are of even sizes. Can't be processed."
    else:
        middleIndex1 = int(len(list1) / 2)
        middleIndex2 = int(len(list2) / 2)
        
        middleElement1 = list1[middleIndex1]
        middleElement2 = list2[middleIndex2]

        newList = [middleElement1, middleElement2]

        return newList

testList1 = [9, 80, 204]
testList2 = [5, 6, 7, 8, 9]

print(middle_elements(testList1, testList2))
