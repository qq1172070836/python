# 全局变量
c = 10
def demo():
    # 局部变量
    c = 20
print(c)

# 局部变量 => 全局变量
# global关键字
def demo():
    global c
    c = 10
demo()
print(c)