def sort_dict_by_values(input_dict: dict) -> dict:
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))
    return sorted_dict

input_dict = {'a': 2, 'b': 1, 'c': 3}
sorted_dict = sort_dict_by_values(input_dict)
print("Sorted dictionary by values:", sorted_dict)