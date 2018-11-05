import xlrd

loc = ("20_10.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)


list =sheet.row_values(1)

print(list[0])
