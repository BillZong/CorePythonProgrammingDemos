#!/usr/bin/env python

"""Answer for 11.7 in chapter 11."""


def two_list_to_tuple_list(list1, list2, mapper=map):
    """Using mapper function to 'zip' two lists into one."""
    if len(list1) != len(list2):
        return None
    else:
        if mapper == map:
            return mapper(None, list1, list2)
        else:
            return mapper(list1, list2)

print two_list_to_tuple_list([1, 2, 3], ['abc', 'def', 'ghi'])
print two_list_to_tuple_list([1, 2, 3], ['abc', 'def', 'ghi'], zip)
print ''


# def my_zip(list1, list2):
#     """My implemetation of zip function."""
#     return [(list1[i], list2[i]) for i in range(len(list1))]

# print two_list_to_tuple_list([1, 2, 3], ['abc', 'def', 'ghi'], my_zip)

connect = two_list_to_tuple_list
print connect([1, 2, 3], ['abc', 'def', 'ghi'],
              lambda list1, list2: [(list1[i], list2[i])
                                    for i in range(len(list1))])
