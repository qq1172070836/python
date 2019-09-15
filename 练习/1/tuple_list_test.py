# Tuple
'''
不可变，查询：index，count     
一般转换成list再操作           
'''
tuple1 = ()
tuple2 = (1,)
print(type(tuple1), type(tuple2))

# List

# len max min + * in 切片 迭代

# 增
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['1', '2', '3']
print(list1 + list2)
list1.insert(5, 1)
print(list1)
list1.append(2)
print(list1)
list1.extend(list2)
print(list1)

# 删
list1.remove(1)
print(list1)
list1.pop(0)
print(list1)
del list1[0:2]
print(list1)
list1.clear()
print(list1)

# 改
# 索引赋值

# 查
num = list1.count(1)
print(num)
index_num = list1.index(1, 1, -1)
print(index_num)

# 排序，反转
list1.sort(key=str, reverse=True)
print(list1)

list1.reverse()
print(list1)
