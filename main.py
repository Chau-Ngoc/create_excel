from openpyxl import Workbook

from constants import BASE_DIR
from utils import extract_file_content, input_content_to_dict

input_file = BASE_DIR / "sample" / "input.txt"

file_content = extract_file_content(input_file)
content_dict = input_content_to_dict(file_content)

workbook = Workbook()
sheet1 = workbook.create_sheet("Sheet 1", -1)
workbook.save("example.xlsx")
