def dict_from_lists(keys, values):
    return dict(zip(keys, values))

def lists_from_dict(my_dict):
    values = []
    keys = []
    for key in my_dict:
        keys.append(key)
        values.append(my_dict.get(key))

    return values, keys

keys = [1, 2, 3]
values = ["1", "2", "3"]

print(dict_from_lists(keys, values))
print(lists_from_dict(dict_from_lists(keys, values)))