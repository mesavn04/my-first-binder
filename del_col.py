import xlwings as xw 
wb = xw.Book('new_big_file.xlsx')
#wb = xw.Book('c:\\users\\zhong\\downloads\\test.xlsx')
sht = wb.sheets[0]
sht.range('A:A').api.Delete()