package main

import "fmt"
import "time"
import "math/rand"

func selection_sort(array []int) {
	for i:= 0; i < len(array); i ++ {
		smallest := i
		for j:= i + 1; j < len(array); j ++ {
			if array[j] < array[smallest] { smallest = j }
		}
		if smallest != i {
			array[smallest], array[i] = array[i], array[smallest]
		}
	}
}

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	test_array := make([]int, 20)
	for i := 0; i < len(test_array); i ++ {
		test_array[i] = rand.Intn(20)
	}
	selection_sort(test_array)
	fmt.Println(test_array)
}
