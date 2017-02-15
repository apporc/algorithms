#include "utils.h"
#include "sorts.h"
#include <stdio.h>
#include <dlfcn.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX_FILENAME 100

int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Usage: ./test <sort name>\n");
        exit(1);
    }
    srandom(time(NULL));
    int test_array[20];
    for (int i = 0; i < 20; i ++) {
        test_array[i] = random() % 20;
    }
    int length = sizeof(test_array)/sizeof(int);

    char library_file[MAX_FILENAME];
    char func_name[MAX_FILENAME];
    snprintf(library_file, MAX_FILENAME, "./%s_sort.so", argv[1]);
    snprintf(func_name, MAX_FILENAME, "%s_sort", argv[1]);

    // Loading sorting library
    void *handle = NULL;
    void (*sort_func)(int*, int);
    char *error;
    handle = dlopen(library_file, RTLD_LAZY);
    if (!handle) {
        fputs (dlerror(), stderr);
        exit(1);
    }

    sort_func = dlsym(handle, func_name);
    if ((error = dlerror()) != NULL)  {
        fputs(error, stderr);
        exit(1);
    }
    (*sort_func)(test_array, length);
    print_array(test_array, length);
    dlclose(handle);
}
