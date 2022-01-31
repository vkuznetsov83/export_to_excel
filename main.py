import openpyxl
import datetime



wb = openpyxl.Workbook()

ws = wb.active
ws.title = "Price List"

# Header

img = openpyxl.drawing.image.Image('metrix.png')
img.anchor = ('A1:A3')

ws['G2'] = 'PRICE LIST'

ws['A5'] = 'Company name'
ws['A6'] = 'house_street'
ws['A7'] = 'city_zip'

ws['C5'] = 'Phone'
ws['C6'] = 'E-mail'
ws['C7'] = 'Website'

ws['G5'] = 'Valid from'
ws['G6'] = datetime.date.today()



# Spreadsheet

ws.merge_cells('A9:A10')
ws.merge_cells('B9:B10')
ws.merge_cells('C9:C10')
ws.merge_cells('D9:D10')
ws.merge_cells('E9:E10')
ws.merge_cells('F9:F10')
ws.merge_cells('G9:G10')






wb.save(filename='Price_list.xlsx')