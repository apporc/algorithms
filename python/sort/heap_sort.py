def max_heapify(array, parent, length):
    while parent < length:
        largest = parent
        left = parent * 2 + 1
        right = left + 1
        if left < length and array[left] > array[largest]:
            largest = left
        if right < length and array[right] > array[largest]:
            largest = right
        if largest != parent:
            array[parent], array[largest] = array[largest], array[parent]
            parent = largest
        else:
            break


def build_max_heap(array):
    middle = len(array) / 2 - 1
    for i in reversed(xrange(0, middle + 1)):
        max_heapify(array, i, len(array))


def heap_sort(array):
    build_max_heap(array)
    for i in reversed(xrange(0, len(array))):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, 0, i)
