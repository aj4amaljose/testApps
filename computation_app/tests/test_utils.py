import os
import pytest
import pandas as pd
from computation_app import utils

def create_excel_file(data, file_name):
    df = pd.DataFrame(data)
    df.to_excel(file_name)

@pytest.mark.parametrize("data, file_name, expected", [
    ({}, "test1.xlsx", 0),
    ({'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}, "test2.xlsx", 3)

]
                         )
def test_read_excel(data, file_name, expected):
    create_excel_file(data, file_name)
    dfs = utils.read_excel(file_name)
    os.remove(file_name)
    assert len(dfs['Sheet1'].columns) == expected


