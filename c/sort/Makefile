all: test bubble_sort.so insertion_sort.so selection_sort.so merge_sort.so

test: test.o utils.o
	gcc test.o utils.o -ldl -o test

utils.o: utils.c utils.h
	gcc -c utils.c -o utils.o

test.o: test.c utils.h sorts.h
	gcc -c test.c -o test.o

bubble_sort.so: bubble_sort.c sorts.h
	gcc -fPIC --shared bubble_sort.c -o bubble_sort.so

insertion_sort.so: insertion_sort.c sorts.h
	gcc -fPIC --shared insertion_sort.c -o insertion_sort.so

selection_sort.so: selection_sort.c sorts.h
	gcc -fPIC --shared selection_sort.c -o selection_sort.so

merge_sort.so: merge_sort.c sorts.h
	gcc -fPIC --shared merge_sort.c -o merge_sort.so

clean:
	rm -rf test *.so *.o
