# Number

# int
num1 = 10
num2 = 0b10
num3 = 0o10
num4 = 0x10
print(num1, num2, num3, num4)
# 进制之间的转换：int, bin, oct, hex

# float
num5 = 1/1
print(num5,type(num5))

import math
num6 = math.ceil(1.1)
print(num6)

from decimal import Decimal
num7 = 2.2-2.0
num8 = Decimal('2.2')-Decimal('2.0')
print(num7, num8)

# bool
num9 = True
num10 = False
print(num9 and num10)
print(num9 or num10)
print(not num9)

# complex
num11 = 1+2j
num12 = complex(1, 2)
print(num11 == num12)
print('============================')


# String
str1 = r'hello world\n'
str2 = " python "
num = ord('a')
print(str1+str2, str2*3, str1[0:-1:2], num)

# 增
print('%s %s' % (str1, str2))
print('{} {}'.format(str1, str2))
print(':'.join([str1, str2, str2]))

# 删
str3 = str1.replace('l', 'i', 2)
print(str3)

# 改
str4 = str2.upper()
str5 = str4.lower()
str6 = str1.capitalize()
str7 = str1.title()
print(str4, str5, str6, str7)
str8 = str2.strip()
print(len(str2), len(str8))
str9 = str1.split('l')
print(str9)

# 查
print(str1.index('l', 3, -1))
print(str1.count('l', 3, -1))
print('==========================================================')

# Tuple
'''
不可变，查询：index，count     
一般转换成list再操作           
'''


# List

print('==========================================================')


# Set
# Dict