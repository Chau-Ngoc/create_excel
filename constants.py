import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

FILENAME_PATTERN = re.compile(r"File name: (?P<filename>[\w.-]+)")
SHEET_PATTERN = re.compile(r"\*{3} (?P<sheet>[\w.\s-]+) \*{3}")
CELL_PATTERN = re.compile(r"(?!\n)\s{4,}\[Cell] (?P<cell>\w+)")
CONTENT_PATTERN = re.compile(r"^(?P<content>(?:\s{4,}(?:\w+ *)+)+)")

SHEET_SPLIT_PATTERN = re.compile(r"\*{3} [\w.\s-]+ \*{3}")

SHEET_CONTENT_PATTERN = re.compile(
    r"\s{4,}\[Cell] (?P<cell>\w+)\n(?P<content>(?:\s{4,}[ \w.,+*/-]+\n*)+)"
)
