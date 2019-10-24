# 顺序查找，又叫线性查找
def linear_search(li, val):
    for index, value in enumerate(li):
        if value == val:
            return index
        else:
            return None