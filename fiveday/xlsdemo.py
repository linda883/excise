import xlrd

workbook = xlrd.open_workbook('通用功能测试点.xls')

sheet_names = workbook.sheet_names()

for sheet_name in sheet_names:

    sheet2 = workbook.sheet_by_name(sheet_name)

    print(sheet_name)
    rows = sheet2.row_values(3)  # 获取第四行内容
    cols = sheet2.col_values(1)  # 获取第二列内容
    print(rows)
    print(cols)
