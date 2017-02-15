def counting_sort(array):
    temp_array = array[:]
    array_max = max(array)
    array_min = min(array)
    bucket_length = array_max - array_min + 1
    bucket = [0] * bucket_length
    for i in array:
        bucket[i - array_min] += 1
    for j in xrange(1, bucket_length):
        bucket[j] = bucket[j] + bucket[j - 1]
    for i in reversed(temp_array):
        array[bucket[i - array_min] - 1] = i
        bucket[i - array_min] -= 1
