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