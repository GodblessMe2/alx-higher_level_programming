def complex_delete(a_dictionary, value):
    key_del = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            key_del.append(i)
    for j in key_del:
        del a_dictionary[j]
    return a_dictionary
