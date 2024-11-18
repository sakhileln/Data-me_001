# TODO: Implement the following functions based on the descriptions.


def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    return lst[::-1]


def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    return lst.count(element)


def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    return [key for key, val in dct.items() if val == value]


def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    new_lst = lst1 + lst2
    return sorted(new_lst)


def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    if len(list(set(numbers))) <= 1:
        return None 
    mx = max(numbers)
    idx = numbers.index(mx)
    numbers.pop(idx)
    return max(numbers)


def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.

    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.

    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    count = 0
    if len(str1) == len(str2):
        for ch in str1:
            if ch in str2:
                count += 1
    if count == len(str1):
        return True
    return False



def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    nw_lst = []
    for lt in nested_list:
        for elem in lt:
            nw_lst.append(elem)
    return nw_lst


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    return list(set(lst))


def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    cm_set = set(lst1) & set(lst2)
    return list(cm_set)
