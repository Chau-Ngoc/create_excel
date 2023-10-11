from openpyxl import Workbook

from constants import BASE_DIR
from utils import extract_json_content

input_file = BASE_DIR / "sample" / "input.json"
json_content = extract_json_content(input_file)

workbook = Workbook()
sheet1 = workbook.create_sheet("Sheet 1", -1)

for key in json_content:
    sheet1.append(json_content[key])

workbook.save("example.xlsx")
