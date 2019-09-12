def reverse_list(list1):
    list2 = []

    for item in list1:
        list2.insert(0, item)

    return list2

testList = [1,2,3,4,5]

print(reverse_list(testList))
