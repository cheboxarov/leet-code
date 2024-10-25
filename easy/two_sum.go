package main

import (
	"fmt"
)

func main() {
	nums := []int{1, 2, 3, 5}
	target := 4
	fmt.Print(twoSum(nums, target))
}

func twoSum(nums []int, target int) []int {
	var set = make(map[int]int)
	for ii, i := range nums {
		buff := target - i
		if val, ok := set[buff]; ok {
			return []int{val, ii}
		}
		set[i] = ii
	}
	return []int{0, 0}
}
