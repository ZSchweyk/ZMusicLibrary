def fill_in_list(array: list, values_to_replace_with_2d_array: list, value_to_replace):
    count = 0
    while value_to_replace in array:
        index = array.index(value_to_replace)
        array[index] = [arr[count] for arr in values_to_replace_with_2d_array]
        count += 1
    return array


def count_appearances(array, value):
    return 0 if len(array) == 0 else sum([item == value for item in array])


def get_val_with_index(array, index):
    index = index % len(array)
    return array[index]

def index_of(array, elem):
    array_of_indices = []
    for i, sub_elem in enumerate(array):
        if elem == sub_elem:
            array_of_indices.append(i)
    return array_of_indices

