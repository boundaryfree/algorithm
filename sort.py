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
            exchange_element(items, i, min_index)

@time_profiling
def insert_sort(elements):
    for i, e in enumerate(elements):
        for j in reversed(range(0, i)):
            if elements[j] > elements[j + 1]:
                exchange_element(elements, j, j + 1)
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
                    exchange_element(elements, j, j - h)
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
            merge(elements, low, low + step - 1, min(low + step * 2 - 1, length - 1))
            low += step * 2
        step *= 2
    
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
    merge(elements, low, mid, high)

@time_profiling
def quick_sort(elements):
    pass

def merge(elements, low, mid, high):
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

def exchange_element(elements, index1, index2):
    if not elements or index1 == index2:
        return
    
    elements[index1], elements[index2] = elements[index2], elements[index1]
