package main

import "fmt"
import "math/rand"
import "time"

func insertion_sort(slice []int) {
	for i := 1; i < len(slice); i ++ {
		j := i - 1
		for j >= 0 && slice[j] > slice[j+1] {
			slice[j], slice[j+1] = slice[j+1], slice[j]
			j -= 1
		}
	}
}

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	test_array := make([]int, 20)
	for i := 0; i < 20; i ++ {
		test_array[i] = rand.Intn(20)
	}
	insertion_sort(test_array)
	fmt.Println(test_array)
}
