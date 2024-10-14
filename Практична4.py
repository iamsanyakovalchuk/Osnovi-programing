def remove_duplicates(input_list):
    element = list(set(input_list))
    return element

def sort_int_str(input_list):
    int_sort = sorted([x for x in input_list if isinstance(x, (int, float))])
    str_sort = sorted([x for x in input_list if isinstance(x, str)], key=str.lower)
    return int_sort + str_sort

input_list = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

result = remove_duplicates(input_list)

result = sort_int_str(result)

print(result)
