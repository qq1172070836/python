s = '你好'
b = s.encode('utf-8')
print(b, type(b))
s = b.decode('utf-8')
print(s, type(s))