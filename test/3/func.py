# 参数类型

# 必须参数
def add1(x, y):
    return x + y
print(add1(1, 2))

# 默认参数
def add2(x, y=1):
    return x + y
print(add2(1))

# 关键字参数
def add3(x, y):
    return x + y
print(add3(x=1, y=2))

# 可变参数
def add4(*param):
    sum = 0
    for i in param:
        sum += i
    return sum
print(add4(1, 2, 3))

# 关键字可变参数
def city_temp(**param):
    for key, value in param.items():
        print(key, ':', value)
result = city_temp(hz='32c', sz='30c', gz='31c')


# 变量作用域
# def func1():
#     x = 1
# print(x)


def func2():
    global x
    x = 1
func2()
print(x)
