from copy import deepcopy
list1 = [[1, 2], 3, 4]
list2 = list1.copy()
list3 = deepcopy(list1)
list1[0][1] = 100
list1[1] = 200
print(list1)
print(list2)
print(list3)

