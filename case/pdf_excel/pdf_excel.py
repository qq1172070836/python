import pdfplumber, xlwt

# 创建excel表格
xlsx_file = xlwt.Workbook(encoding='utf8')
table = xlsx_file.add_sheet('data', cell_overwrite_ok=True)
table_head = ['日期', '单号', '件数', '重量/磅', '费用1', '费用2', '费用3', '费用4']
for i in range(len(table_head)):
    table.write(0, i, table_head[i])

# 读取pdf文件内容
with pdfplumber.open(r'D:\python\python小项目\pdf_excel\1348077557.pdf') as pdf:
    total_page = len(pdf.pages)
    for x in range(total_page):
        page = pdf.pages[x]
        text = page.extract_text().split('\n')
        for i in text:
            if 'Export Date/' in i:
                data1 = text[text.index(i)+3].split(' ')
                # 日期
                date = data1[0]
                table.write(x + 1, 0, date)
                # 单号
                num = data1[1]
                table.write(x + 1, 1, num)
                data2 = text[text.index(i)+4].split(' ')
                # 件数
                n = data2[2]
                table.write(x + 1, 2, n)
                # 重量/磅
                lbs = data2[4]
                table.write(x + 1, 3, lbs)
            if 'Description of Charges' in i:
                # 费用
                cost1 = text[text.index(i) + 1].split(' ')[-1]
                table.write(x + 1, 4, cost1)
                cost2 = text[text.index(i) + 3].split(' ')[-1]
                table.write(x + 1, 5, cost2)
                cost3 = text[text.index(i) + 4].split(' ')[-1]
                table.write(x + 1, 6, cost3)

                cost4 = text[text.index(i) + 6].split(' ')[-1]
                table.write(x + 1, 7, cost4)
    xlsx_file.save('data.xls')