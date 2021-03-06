import copy
from utils import time_profiling

@time_profiling
def select_sort(items):
    for i, it1 in enumerate(items):
        min = it1
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < min:
                min = items[j]
                min_index = j
        if min_index != i:
            __exchange(items, i, min_index)

@time_profiling
def insert_sort(elements):
    for i, e in enumerate(elements):
        for j in reversed(range(0, i)):
            if elements[j] > elements[j + 1]:
                __exchange(elements, j, j + 1)
            else:
                break

@time_profiling
def shell_sort(elements):
    h = 1
    while h < int(len(elements) / 3):
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, len(elements), h):
            for j in reversed(range(h, i + 1, h)):
                if elements[j] < elements[j - h]:
                    __exchange(elements, j, j - h)
                else:
                    break

        h = int(h / 3)

@time_profiling
def merge_sort(elements):
    __merge_sort(elements)

@time_profiling
def merge_sort_bu(elements):
    length = len(elements)
    step = 1
    while step < length:
        low = 0
        while low < length - step:
            __merge(elements, low, low + step - 1, min(low + step * 2 - 1, length - 1))
            low += step * 2
        step *= 2

@time_profiling
def quick_sort(elements):
    __quick_sort(elements)

@time_profiling
def heap_sort(elements):
    __heapify(elements)
    for i in range(1, len(elements)):
        __exchange(elements, 1, len(elements) - i)
        __heap_sink(elements, 1, start=1, end=len(elements) - i - 1)

    for i in range(0, len(elements) - 1):
        if __less(elements, i + 1, i):
            __exchange(elements, i + 1, i)
        else:
            break

    return elements

def __heapify(elements):
    n = len(elements) - 1
    i = int( n / 2)
    while i > 0:
        __heap_sink(elements, i)
        i -= 1

def __heap_sink(elements, index, start=None, end=None):
    if start is None:
        start = 1
    if end is None:
        end = len(elements) - 1

    while 2 * index <= end:
        k = 2 * index
        if k < end and __less(elements, k, k + 1):
            k += 1
        if __less(elements, index, k):
            __exchange(elements, index, k)
            index = k
        else:
            break

def __heap_swim(elements, index):
    while int(index / 2) > 1:
        p = int(index / 2)
        if __less(elements, p, index):
            __exchange(elements, p, index)
            index = p

def __merge_sort(elements, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(elements) - 1

    if low >= high:
        return

    mid = int((low + high) / 2)
    __merge_sort(elements, low, mid)
    __merge_sort(elements, mid + 1, high)
    __merge(elements, low, mid, high)

def __quick_sort(elements, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(elements) - 1

    if low >= high:
        return

    mid = __partition(elements, low, high)
    __quick_sort(elements, low, mid - 1)
    __quick_sort(elements, mid + 1, high)

def __partition(elements, low, high):
    pos_element = elements[low]
    lf_index = low + 1
    rt_index = high
    while True:
        while lf_index < high and elements[lf_index] <= pos_element:
            lf_index += 1
        while rt_index > low and elements[rt_index] > pos_element:
            rt_index -= 1

        if lf_index >= rt_index:
            break
        
        __exchange(elements, lf_index, rt_index)
        # print('inner exchage: {}'.format(elements))

    __exchange(elements, low, rt_index)
    # print('outter exchage: {}'.format(elements))

    return rt_index

def __merge(elements, low, mid, high):
    copied_elements = copy.copy(elements)
    for i in range(0, high - low + 1):
        copied_elements[i] = elements[low + i]

    l_index = low
    r_index = mid + 1
    for i in range(low, high + 1):
        if l_index > mid and r_index <= high:
            elements[i] = copied_elements[r_index - low]
            r_index += 1
        elif l_index <= mid and r_index > high:
            elements[i] = copied_elements[l_index - low]
            l_index += 1
        elif l_index > mid and r_index > high:
            break
        else:
            if copied_elements[l_index - low] > copied_elements[r_index - low]:
                elements[i] = copied_elements[r_index - low]
                r_index += 1
            elif copied_elements[l_index - low] < copied_elements[r_index - low]:
                elements[i] = copied_elements[l_index - low]
                l_index += 1
            else:
                elements[i] = copied_elements[l_index - low]
                l_index += 1

def __exchange(elements, index1, index2):
    if not elements or index1 == index2:
        return
    
    elements[index1], elements[index2] = elements[index2], elements[index1]

def __less(elements, x, y):
    return elements[x] < elements[y]
