# 二分查找，又叫折半查找
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:  # li[mid] < val
            left = mid + 1
    else:
        return None