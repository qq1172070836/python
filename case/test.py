import xlwt

fopen = open("E:/我的资料/资料/电脑维护/技术部 电商电脑硬件信息统计/陈嘉兴.txt", 'r')
lines = fopen.readlines()
# 新建一个excel文件
file = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 新建一个sheet
sheet = file.add_sheet('data')

# 写入a.txt，a.txt文件有15行文件
i = 0
for line in lines:
    sheet.write(i, 0, line)
    i = i + 1

# 写入b.txt，
j = 15  # 从15行写入
fopen2 = open("E:/我的资料/资料/电脑维护/技术部 电商电脑硬件信息统计/陈军军.txt", 'r')
lines2 = fopen2.readlines()
for line in lines2:
    sheet.write(j, 0, line)
    j = j + 1
file.save('test.xls')