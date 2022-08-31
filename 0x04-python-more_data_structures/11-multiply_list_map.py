def multiply_list_map(my_list=[], number=0):
    numbers = list(map((lambda x: x * number), my_list))
    return numbers
