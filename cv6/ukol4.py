def pretty_print(lst, level=0):
    for obj in lst:
        if isinstance(obj, list):
            pretty_print(obj, level + 1)
        else:
            for lvl in range(0, level):
                print('\t ', end="")
            print(obj)    
        

tree = ["a", ["b", "c", "d", "e", ["f", "g", "h", ["i", "j"], "k"], "l"]]
pretty_print(tree)
