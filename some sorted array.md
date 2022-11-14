# practic_python

Университетский курс по Питону. Задачи, которые могут быть полезны на собеседовании


+ [Merge two sorted arrays](#merge-two-sorted-arrays)
+ [Squares of sorted array](#squares-of-sorted-array)

# Arrays

## Squares of sorted array

Возвращение отсортированного массива, состоящего из элементов начального массива, возведенных в квадрат за O(n)

```python

def merge(first, second):
    result = []
    count_el = len(first) + len(second)
    for i in range(count_el):
        if first != [] and second != []:
            if first[0] <= second[0]:
                result.append(first.pop(0))
            else:
                result.append(second.pop(0))
        elif not first:
            result.append(second.pop(0))
        elif not second:
            result.append(first.pop(0))
    return result


def squares(s):
    n = len(s)
    if s[0] >= 0 and s[n-1] >= 0:
        return [el**2 for el in s]
    elif s[0] <= 0 and s[n-1] <= 0:
        return [s[i]**2 for i in range(n-1, -1, -1)]
    else:
        i = 0
        while s[i] <= 0:
            i += 1
        pivot = i
        left = s[:pivot]
        right = s[pivot:]
        left_square = [left[i]**2 for i in range(pivot-1, -1, -1)]
        right_square = [right[i]**2 for i in range(n-pivot)]
        return merge(left_square, right_square)

```

## Merge two sorted arrays

На входе есть два отсортированных массива в неубывающем порядке, объединить эти два массива в один отсортированный в неубывающем порядке

```python 
def merge(left, right):
    len_left = len(left)
    len_right = len(right)
    result = [0] * (len_left + len_right)
    pA = pB = pC = 0

    while pA != len_left and pB != len_right:

        if left[pA] <= right[pB]:
            result[pC] = left[pA]
            pC += 1
            pA += 1
        else:
            result[pC] = right[pB]
            pC += 1
            pB += 1

    while pA != len_left:
        result[pC] = left[pA]
        pC += 1
        pA += 1

    while pB != len_right:
        result[pC] = right[pB]
        pC += 1
        pB += 1

    return 
```

