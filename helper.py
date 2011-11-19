def compose(func_list, input):
    o = input
    for func in func_list:
        o = func(o)
    return o
