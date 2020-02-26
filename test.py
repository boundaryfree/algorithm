import copy
import random
from sort import select_sort, insert_sort, shell_sort, merge_sort, merge_sort_bu

sort_alg_map = {
    # 'select': select_sort,
    # 'insert': insert_sort,
    # 'shell sort': shell_sort,
    'merge sort': merge_sort,
    'merge sort bottom to up': merge_sort_bu,
}

def test(elements, algorithms=[]):
    if not algorithms:
        algorithms = sort_alg_map.keys()
    
    for alg_name in algorithms:
        fun = sort_alg_map.get(alg_name, None)
        if not fun:
            print('{} sort algorithm implementation NOT found'.format(alg_name))
            continue
        
        sorting_elements = copy.deepcopy(elements)
        print('-' * 20 + 'Begin executing {}, count {}'.format(alg_name, len(sorting_elements)) + '-' * 20)
        fun(sorting_elements)
        print('Sort result: {}'.format(is_sorted(sorting_elements)))
        # print('Sorted list: {}'.format(sorting_elements))
        print('-' * 20 + 'End executing {}'.format(alg_name) + '-' * 20)

def is_sorted(items):
    for index, it in enumerate(items):
        if index > 0 and it < items[index - 1]:
            return False

    return True
        
if __name__ == '__main__':
    count = 10000
    elements = [random.randint(0, count - 1) for x in range(0, count)]
    # elements = [x for x in range(0, count)]
    # print('Original list: {}'.format(elements))

    test(elements)