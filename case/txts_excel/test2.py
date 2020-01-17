import os, xlwt

# 创建excel表格
xlsx_file = xlwt.Workbook(encoding='utf8')
table = xlsx_file.add_sheet('data', cell_overwrite_ok=True)
table_head = ['硬件检查报告', '电脑使用者', '电脑型号', '处理器', '内存容量', '显卡', '硬盘', '主板', '网卡', '声卡', '显示器', '当前操作系统']
for i in range(len(table_head)):
    table.write(0, i, table_head[i])

# 读取txt内容
mypath = 'E:/我的资料/资料/电脑维护/技术部 电商电脑硬件信息统计'
myfiles = os.listdir(mypath)

for file in myfiles:
    with open((mypath + '/' + file), 'r') as f:
        lines = f.readlines()
        for line in lines:
            for i in range(len(lines)):
                table.write(myfiles.index(file)+1, i, lines[i])
                print(myfiles.index(file)+1, i, lines[i])

# # 修改电脑使用者
for file in myfiles:
    table.write(myfiles.index(file)+1, 1, file.replace('.txt', ''))

# 保存
xlsx_file.save('data.xls')