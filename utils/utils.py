import json
import os
from typing import Union


def extract_json_content(json_file: Union[str, os.PathLike]):
    with open(json_file, "r") as file:
        return json.load(file)
