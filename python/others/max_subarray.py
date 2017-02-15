#!/bin/env python
import random
import sys


def max_subarray_old(array):
    # A fixed solution from myself. O(n)
    max_sum_result = (0, 0, 0)
    temp_sum_result = (0, 0, 0)
    for i in xrange(0, len(array)):
        if array[i] > 0:
            if temp_sum_result[0] > 0:
                temp_sum_result = (
                    temp_sum_result[0] + array[i], temp_sum_result[1], i)
            else:
                temp_sum_result = (array[i], i, i)
            if temp_sum_result[0] > max_sum_result[0]:
                max_sum_result = temp_sum_result
        else:
            temp_sum_result = (temp_sum_result[0] + array[i],
                               temp_sum_result[1], i)
    return max_sum_result


def on_max_subarray(array):
    # time complexity O(n)
    max_sum_result = (0, 0, 0)
    temp_sum_result = (0, 0, 0)
    for i in xrange(0, len(array)):
        if temp_sum_result[0] == 0:
            temp_sum_result = (array[i], i, i)
        else:
            # temp_sum_result can't be less then zero.
            temp_sum_result = (temp_sum_result[0] + array[i],
                               temp_sum_result[1], i)

        if temp_sum_result[0] < 0:
            temp_sum_result = (0, 0, 0)
        elif temp_sum_result[0] > max_sum_result[0]:
            max_sum_result = temp_sum_result
        else:
            # if 0 < temp_sum_result < max_sum_result, keep it.
            temp_sum_result = temp_sum_result

    return max_sum_result


def force_max_subarray(array):
    # brute force
    max_sum_result = [0, 0, 0]
    for i in xrange(1, len(array) + 1):
        for j in xrange(0, len(array) - i + 1):
            temp_sum_result = [0, j, j + i - 1]
            for k in xrange(j, j + i):
                temp_sum_result[0] = temp_sum_result[0] + array[k]
            if temp_sum_result[0] > max_sum_result[0]:
                max_sum_result = temp_sum_result

    return max_sum_result


def merge_max_subarray(array):
    return recursive_merge_max_subarray(array, 0, len(array) - 1)


def recursive_merge_max_subarray(array, start, stop):

    def get_cross_max_subarray(array, start, middle, stop):

        def max_subarray_with_boundary(array,
                                       start=None,
                                       boundary=None,
                                       stop=None):
            max_sum_result = (-sys.maxint - 1, None, None)

            if start is None:
                temp_sum_result = (0, boundary, 0)
                for i in xrange(boundary, stop + 1):
                    temp_sum_result = (temp_sum_result[0] + array[i],
                                       temp_sum_result[1],
                                       i)
                    if temp_sum_result[0] > max_sum_result[0]:
                        max_sum_result = temp_sum_result
                return max_sum_result

            elif stop is None:
                temp_sum_result = (0, 0, boundary)
                for i in reversed(xrange(start, boundary + 1)):
                    temp_sum_result = (temp_sum_result[0] + array[i],
                                       i,
                                       temp_sum_result[2])
                    if temp_sum_result[0] > max_sum_result[0]:
                        max_sum_result = temp_sum_result
                return max_sum_result

        left = max_subarray_with_boundary(array, start=start, boundary=middle)
        right = max_subarray_with_boundary(array, boundary=middle + 1,
                                           stop=stop)
        return (left[0] + right[0],
                left[1],
                right[2])

    if start == stop:
        return (array[start], start, start)
    middle = (start + stop) / 2
    left_max_subarray = recursive_merge_max_subarray(array, start, middle)
    right_max_subarray = recursive_merge_max_subarray(array, middle + 1, stop)
    cross_max_subarray = get_cross_max_subarray(array, start, middle, stop)
    return max(left_max_subarray, right_max_subarray, cross_max_subarray,
               key=lambda x: x[0])


def maxSubArray(nums):
    if nums is None or len(nums) == 0:
        return 0
    maxSum = nums[0]
    minSum = 0
    sum = 0
    for num in nums:
        sum += num
        if sum - minSum > maxSum:
            maxSum = sum - minSum
        if sum < minSum:
            minSum = sum
    return maxSum


test_array = []
for i in xrange(0, 50):
    test_array.append(random.randint(-25, 25))

print("test_array: %r" % test_array)
print("Max-Subarray-Old: sum -> %s, start -> %s, stop -> %s"
      % max_subarray_old(test_array))
print("On-Max-Subarray: sum -> %s, start -> %s, stop -> %s"
      % on_max_subarray(test_array))
print("Force-Max-Subarray: sum -> %s, start -> %s, stop -> %s"
      % tuple(force_max_subarray(test_array)))
print("Merge-Max-Subarray: sum -> %s, start -> %s, stop -> %s"
      % merge_max_subarray(test_array))
print("Max-Subarray-Old: sum -> %s"
      % maxSubArray(test_array))
