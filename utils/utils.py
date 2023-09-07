from constants import SHEET_CONTENT_PATTERN, SHEET_PATTERN, SHEET_SPLIT_PATTERN


def extract_file_content(file):
    with open(file) as file:
        return file.read()


def join_content_lines(content: str):
    content = content.strip()
    content_lines = " ".join(content.split())
    return content_lines


def input_content_to_dict(content: str):
    sheet_matches = SHEET_PATTERN.finditer(content)
    content_dict = {sheet_match["sheet"]: {} for sheet_match in sheet_matches}
    sheets = SHEET_SPLIT_PATTERN.split(content)[1:]
    sheets_cells = zip(content_dict.keys(), sheets)

    for sheet_cell in sheets_cells:
        sheet_name, sheet_content = sheet_cell
        matches = SHEET_CONTENT_PATTERN.finditer(sheet_content)
        for match in matches:
            cell, content = match.groups()
            content = join_content_lines(content)
            content_dict[sheet_name].update(((cell, content),))

    return content_dict
