package main

import "fmt"
import "time"
import "math/rand"

func max(array []int) int {
	max := array[0]
	for i := 1; i < len(array); i ++ {
		if array[i] > max {
			max = array[i]
		}
	}
	return max
}

func min(array []int) int {
	min := array[0]
	for i := 1; i < len(array); i ++ {
		if array[i] < min {
			min = array[i]
		}
	}
	return min
}

func counting_sort(array []int) {
	array_max, array_min := max(array), min(array)
	bucket_length := array_max - array_min + 1
	bucket := make([]int, bucket_length)
	for i := 0; i < len(array); i ++ {
		bucket[array[i] - array_min] += 1
	}
	for i := 1; i < bucket_length; i ++ {
		bucket[i] = bucket[i] + bucket[i - 1]
	}
	temp_array := make([]int, len(array))
	for i := len(array) - 1; i >= 0; i -- {
		temp_array[bucket[array[i] - array_min] - 1] = array[i]
		bucket[array[i] - array_min] -= 1
	}
	copy(array, temp_array)
}


func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	test_array := make([]int, 20)
	for i := 0; i < 20; i ++ {
		test_array[i] = rand.Intn(100) - 50
	}
	fmt.Printf("Before sort: ")
	fmt.Println(test_array)
	counting_sort(test_array)
	fmt.Printf("After sort: ")
	fmt.Println(test_array)
}
