# practic_python1

Университетский курс по Питону. Задачи, которые могут быть полезны на собеседовании


+ [Merge two sorted arrays](#merge-two-sorted-arrays)
+ [Squares of sorted array](#squares-of-sorted-array)
+ [Hello world](#hello-world)
+ [Length of the maximum continuous subsequence](#length-of-the-maximum-continuous-subsequence)
+ [Just add the arrows](#Just-add-the-arrows)
+ [Two sorted arrays](#Two-sorted-arrays)
+ [Nested loops](#nested-loops)
+ [Diagonal Sum](#diagonal-sum)

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

## Hello world

if % 3 == 0 hello; if % 5 == 0 world; if и на 3, и на 5, то helloworld

```python 

def helloWorld(n):
    for item in range(n + 1):
        if item % 3 == 0:
            print('Hello')
        elif item % 5 == 0:
            print('World')
        elif item % 3 == 0 and item % 5 == 0:
            print('HelloWorld')
        else:
            print(item)
```

## Length of the maximum continuous subsequence

list, состоящий из 0 и 1. Найти длину максимальной непрерывной подпоследовательности, состоящей из 1


```python
 def ones(lst):
    k = 0
    max = 0
    for indx in range(len(lst)):
        if lst[indx] == 1:
            k += 1
        else:
            if max < k:
                max = k
            k = 0
    print(max)
```    
   
   
## Just add the arrows

Вход: nums = [0,1,2,4,5,7]

[0, 1, 2], [4, 5], [7]

Выход: ["0->2","4->5","7"]

```python
def find_sum(arr):
    middle = []
    if len(arr) == 0:
        return middle
    left = arr[0]
    right = arr[0]
    for idx in range(1, len(arr)):
        if arr[i] - 1 != arr[i-1]:
            if left == right:
                middle.append(str(left))
            else:
                middle.append(str(left) + '->' + str(right))
            left = right = arr[i]
        right = arr[i]
    if left == right:
        middle.append(str(left))
    else:
        middle.append(str(left) + '->' + str(right))
    return middle
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

# Matrix

## Diagonal Sum

Найти сумму диагональных элементов

```python
def sum_diag(matrix):
       summ = 0
       for i in range(len(matrix)):
              for j in range(len(matrix)):
                     if i == j or i + j + 1 == len(matrix):
                            summ += matrix[i][j]

       print(summ)

print(sum_diag(mat))
```

## Two sorted arrays

На входе два отсортированных массива (списка), на выходе получить 1 отсортированный массив. Элементы списка это целые числа за o(n)

```python
def merge(first, second):
    f_arr = []
    l1 = 0
    l2 = 0
    while (l1 < len(first)) and (l2 < len(second)):
        if first[l1] < second[l2]:
            f_arr.append(first[l1])
            l1 += 1
        else:
            f_arr.append(second[l2])
            l2 += 1
    if l2 < len(second):
        while l2 < len(second):
            f_arr.append(second[l2])
            l2 += 1
    else:
        while l2 < len(first):
            f_arr.append(first[l1])
            l1 += 1
    return f_arr
```

## Nested loops

in:

chrs = ["a","b","b","c","c","c"]

chrs2 = ["d","a","b","c"]

chrs2 = ["c","c","c"]

out:

"ab2c3"

"dabc"

"c3"

```python
ans = dict()
ans_l = list()
for i in l:
    if i in ans.keys():
        ans[i] += 1
    else:
        ans[i] = 1
for k, v in ans.items():
    ans_l.extend([k, str(v)])

print(''.join(ans_l))
```
