import math


def bin_search(li, elem):
	return bin_search_inner(li, elem, len(li) - 1, 0, -1)


def bin_search_inner(li, elem, top, bottom, index):
	mid = int(math.floor((top + bottom) / 2.0))
	if li[mid] == elem:
		index = mid
	elif li[mid] > elem:
		top = mid - 1
	else:
		bottom = mid + 1
	if top >= bottom and index == -1:
		return bin_search_inner(li, elem, top, bottom, index)
	return index


if __name__ == '__main__':
	ls = [1, 2, 2, 2, 2, 3, 3, 4, 5, 66, 8789]
	print(bin_search(ls, 3))
