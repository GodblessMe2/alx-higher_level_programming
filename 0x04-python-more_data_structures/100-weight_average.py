def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        wht = 0
        for i in my_list:
            num += (i[0] * i[1])
            wht += i[1]
        return (num / wht)
    return 0
