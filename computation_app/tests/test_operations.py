import pytest
from computation_app.computation_app import operations


@pytest.mark.parametrize("value_1, value_2, operation, expected",
                         [
                             (1, 3, 'addition', 4),
                             (1.0, -3.1, 'addition', -2.1),
                             (0, -3.1, 'addition', -3.1),
                             (0, 0, 'addition', 0),
                             (0, 0, 'subtraction', 0),
                             (5, 8, 'subtraction', -3),
                             (5, 8, 'multiplication', 40),
                             (5, -8.1, 'multiplication', -40.5),
                             (-5, -8, 'multiplication', 40),
                             (0, 0, 'multiplication', 0),
                             (0, 0, 'exponentiation', 1),
                             (2, 8, 'exponentiation', 256),
                             (2, -1.0, 'exponentiation', .5),
                             (2, -1.5, 'exponentiation', 0.3535533905932738),
                             (-1.2, 0, 'exponentiation', 1),
                             (-1.2, 0, 'division', "Division by zero is not allowed"),
                             (-1.2, 1, 'division', -1.2)
                         ])
def test_cleanse_data(value_1, value_2, operation, expected):
    assert expected == operations.MAPPINGS[operation](value_1, value_2)
