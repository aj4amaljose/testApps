"""
Module contains operations to be carried against the operations field in the output.
Use decorator set_operation to map the function to the operation value
"""
from .errors import DIVISION_ERROR

MAPPINGS = dict()


def set_operation(operation):
    """
    Creates mapping for the operations to be carried out

    :param operation: Operation to be carried out
    :return: Function
    """
    def wrapper(func):
        """
        Maps operation name to the Function

        :param func: Function
        :return: Mapping
        """
        if isinstance(operation, list):
            [MAPPINGS.update({op: func}) for op in operation]
        else:
            MAPPINGS[operation] = func
        return func
    return wrapper


@set_operation('division')
def division(value_1, value_2):
    """
    Divides value 1 by value 2

    :param value_1: Value 1
    :param value_2: value 2
    :return: Result
    """
    if value_2 == 0:
        return DIVISION_ERROR

    return value_1 / value_2


@set_operation(['addition', 'add'])
def addition(value_1, value_2):
    """
    Adds input numbers

    :param value_1: Value 1
    :param value_2: Value 2
    :return: Result
    """
    return value_1 + value_2


@set_operation('multiplication')
def multiplication(value_1, value_2):
    """
    Multiplies two input numbers

    :param value_1: Value 1
    :param value_2: Value 2
    :return: Result
    """
    return value_1 * value_2


@set_operation('exponentiation')
def exponentiation(value_1, value_2):
    """
    Provides Exponential value

    :param value_1: Value 1
    :param value_2: value 2
    :return: Result
    """
    return value_1 ** value_2


@set_operation(['subtraction', 'subtract'])
def subtraction(value_1, value_2):
    """
    Finds difference between two given numbers
    :param value_1: Value 1
    :param value_2: Value 2
    :return: Results
    """
    return value_1 - value_2

