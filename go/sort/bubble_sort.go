package main

import "fmt"
import "math/rand"
import "time"

func bubble_sort(slice []int) {
	for i := len(slice) - 1; i > 0; i -- {
		for j := 0; j < i; j ++ {
			if slice[j] > slice[j+1] {
				slice[j], slice[j+1] = slice[j+1], slice[j]
			}
		}
	}
}

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	test_array := make([]int, 20)
	for i := 0; i < 20; i ++ {
		test_array[i] = rand.Intn(20)
	}
	bubble_sort(test_array)
	fmt.Println(test_array)
}
