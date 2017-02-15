def merge(left, right):
    array = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1

    array += right[j:]
    array += left[i:]

    return array


def recursive_merge_sort(array):
    length = len(array)
    if length < 2:
        return array
    middle = length / 2
    left = recursive_merge_sort(array[:middle])
    right = recursive_merge_sort(array[middle:])
    return merge(left, right)


def merge_sort(array):
    array[:] = recursive_merge_sort(array)
