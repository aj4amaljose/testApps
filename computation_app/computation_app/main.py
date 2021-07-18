"""
Main Module
"""
import os
import logging
from computation_app import utils, operations, validations, errors

logging.basicConfig(level=logging.DEBUG)


VALID_HEADERS = ['x', 'y', 'operation', 'result']


def validate_row_value(columns, row):
    """
    Validates row values

    :param columns: Columns to be validated
    :param row: Row data
    :return: Validation errors
    """
    validation_errors = []
    for column in columns:
        if column in validations.VALIDATION_MAPPING['column'].keys():
            validation_errors += ["Error in column {}: {}".format(column, validation(row[column])) for validation in
                                  validations.VALIDATION_MAPPING['column'][column] if validation(row[column])]
    return validation_errors


def handle_row(row, columns, df, index):
    """
    Handles row

    :param row: Row
    :param columns: columns in the sheet
    :param df: sheet dataframe
    :param index: index of the row
    """
    try:
        validation_errors = validate_row_value(columns, row)
        if any(validation_errors):
            df.loc[index, ['result']] = ''
            df.loc[index, ['error']] = ','.join(validation_errors)
        else:
            value = operations.MAPPINGS[row['operation']](row['x'], row['y'])

            if not isinstance(value, str):
                df.loc[index, ['result']] = value
            else:
                df.loc[index, ['result']] = ''
                df.loc[index, ['error']] = value
    except Exception as er:
        logging.error("Exception in handle_row method: {}".format(er))


def handle_df(df):
    """
    Validates dataframe and process dataframe

    :param df: Dataframe
    :return: Updated Dataframe
    """
    try:
        columns = list(df.columns)
        df['result'] = df['result'].astype(str)

        for index, row in df.iterrows():
            handle_row(row, columns, df, index)
    except Exception as exc:
        logging.error("Error in handle_df method {}".format(exc))
    finally:
        return df


def handle_file(input_file_path, output_folder_path, output_file_name):
    """
    Process file for computation

    :param input_file_path: File path
    :param output_folder_path: Output Folder path
    :param output_file_name: Output Filename
    """
    try:
        if not os.path.isdir(output_folder_path):
            logging.error(errors.INVALID_FOLDER)
            return

        output_file_path = os.path.join(output_folder_path, output_file_name)

        if all(validation(input_file_path) for validation in validations.VALIDATION_MAPPING['file']):
            dfs = utils.read_excel(file_path=input_file_path)

            for item in dfs.items():

                sheet_name, df = item
                logging.debug("Processing sheet {}".format(sheet_name))

                if validations.is_headers_valid(headers=df.columns, valid_headers=VALID_HEADERS):
                    handle_df(df).to_excel(output_file_path,
                                           sheet_name=sheet_name,
                                           index=False)
                else:
                    logging.error("Sheet {} has error: {}".format(sheet_name, errors.MISSING_HEADERS))
        else:
            logging.error(errors.FILE_MISSING)

    except Exception as ex:
        logging.error(ex)


if __name__ == '__main__':
    INPUT_FILE_PATH = r'C:\Copy of Sample Input.xlsx'
    OUTPUT_FOLDER_PATH = r'C:\test'
    OUTPUT_FILE_NAME = 'output.xlsx'
    handle_file(input_file_path=INPUT_FILE_PATH,
                output_folder_path=OUTPUT_FOLDER_PATH,
                output_file_name=OUTPUT_FILE_NAME)
