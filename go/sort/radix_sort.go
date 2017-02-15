package main

import "fmt"
import "time"
import "math"
import "math/rand"

const MAX_BUCKET_SIZE = 100

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

func radix_sort(array []int) []int {
	buckets := make([][]int, 10)
	for i := 0; i < 10; i ++ {
		buckets[i] = make([]int, 0, MAX_BUCKET_SIZE)
	}
	radix := int(math.Ceil(math.Log10(float64(max(array)))))
	for i := 0; i < radix; i ++ {
		for j := 0; j < len(array); j ++ {
			upper := array[j] / int(math.Pow10(i))
			lower := array[j] / int(math.Pow10(i + 1)) * int(math.Pow10(i + 1))
			loc := upper - lower
			buckets[loc] = append(buckets[loc], array[j])
		}
		array = array[:0]
		for j := 0; j < 10; j ++ {
			fmt.Println("buckets=", buckets[j])
			for k := 0; k < len(buckets[j]); k ++ {
				array = append(array, buckets[j][k])
			}
			buckets[j] = buckets[j][:0]
		}
	}
	return array
}


func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	test_array := make([]int, 20)
	for i := 0; i < 20; i ++ {
		test_array[i] = rand.Intn(100)
	}
	fmt.Printf("Before sort: ")
	fmt.Println(test_array)
	test_array = radix_sort(test_array)
	fmt.Printf("After sort: ")
	fmt.Println(test_array)
}
