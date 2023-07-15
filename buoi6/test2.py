def sum_array(lst):
    _min = min(lst)
    _max = max(lst)
    return sum(lst) - min(lst) - max(lst)



_list = [1,2,3,4,5]
print(sum_array(_list))