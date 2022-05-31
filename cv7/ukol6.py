from copy import deepcopy


d_outer = {'a': 1,'b': [1, 2] }
d_inner = {'c': 3.14 }
d_outer['inner'] = d_inner

new_dict_deepcopy = deepcopy(d_outer)

print(d_outer)
print(new_dict_deepcopy)