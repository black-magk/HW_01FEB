def linear_search(value_to_find, array_to_search_through):
    # for loop for the array to searrch through looking for valuetofind
    # if

    for index, value in enumerate(array_to_search_through):
        if value_to_find == value:
            return index

    return "Not Found"


def linear_search_global(value_to_find, array_to_search_through):
    # Put empty list

    index_list = []

    for index, value in enumerate(array_to_search_through):
        if value_to_find == value:
            index_list.append(index)
    if (len(index_list) == 0):
        return "No Index's Exist"
    # your code here
    return index_list


# TEST CASES

print(linear_search('a', 'banana'))
print(linear_search('a', 'zzzzzzz'))
print(linear_search_global('a', 'banana'))
print(linear_search_global('n', 'banana'))
