import xlwings as xw

wb = xw.Book('test_xlwings.xlsx')  # Open an existing Workbook
sheet = wb.sheets['Sheet']

# read and write values from the worksheet
sheet.range('A1').value = 'Foo'
print(sheet.range('A1').value)

# Write a Pandas DataFrames directly to the Excel sheet
import pandas as pd
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])

sheet.range('A1').value = df

# Read the DataFrame back, using the 'expand' option to read the whole table
sheet.range('A1').options(pd.DataFrame, expand='table').value