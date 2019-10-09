package main

func ifElse(cond bool, success func() interface{}, fail func() interface{}) func() interface{} {
	return func() interface{} {
		if cond {
			return success()
		}
		return fail()
	}
}

func binSearchInner(arr []int, x int, bottom int, top int) int {
	mid := (top + bottom) / 2
	return ifElse(
		top < bottom,
		func() interface{} {
			return -1
		},
		ifElse(
			arr[mid] == x,
			func() interface{} {
				return mid
			},
			ifElse(
				arr[mid] > x,
				func() interface{} {
					return binSearchInner(arr, x, bottom, mid - 1)
				},
				func() interface{} {
					return binSearchInner(arr, x, mid + 1, top)
				},
			),
		),
	)().(int)
}

func binSearch(arr []int, x int) int {
	return binSearchInner(arr, x, 0, len(arr) - 1)
}

func main() {
	arr := []int {2, 5, 7, 9, 11, 17, 222}
	println(binSearch(arr, 11))
	println(binSearch(arr, 12))
}
