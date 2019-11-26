## IO monad task:
 * [IO monad implementation](monad/io.py)
 * [solved task](io_task.py)
 
[Question](https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt#L40):

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a
single line.

This code may produce type cast error when casting user input to
integer number.

Solution without monad:

```python
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


x = int(input())
print(fact(x))
```

## Maybe monad task:
 * [Maybe monad implementation](monad/maybe.py)
 * [solved task](maybe_task.py)

[Question](https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt#L1836):

Please write a binary search function which searches an item in a
sorted list. The function should return the index of element to be
searched in the list.

This code may produce an unexpected behaviour when any parameter
of bin_search function is None.

Solution without monad:
```python
import math


def bin_search(li, element):
    bottom = 0
    top = len(li) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if li[mid] == element:
            index = mid
        elif li[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1
    return index


li = [2, 5, 7, 9, 11, 17, 222]
print(bin_search(li, 11))
print(bin_search(li, 12))
```

## Try monad task:
 * [Try monad implementation](monad/try_.py)
 * [solved task](try_task.py)

Self invented problem =):

Calculate the expression log(number, base) / denominator,
where number, base and denominator is numeric numbers which
is read from console.

This code may produce type cast error, domain error when @num or @base
is not valid for calculating the logarithm and division by zero
error, when @denominator is 0.

Solution without monad:
```python
import math


num = float(input('Input number:'))
base = float(input('Input base:'))
denominator = float(input('Input denominator:'))

print('Result:', (math.log(num, base) / denominator))
```
