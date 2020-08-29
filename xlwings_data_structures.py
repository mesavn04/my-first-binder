import xlwings as xw
#Single Cells
import datetime as dt
sht = xw.Book().sheets[0] #create new workbook
sht.range('F1').value = 1
sht.range('F2').value = 'Hello'
sht.range('F3').value is None
sht.range('F4').value = dt.datetime(2000, 1, 1)
sht.range('F4').value
#1d lists
sht.range('A1').value = [[1],[2],[3],[4],[5]]  # Column orientation (nested list)
sht.range('A1:A5').value
sht.range('A1').value = [1, 2, 3, 4, 5]
sht.range('A1:E1').value
#To force a single cell to arrive as list
#sht.range('A11').options(ndim=1).value= [[1],[2],[3],[4],[5]]
#To write a list in column orientation to Excel, use transpose
#sht.range('G1').options(transpose=True).value = [1,2,3,4]
#2d lists
sht.range('A11:A15').options(ndim=2).value=[[1],[2],[3],[4],[5]]
sht.range('A11:E11').options(ndim=2).value=[[1],[2],[3],[4],[5]]
