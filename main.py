import math
import sys

w=5

def SelectPart(array , k):
    left, right = 0, len(array)
    array.append(sys.maxsize)
    while True:
        v = partition(array, left, right)
        if k < v:
            right = v - 1
        elif k == v:
            return v
        else:
            left = v + 1


def SelectOpt( array , k,left,right):
    while True:
     d = right - left
     if d <= w:
         array = InsertionSort(array, left, right)
         return left + k
     dd = int(math.floor(d / w))
     for i in range(1, dd + 1, 1):
         array = InsertionSort(array, left + w * (i - 1), left + i * w - 1)
         swap(array, left + i - 1, left + w* (i - 1) + int(math.ceil(w / 2)) - 1)
     v = SelectOpt(array, int(math.ceil(dd / 2)), left, left + dd - 1)
     array[left], array[v] = array[v], array[left] 
     v = partition(array, left, right)
     temp = v - left
     if k > temp:
         k -= temp
         left = v + 1
     elif k == temp:
         return v
     else:
         right = v - 1


def InsertionSort(array, left, right):
    for i in range(left, right + 1, 1):
        new_element = array[i]
        location = i - 1
        while location >= 0 and array[location] > new_element:
            array[location + 1] = array[location]
            location -= 1
        array[location + 1] = new_element
    return array


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]

def partition(array, first, last):
    p_value = array[first + 1]
    low = first + 1
    up = last
    array[low], array[up] = array[up], array[low]
    while low < up:
        while array[up] > p_value:
            up -= 1
        while array[low] < p_value:
            low += 1
        array[low], array[up] = array[up], array[low]
    array[low], array[up] = array[up], array[low]
    array[first], array[up] = array[up], array[first]
    return up


with open('input.txt') as f:
    s = f.readline()
    s = int(s)
    array = list(map(int, f.readline().split()))

with open('output.txt', 'a') as f:
    f.write(str(SelectPart(array, s)))
    f.write('\n')
    f.write(str(SelectOpt(array, s, 0, len(array) - 1)))