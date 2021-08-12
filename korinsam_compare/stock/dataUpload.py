import openpyxl

data = openpyxl.load_workbook('korinsam_data.xlsx')
sheet1 = data.get_sheet_by_name('오픈마켓')
rows = sheet1['B5':'B31']

for row in rows:
    for cell in row:
        print(cell.value)
    

