
def if_else(cond, success, fail):
	def inner():
		return success() if cond else fail()
	return inner


def bs_inner(arr, x, bottom, top):
	mid = (top + bottom) // 2
	return if_else(
		top < bottom,
		lambda: -1,
		if_else(
			arr[mid] == x,
			lambda: mid,
			if_else(
				arr[mid] > x,
				lambda: bs_inner(arr, x, bottom, mid - 1),
				lambda: bs_inner(arr, x, mid + 1, top)
			)
		)
	)()


def bin_search(li, elem):
	return bs_inner(li, elem, 0, len(li) - 1)


if __name__ == '__main__':
	ls = [2, 5, 7, 9, 11, 17, 222]
	print(bin_search(ls, 11))
	print(bin_search(ls, 12))
