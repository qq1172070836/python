n = 100
# 用循环实现
# while n > 0:
#     n = n//2
#     print(n)

# 用函数实现
def calc(n):
    n = n//2
    print(n)
    if n > 0:
        calc(n)
    print(n)
calc(n)