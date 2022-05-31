def sort_dict_by_keys(my_dict):
    keys = []
    new_dict = {}

    for key in my_dict:
        keys.append(key)
    keys.sort()

    for key in keys:
        new_dict[key] = my_dict.get(key)
    return new_dict
    

def sort_dict_by_values(my_dict):
    def invert_dict(my_dict):
        keys = []
        values = []

        for key in my_dict:
            keys.append(key)
            values.append(my_dict.get(key))
        
        return dict(zip(values, keys))

    return invert_dict(sort_dict_by_keys(invert_dict(my_dict)))

    

d = {'b': -2,'c': 3,'a': 1 }
print(sort_dict_by_keys(d))
print(sort_dict_by_values(d))