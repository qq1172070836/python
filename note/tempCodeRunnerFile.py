list1 = [[1, 2], 3, 4]
list2 = list1.copy()
list1[0][1] = 100
list1[1] = 200
print(list1)
print(list2)