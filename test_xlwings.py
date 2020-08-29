import xlwings as xw
wb = xw.Book()
sheet = wb.sheets['Sheet1']
sheet.range('A1').value = "Hello Excel from Python"
sheet.range((3,2)).value = 'x-axis'
sheet.range((3,3)).value = 'y-axis'
for i in range(5):
    sheet.range((i+4, 2)).value = i
for i in range(5):
    sheet.range((i+4,3)).value = f'=exp(B{i+4})'
data = sheet.range('B3:C8').value
import pandas as pd
df = xw.Range('B3').expand().options(pd.DataFrame).value
df.reset_index(inplace=True)
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(df['x-axis'],df['y-axis'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
sheet.pictures.add(fig, name='MyPlot', update=True)   #add the graph back into Excel
wb.save('automate_excel_with_python.xlsx')
wb.close()
