def selection_sort(array):
    for i in xrange(0, len(array)):
        smallest = i
        j = i + 1
        while j < len(array):
            if array[j] < array[smallest]:
                smallest = j
            j += 1
        if smallest != i:
            array[i], array[smallest] = array[smallest], array[i]
