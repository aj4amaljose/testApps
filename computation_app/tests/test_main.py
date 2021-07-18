import os
import pytest
import pandas as pd
from computation_app import main, utils


def create_excel_file(data, file_name):
    df = pd.DataFrame(data)
    df.to_excel(file_name)


@pytest.mark.parametrize("data, file_name, expected", [

    ({'x': [1, 2, 0], 'y': [3, 6, 7], 'operation': ['addition', 'subtraction', 'multiplication'],
      'result': [None, None, None]}, "test1.xlsx", 3)

])
def test_handle_file(data, file_name, expected):
    output_folder_path = os.path.dirname(os.path.abspath(__file__))
    output_file_name = 'output.xlsx'
    output_file_path = os.path.join(output_folder_path, 'output.xlsx')
    create_excel_file(data, file_name)
    main.handle_file(file_name, output_folder_path, output_file_name)
    dfs = utils.read_excel(output_file_path)
    os.remove(file_name)
    os.remove(output_file_path)
    assert list(dfs["Sheet1"]["result"].values)  == [4,-4, 0]

