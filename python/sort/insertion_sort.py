def insertion_sort(array):
    if not isinstance(array, list):
        return False
    for i in xrange(1, len(array)):
        j = i - 1
        while j >= 0 and array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j = j - 1
