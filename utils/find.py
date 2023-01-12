from utils.common import file_operations
# can also do from .common.file_operations import save_to_file which means from current module


def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i

    raise NotFoundError(f'{expected} not found in provided iterable.')


class NotFoundError(Exception):
    pass

