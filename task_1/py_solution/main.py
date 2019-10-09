
def bin_search(li, elem):
	return binary_search_inner(li, elem, 0, len(li) - 1)


def binary_search_inner(arr, x, bottom, top):
	if top < bottom:
		return -1
	mid = int(bottom + (top - bottom) / 2)
	if arr[mid] == x:
		return mid
	elif arr[mid] > x:
		return binary_search_inner(arr, x, bottom, mid - 1)
	else:
		return binary_search_inner(arr, x, mid + 1, top)


if __name__ == '__main__':
	ls = [2, 5, 7, 9, 11, 17, 222]
	print(bin_search(ls, 11))
	print(bin_search(ls, 12))
