package main

import "fmt"
import "time"
import "math/rand"


func max_heapify(array []int, parent int) {
	length := len(array)
	for parent < length {
		largest := parent
		left := parent * 2 +1
		right := left + 1
		if left < length && array[left] > array[largest] {
			largest = left
		}
		if right < length && array[right] > array[largest] {
			largest = right
		}
		if largest != parent {
			array[largest], array[parent] = array[parent], array[largest]
			parent = largest
		} else { break }
	}
}

func build_max_heap(array []int) {
	middle := len(array) / 2 - 1
	for i := middle; i >= 0; i -- {
		max_heapify(array, i)
	}
}

func heap_sort(array []int) {
	build_max_heap(array)
	for i:= len(array) - 1; i > 0; i -- {
		array[0], array[i] = array[i], array[0]
		max_heapify(array[0:i], 0)
	}
}

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	test_array := make([]int, 20)
	for i := 0; i < 20; i ++ {
		test_array[i] = rand.Intn(20)
	}
	fmt.Printf("Before sort: ")
	fmt.Println(test_array)
	heap_sort(test_array)
	fmt.Printf("After sort: ")
	fmt.Println(test_array)
}
