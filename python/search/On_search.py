#!/bin/env python
import math
from random import randrange


def On_search(array, k):
    return recursive_on_search(array, k)


def recursive_on_search(array, k):
    median = partition(array)
    if median + 1 == k:
        return array[median]
    elif median + 1 > k:
        return recursive_on_search(array[:median], k)
    else:
        return recursive_on_search(array[median + 1:], k - median - 1)


def partition(array):
    median = choose_median(array)
    array[-1], array[median] = array[median], array[-1]
    mark = -1
    for i in range(0, len(array) - 1):
        if array[i] < array[-1]:
            mark += 1
            array[mark], array[i] = array[i], array[mark]
    array[mark + 1], array[-1] = array[-1], array[mark + 1]
    return median


def choose_median(array):
    if len(array) < 2:
        return len(array) / 2
    bucket_length = int(math.ceil(len(array) / 5.0))
    buckets = [[] for i in range(0, bucket_length)]
    for i in range(0, len(array)):
        buckets[i / 5].append(array[i])
    map(lambda x: x.sort(), buckets)
    buckets.sort(key=lambda x: x[len(x) / 2])
    median = bucket_length / 2
    array[:] = reduce(lambda x, y: x + y, buckets)
    return median * 5 + len(buckets[median]) / 2 - 1


test_array = [randrange(0, 100) for x in xrange(0, 20)]
print(test_array)
test_array.sort()
print(test_array)
print On_search(test_array, 10)
