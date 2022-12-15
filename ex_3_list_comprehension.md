# practic_python1

Университетский курс по Питону. Задачи, которые могут быть полезны на собеседовании


+ [1](#1)
+ [2](#2)
+ [3](#3)
+ [4](#4)
+ [5](#5)
+ [6](#6)
+ [7](#7)
+ [8](#8)
+ [9](#9)
+ [10](#10)
+ [11](#11)
+ [12](#12)
+ [13](#13)
+ [14](#14)
+ [15](#15)
+ [16](#16)

## Import

Используемые библиотеки

```python

import json
import math
import re
import numpy as np

```

## 1

Найти все числа от 1 до 1000, которые делятся на 17

```python


print([i for i in (range(1, 1001)) if i%17==0]) #1

```
## 2

Найти все числа от 1 до 1000, которые содержат в себе цифру 2

```python
print([i for i in list(range(1, 1001)) if (str(i)).find("2") != -1]) #2

```

## 3

Найти все числа от 1 до 10000, которые являются палиндромом	

```python
print([i for i in range(10, 1001) if str(i) == (str(i))[::-1]]) #3
```

## 4

Посчитать количество пробелов в строке

```python
some_text = ('sa  dFa  sSfs Adfa sd')
print(some_text.count(' ')) #4
```
## 5

Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова

```python
some_text1 = ('asdsfasdyuoiA')
print(re.sub('[A|a|E|e|I|i|O|o|U|u|Y|y]', '', some_text1)) #5
```

## 6

На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5

```python
some_text1 = ('a s ds fasdyuoiA lkasnfnnlsf askfknflnasl asfkklsdfnlsndf')
count = 0
for i in some_text1.split():
    if len(i) > 5:
        count += 1
print(count) #6
```

## 7

На входе строка со словами, разделенными через 1 пробел. Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.

```python
print(dict((i, len(i)) for i in some_text1.split())) #7
```

## 8

На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.

```python
print([i for i in set(some_text.upper()) if i.isalpha()]) #8
```
## 9

На входе список чисел, получить список квадратов этих чисел / use map
 
```python
print(list(map(lambda x: x*x, range(2, 241, 3)))) #9
```

## 10

На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2. 
На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)

```python
data = [(0, -2), (1, 1), (2, 3), (5, 3)]
print(dict((i, math.sqrt(i[1]*i[1] + i[0]*i[0])) for i in data if i[1]==5*i[0]-2)) #10
```
## 11

Возвести в квадрат все четные числа от 2 до 27. На выходе список.

```python
print(list([i*i for i in range(2, 28, 2)])) #11
```


## 12

На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат (0, 0) в первой четверти 
 
 
```python
min = 9999999999
print([math.sqrt(i[1]*i[1] + i[0]*i[0]) for i in data if i[0]>0 and i[1]>0])
for i in data:
    if i[0] > 0 and i[1] > 0:
        dist = math.sqrt(i[1]*i[1] + i[0]*i[0])
        if dist < min:
            min = dist
print(min)  #12
```
## 13

На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...]


```python
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
print(len(nums_second))
print([(x, y) for y in (np.array(nums_first) + np.array(nums_second)) for x in (np.array(nums_first) - np.array(nums_second))])
```

## 14

На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.

```python
string = ['43141', '32441', '431', '4154', '43121', '44']
print([str(int(i) * int(i)) for i in string if (int(i) * int(i))%2 == 0]) #14
```

## 15


Менеджер как обычно придумал свое представление данных, а нам оно не подходит

input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""


Мы хотим получить нормальную таблицу, чтобы импортировать в csv


[
  {
    'name': 'Petya',
    'grade': '5'
    'subject': 'math'
    'year': '1999'
  },
  {
    'name': 'Vasya',
    'grade': '5'
    'subject': 'language'
    'year': '2000'
  },
  ...
]




```python
input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""

    list(map(dict, (zip(*map(lambda key_values: map(lambda value: (key_values[0], value), key_values[1].split(',')),
                map(lambda key_values_raw: key_values_raw.split(',', 1),s.splitlines()))))))
```
## 16

Получить сумму по столбцам у двумерного списка

a = [[11.9, 12.2, 12.9],
    [15.3, 15.1, 15.1], 
    [16.3, 16.5, 16.5],
    [17.7, 17.5, 18.1]]
    
result = [61.2, 61.3, 62.6]  

```python
   list(map(sum, zip(*numbers))) #16
```
