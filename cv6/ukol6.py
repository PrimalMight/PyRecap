import numpy as np

palacinky = [3, 2, 8, 1]

def is_sorted(lst):
    if lst == np.sort(lst, kind='mergesort'):
        return True
    return False

def stick_and_flip(lst):
    max_index = lst.index(max(lst))
    on_spatula = lst[:max_index + 1]
    new_pancake_stack = []

    new_pancake_stack.append(on_spatula[::-1])
    new_pancake_stack.append(lst[max_index + 1:])

    return [item for sublist in new_pancake_stack for item in sublist][::-1]


print(stick_and_flip(palacinky))