import openpyxl

wb = openpyxl.Workbook()

ws = wb.active
ws.title = "Price List"

# Header

ws['G2'] = 'PRICE LIST'

ws['A5'] = 'Company name'
ws['A6'] = 'house_street'
ws['A7'] = 'city_zip'

ws['C5'] = 'Phone'
ws['C6'] = 'E-mail'
ws['C7'] = 'Website'

ws['F5'] = 'Valid from'
ws['F6'] = 'Valid to'






wb.save(filename='Price_list.xlsx')