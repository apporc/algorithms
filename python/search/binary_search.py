#!/bin/env python


def binary_search(array, item):
    if len(array) == 1 and array[0] != item:
        return False
    middle = len(array)/2
    if array[middle] == item:
        return middle
    elif array[middle] < item:
        return middle + binary_search(array[(middle+1):], item) + 1
    elif array[middle] > item:
        return binary_search(array[:middle], item)

test_array = range(0, 10)
print binary_search(test_array, 5)
