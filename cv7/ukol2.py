def invert_dict(my_dict):
    keys = []
    values = []

    for key in my_dict:
        keys.append(key)
        values.append(my_dict.get(key))
    
    return dict(zip(values, keys))


orig = {1:'a', 2:'b', 3:'c'}
print(invert_dict(orig))