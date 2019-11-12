import timeit


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
# ---------------------------------------------------------------


def get_odd_elements(x, start):
    """
    Function should return a list containing first 'x' odd elements,
    starting from 'start' value.

    >>> get_odd_elements(2, 31)
    [31, 33]

    >>> get_odd_elements(3, 10)
    [11, 13, 15]
==
    """
    list_witihin_range_start_and_up = []
    for number in range(start, 100):    # chagne to while loop, because of the range!
        list_witihin_range_start_and_up.append(number)
    
    list_with_odd_numbers = []

    for elem in list_witihin_range_start_and_up:
        if elem % 2 != 0:
            list_with_odd_numbers.append(elem)
        
    first_x_elements_of_list_with_odd_numbers = list_with_odd_numbers[:x]
    return first_x_elements_of_list_with_odd_numbers


# EXERCISE 2
# list_with_numbers = [1, 6, 3, 7, 0, 11, 13, 15]
# # x = 1
# # odd_numbers = get_odd_elements(x, start)
# # print(odd_numbers)

# list_with_numbers = [1, 6, 3, 7, 0, 11, 13, 15]
# x = 3
# start = 31
# odd_numbers_doctest_final = get_odd_elements(2, 31)
# print(odd_numbers_doctest_final)

# list_with_numbers = [31]
# odd_numbers_doctest_final = get_odd_elements(4, list_with_numbers)
# print(odd_numbers_doctest_final)
# ---------------------------------------------------------------


def get_sum_of_all_even_elements(my_list):
    """
    Function should sum all it's even elements and return it as an integer.

    >>> get_sum_of_all_even_elements([1, 15, 21])
    0

    >>> get_sum_of_all_even_elements([1, 2, 3, 6, 9, 11])
    8

    """
    sum_of_list_of_all_even_elemnts = 0
    list_of_all_even_elements = []
    for elem in my_list:
        if elem % 2 == 0:
            list_of_all_even_elements.append(elem)
    sum_of_list_of_all_even_elemnts = sum(list_of_all_even_elements)
    return sum_of_list_of_all_even_elemnts     


# EXERCISE 3
# my_list = [1, 6, 3, 7, 0, 11, 10, 13, 15]
# sum_of_all_even_elements = get_sum_of_all_even_elements(my_list)
# print(sum_of_all_even_elements)
# ---------------------------------------------------------------


def get_letters_statistics(word):
    """
    Function should return a dictionary where keys are letters and coresponding values are quantities of that letters.

    >>> result = get_letters_statistics('abc')
    >>> result == {'a': 1, 'b': 1, 'c': 1}
    True

    >>> result2 = get_letters_statistics('abrakadabra')
    >>> result2 == {'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1}
    True

    """
    # word = sorted(word)

    # VERSION WITH LIST AND DICTIONARY
    # letters_list = []
    # for letter in word:
    #     letters_list.append(letter)
    
    # dict_of_letters = {}
    # for elem in letters_list:
    #     if elem in dict_of_letters:
    #         dict_of_letters[elem] += 1
    #     else:
    #         dict_of_letters[elem] = 1

    # return dict_of_letters

    # VERSION WITH JUST DICTIONARY
    dict_of_letter_frequency = {} 
  
    for letter in word: 
        if letter in dict_of_letter_frequency: 
            dict_of_letter_frequency[letter] += 1
        else: 
            dict_of_letter_frequency[letter] = 1
    # print(all_freq)
    return dict_of_letter_frequency


# EXERCISE 4
# word = 'abc'
# letters_statistic = get_letters_statistics('abrakadabra')
# print(letters_statistic)
# ---------------------------------------------------------------

start = timeit.default_timer()

letters_statistic2 = get_letters_statistics('abc')
print(letters_statistic2)

stop = timeit.default_timer()
execution_time = stop - start

print("Program Executed in ", execution_time)  # It returns time in sec