#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def search_replace_value(i):
        return (i if i != search else replace)
    return list(map(search_replace_value, my_list))
