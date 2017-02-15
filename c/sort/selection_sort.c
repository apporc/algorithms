#include "sorts.h"

void selection_sort(int array[], int length) {
    for (int i = 0; i < length; i ++ ) {
        int smallest = i;
        for (int j = i + 1; j < length; j ++ ) {
            if (array[j] < array[smallest] ) smallest = j;
        }
        if (smallest != i) {
            array[i] = array[i] ^ array[smallest];
            array[smallest] = array[i] ^ array[smallest];
            array[i] = array[i] ^ array[smallest];
        }
    }
}
