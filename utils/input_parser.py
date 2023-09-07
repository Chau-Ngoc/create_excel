import re

from utils import extract_file_content


class Sheet:
    def __init__(self, name, content):
        self.sheet_name = name
        self.content = content


class InputParser:
    SHEET_NAME_SPLIT_PATTERN = re.compile(r"\*{3} [\w.\s-]+ \*{3}")
    SHEET_NAME_PATTERN = re.compile(r"\*{3} (?P<sheet_name>[\w.\s-]+) \*{3}")

    def __init__(self, file):
        self.file_content = extract_file_content(file)
        self.sheets = self.split_into_sheets()

    def get_sheet_names(self):
        return self.SHEET_NAME_PATTERN.findall(self.file_content)

    def split_file_content_by_sheets(self):
        return self.SHEET_NAME_SPLIT_PATTERN.split(self.file_content)[1:]

    def split_into_sheets(self):
        sheet_contents = self.split_file_content_by_sheets()
        sheet_names = self.get_sheet_names()
        return [
            Sheet(name, content)
            for name, content in zip(sheet_names, sheet_contents)
        ]
