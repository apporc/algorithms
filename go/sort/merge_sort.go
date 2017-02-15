package main

import "fmt"
import "time"
import "math/rand"

func merge(left []int, right []int) []int {
	array := make([]int, 0, len(left) + len(right))
	for len(left) > 0 || len(right) > 0 {
		if len(left) == 0 {
			return append(array, right...)
		}
		if len(right) == 0 {
			return append(array, left...)
		}
		if left[0] < right[0] {
			array = append(array, left[0])
			left = left[1:]
		} else {
			array = append(array, right[0])
			right= right[1:]
		}
	}
	return array
}

func merge_sort(array []int) []int {
	if len(array) < 2 { return array }
	middle := len(array)/2
	left := merge_sort(array[:middle])
	right := merge_sort(array[middle:])
	return merge(left, right)
}

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	test_array := make([]int, 20)
	for i := 0; i < 20; i ++ {
		test_array[i] = rand.Intn(20)
	}
	fmt.Printf("Before sort: ")
	fmt.Println(test_array)
	test_array = merge_sort(test_array)
	fmt.Printf("After sort: ")
	fmt.Println(test_array)
}
