#!/usr/bin/env python

"""Dictionary factory using keys and values."""


def dic_with_keys_and_values(hkeys, objvalues):
    """Factory function using keys and values to make dict."""
    if len(hkeys) != len(objvalues):
        print("Keys' and values' length aren't same!")
        return None

    d = dict()
    for i, key in enumerate(hkeys):
        d[key] = objvalues[i]

    return d

alnums = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz0', '123']
print dic_with_keys_and_values(range(10), alnums)
print dic_with_keys_and_values(range(4), alnums)
