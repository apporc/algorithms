#include "sorts.h"

void merge(int array[], int start, int middle, int stop) {
    int result[stop - start + 1];
    int i, j, k;
    i = start;
    j = middle + 1;
    k = 0;
    while (i <= middle && j <= stop) {
        if (array[i] < array[j]) result[k++] = array[i++];
        else result[k++] = array[j++];
    }
    while (i <= middle) result[k++] = array[i++];
    while (j <= stop) result[k++] = array[j++];
    int m, n;
    m = 0;
    n = start;
    while (m < (stop - start + 1)) {
        array[n++] = result[m++];
    }
    return;
}

void recursive_merge_sort(int array[], int start, int stop) {
    if (stop == start) return;
    int middle = start + (stop - start) / 2;
    recursive_merge_sort(array, start, middle);
    recursive_merge_sort(array, middle + 1, stop);
    merge(array, start, middle, stop);
    return;
}

void merge_sort(int array[], int length) {
    recursive_merge_sort(array, 0, (length - 1));
    return;
}
