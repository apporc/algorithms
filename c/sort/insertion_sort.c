#include "sorts.h"

void insertion_sort(int *array, int length) {
    for (int i = 0; i < length; i ++) {
        int j = i - 1;
        while ( j >= 0 && array[j] > array[j+1]) {
            array[j] = array[j] ^ array[j+1];
            array[j+1] = array[j] ^ array[j+1];
            array[j] = array[j] ^ array[j+1];
            j --;
        }
    }
}
