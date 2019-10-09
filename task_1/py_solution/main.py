
def if_else(cond, success, fail):
	def inner():
		return success() if cond() else fail()
	return inner


def bin_search_inner(arr, x, bottom, top):
	mid = (top + bottom) // 2
	return if_else(
		lambda: top < bottom,
		lambda: -1,
		if_else(
			lambda: arr[mid] == x,
			lambda: mid,
			if_else(
				lambda: arr[mid] > x,
				lambda: bin_search_inner(arr, x, bottom, mid - 1),
				lambda: bin_search_inner(arr, x, mid + 1, top)
			)
		)
	)()


def bin_search(arr, elem):
	return bin_search_inner(arr, elem, 0, len(arr) - 1)


if __name__ == '__main__':
	ls = [2, 5, 7, 9, 11, 17, 222]
	print(bin_search(ls, 11))
	print(bin_search(ls, 12))
