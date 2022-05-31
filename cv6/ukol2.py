import numpy as np

def sort_indices(input_list):
    sorted_input_list = np.sort(input_list, kind='quicksort')

    indexes = []
    for num in sorted_input_list:
        indexes.append(input_list.index(num))

    return indexes

def apply_inds(lst, inds):
    new_list = []

    for index in inds:
        new_list.append(lst[index])
    
    return new_list

lst = [4, 3, 1, 2]
inds = sort_indices(lst)
print(inds)

result = apply_inds([1, 2, 3], [0, 2, 1])
print(result)