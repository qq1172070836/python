# 第3版，嵌套函数，返回内层函数的内存地址，但不执行内存函数
account = {
    'is_authenticated': False,
    'user': 'lin',
    'password': '1234'
}

def login(func):
    def inner(*args,**kwargs):
        if account['is_authenticated'] == False:
            user = input('请输入用户名：')
            password = input('请输入密码：')
            if user == account['user'] and password == account['password']:
                print('登录成功！')
                account['is_authenticated'] = True
                func(*args,**kwargs) # 认证成功，执行功能函数
            else:
                print('用户名或密码错误！')
        else:
            print('用户已登录，验证成功！')
            func(*args, **kwargs)
    return inner

def home():
    print('----首页----')

@login
def guonei():
    print('----国内专区----')

def oumei():
    print('----欧美专区----')

@login
def rihan(vip_level):
    if vip_level > 3:
        print('----解锁本专区所有高级玩法----')
    else:
        print('----日韩专区----')

home()
# guonei = login(guonei)
# 返回的是内层函数的内存地址
# print(guonei)
guonei()
rihan(4)