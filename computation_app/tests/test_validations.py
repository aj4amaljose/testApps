import os
import pytest
from computation_app.errors import INVALID_DATATYPE, INVALID_OPERATOR
from computation_app import validations

@pytest.mark.parametrize("value, expected", [
    (1, False),
    (-1.5, False),
    (0, False),
    ("test1", INVALID_DATATYPE),
    (0, False)
]
                         )
def test_is_input_invalid(value, expected):
    assert expected == validations.is_input_invalid(value)


@pytest.mark.parametrize("value, expected", [
    ("addition", False),
    (-1.5, INVALID_OPERATOR),
    ("log", INVALID_OPERATOR),
]
                         )
def test_is_operation_name_invalid(value, expected):
    assert expected == validations.is_operation_name_invalid(value)


@pytest.mark.parametrize("file_path, expected", [
    (r"c:/test.xlsx", True),
    (r"c:/test.py", False),
]
                         )
def test_is_file_excel(file_path, expected):
    assert expected == validations.is_file_excel(file_path)


@pytest.mark.parametrize("file_path, expected", [
    (os.path.abspath(__file__), True),
    (r"c:/test85485/test.py", False),
]
                         )
def test_is_file_exists(file_path, expected):
    assert expected == validations.is_file_exists(file_path)