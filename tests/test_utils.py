from utils import extract_json_content


def test_extract_json_content(resource_dir):
    input_file = resource_dir / "test_input.json"
    expected_dict = {
        "1": ["First name", "Last name", "Gender"],
        "2": ["Ki", "Ka", "Male"],
        "3": ["Fee", "Foe", "Female"],
    }

    json_dict = extract_json_content(input_file)

    assert json_dict == expected_dict
