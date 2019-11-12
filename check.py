
def get_common_elements(first_list, second_list):
    """
    Function should return a list containing elements that are on both input lists.

    >>> get_common_elements([1, 2, 3], [3, 4, 5])
    [3]

    >>> get_common_elements([3, 5, 8], [3, 4, 5, 12, 8])
    [3, 5, 8]

    """

    common_elements = []

    for elem in first_list:
        if elem in second_list:
            common_elements.append(elem)
    
    return common_elements


# EXERCISE 1

# first_list = [1, 2, 3, 5, 'test', 'piwo', 0, 11, 'o']
# second_list = [1, 6, 3, 7, 0, 'test']
# ce = get_common_elements(first_list, second_list)
# print(ce)
# ce_doctest = get_common_elements([1, 2, 3], [3, 4, 5])
# print(ce_doctest)
