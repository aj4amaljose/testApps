"""
Contains validation for the input data.
Use decorator for mapping set_for to map validations against the columns/Files.
"""
import os.path
from .operations import MAPPINGS
from collections import defaultdict

from .errors import INVALID_DATATYPE, INVALID_OPERATOR, NULL_ERROR

VALIDATION_MAPPING = defaultdict(dict)


def update_mapping(mapping, val, func):
    """
    Update Mapping with functions

    :param mapping: Mapping
    :param val: val
    :param func: Function
    """
    if val in mapping.keys():
        mapping[val].append(func)
    else:
        mapping[val] = [func]


def set_for(validation_type, values=None):
    """
    Creates a mapping for validations
    """

    def wrapper(func):

        if isinstance(values, list):
            for val in values:
                update_mapping(VALIDATION_MAPPING[validation_type], val, func)
        elif values:
            update_mapping(VALIDATION_MAPPING[validation_type], values, func)
        else:
            update_mapping(VALIDATION_MAPPING, validation_type, func)

        return func

    return wrapper


@set_for(validation_type='file')
def is_file_exists(file_path):
    """
    Check the file exists in the provided path

    :param file_path: Full file path
    :return: Bool
    """
    return os.path.isfile(file_path)


@set_for(validation_type='file')
def is_file_excel(file_path):
    return file_path.endswith('xlsx')


def is_headers_valid(headers, valid_headers):
    """
    Checks whether the sheet has all the valid headers

    :param headers: Headers in the sheet
    :param valid_headers: Valid headers
    :return: Validation result
    """
    check = 0
    for header in valid_headers:
        if header in headers:
            check += 1
    return check == len(valid_headers)


@set_for(validation_type='column', values=['x', 'y'])
def is_input_invalid(value):
    """
    Check if the data is invalid for math operations

    :param value: Input Value
    :return: Validation result
    """
    if isinstance(value, int) or isinstance(value, float):
        return False
    elif not value:
        return NULL_ERROR
    else:
        return INVALID_DATATYPE


@set_for(validation_type='column', values='operation')
def is_operation_name_invalid(value):
    """
    Validates operation value in the input file.

    :param value: Value
    :return: Validation result
    """
    if value in MAPPINGS.keys():
        return False
    elif not value:
        return NULL_ERROR
    else:
        return INVALID_OPERATOR
