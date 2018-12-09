__author__ = 'Administrator'
#导入xlrd
import xlrd
#2.打开exxel(work_book)
excel = xlrd.open_workbook("../data/data.xlsx")
#指定工作表
sheet=excel.sheet_by_name("登录")
sheet=excel.sheet_by_index(0)

print(sheet.nrows)#有效数据行数
print(sheet.ncols)#有效数据列数

print(sheet.row_values(0))#打印第一行
print(sheet.row_values(1))#第二行
print(sheet.cell(1,0).value)#打印单元格数
#关闭
#excel.close

sheet = excel.sheet_by_name('注册')
for i in range(1,sheet.nrows):
    print(sheet.row_values(i))


#(sheet)def read_data