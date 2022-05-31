def group_dict(words, len): # len here acts as choosing mechanism by which we categorize words, shouldnt be called len tho, we have overwritten len() function to our own
    my_dict = {}
    
    for word in words:
        if len(word) in my_dict:
            my_dict[len(word)].append(word)
        else:
            my_dict[len(word)] = [word]

    return my_dict

def first_letter(x):
    return x[0]

words = ['jeden','dva','tri','štyri','pat','šesť']
print(group_dict(words, first_letter))
