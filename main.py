from openpyxl import Workbook

workbook = Workbook()
sheet1 = workbook.create_sheet("Sheet 1", -1)
workbook.save("example.xlsx")
