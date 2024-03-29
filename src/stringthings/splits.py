# -*-coding: utf-8 -*-
"""
Created on Mon Jan 01 13:53:33 2024

@author: Martín Araya
"""

__all__ = ['multisplit', 'split_dmmmy']


def multisplit(string, sep=[' '], remove=[' ']):
    """
    Receives a string and returns a list with string split by all the separators in sep.
    the default separator is the blank space ' '.
    use the remove parameter to indicate the separators that must not be reported in the output list.
    by default, the blank space is not reported.
    """
    assert type(string) is str

    # check sep is list
    if type(sep) is str:
        sep = [sep]

    # eliminate duplicated separators
    sep = list(set(sep))

    # sort sep by length
    s = len(sep)
    for i in range(s - 1):
        for j in range(s - i - 1):
            if len(sep[j]) < len(sep[j + 1]):
                sep[j], sep[j + 1] = sep[j + 1], sep[j]

    # initialize counters
    string_list = []
    i, x, t = 0, 0, len(string)
    # loop through the entire string
    while i < t:
        found = False  # flag for found separator
        # look for each separator
        for se in sep:
            s = len(se)
            if (i + s <= t) and string[i:i + s] == se:
                string_list += [string[x:i], se]
                x = i + s
                i += s
                found = True
                break
        i += 1 if not found else 0
    string_list += [string[x:]]

    # clean the output
    new_list = []
    for part in string_list:
        if part not in remove + ['']:
            new_list += [part]

    return new_list


def split_dmmmy(string):
    mi, mf = -1, -1
    for x in range(len(string)):
        if not string[x].isdigit() and mf == -1:
            mi = x
        if string[x].isdigit() and mi > -1:
            mf = x + 1
            break
    if mi > 0 and mf > 0:
        return [string[:mi], string[mi:mf], string[mf:]]
