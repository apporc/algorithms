#include "sorts.h"

void bubble_sort(int array[], int length) {
    for (int i = length - 1; i > 0; i --) {
        for (int j  = 0; j < i - 1; j ++) {
            if (array[j] > array[j+1]) {
                array[j] = array[j] ^ array[j+1];
                array[j+1] = array[j] ^ array[j+1];
                array[j] = array[j] ^ array[j+1];
            }
        }
    }
}

