package main

import "fmt"
import "time"
import "math/rand"


func quick_sort(array []int) {
	if len(array) <= 1 {
		return
	}
	sep := partition(array)
	quick_sort(array[:sep])
	quick_sort(array[sep + 1:])
}


func partition(array []int) int {
	length := len(array)
	middle := rand.Intn(length)
	array[middle], array[length - 1] = array[length - 1], array[middle]
	i := -1
	for j := 0; j < length - 1; j ++ {
		if array[j] < array[length - 1] {
			i ++
			array[i], array[j] = array[j], array[i]
		}
	}
	i ++
	array[i], array[length - 1] = array[length - 1], array[i]

	return i
}


func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	test_array := make([]int, 20)
	for i := 0; i < 20; i ++ {
		test_array[i] = rand.Intn(20)
	}
	fmt.Printf("Before sort: ")
	fmt.Println(test_array)
	quick_sort(test_array)
	fmt.Printf("After sort: ")
	fmt.Println(test_array)
}
