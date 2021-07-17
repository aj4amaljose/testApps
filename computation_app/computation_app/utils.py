"""
Contains general utilities
"""
import pandas as pd


def read_excel(file_path):
    """
    Reads excel and generated dataframes

    :param file_path: File path
    :return: Dataframe mapping
    """
    xl_file = pd.ExcelFile(file_path)
    dfs = {sheet_name: xl_file.parse(sheet_name)
           for sheet_name in xl_file.sheet_names}
    return dfs
