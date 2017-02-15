import math


def radix_sort(array):
    buckets = [[] for i in range(10)]
    radix = int(math.ceil(math.log10(max(array))))
    for i in range(radix):
        higher = pow(10, i + 1)
        lower = pow(10, i)
        for j in array:
            buckets[j / lower - (j / higher) * higher].append(j)
        del array[:]
        for bucket in buckets:
            array += bucket
            del bucket[:]
