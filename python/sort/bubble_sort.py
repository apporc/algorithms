def bubble_sort1(array):
    if not isinstance(array, list):
        return False
    for i in reversed(xrange(1, len(array))):
        for j in xrange(0, i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def bubble_sort(array):
    if not isinstance(array, list):
        return False
    i = len(array) - 1
    while i > 0:
        for j in xrange(0, i):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]
        i -= 1
