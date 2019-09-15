# String
str1 = r'hello world\n'
str2 = " Python "
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

# 判断
print(str1.isdigit())
print(str1.isalpha())
print(str1.isupper())
print(str1.islower())
print(str2.startswith(' '))
print(str2.endswith(' '))