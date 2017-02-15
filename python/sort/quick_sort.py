import random


def quick_sort(array):
    if len(array) <= 1:
        return array
    middle = partition(array)
    left = quick_sort(array[0:middle])
    right = quick_sort(array[middle + 1:len(array)])
    array[:] = left + [array[middle]] + right
    return array


def partition(array):
    i = -1
    choose_middle(array)
    for j in xrange(len(array) - 1):
        if array[j] < array[len(array) - 1]:
            i += 1
            array[i], array[j] = array[j], array[i]
    i += 1
    array[len(array) - 1], array[i] = array[i], array[len(array) - 1]
    return i


def choose_middle(array):
    middle = random.randint(0, len(array) - 1)
    array[middle], array[len(array) - 1] = array[len(array) - 1], array[middle]
