import json
import openpyxl

book = openpyxl.Workbook()

sheet = book.active

sheet['A1'] = 100
sheet['B3'] = 'hello'

sheet[1][0].value = 'world'
sheet.cell(row = 1, column = 3).value = 'hello world'

book.save('sheet.xlsx')
book.close()