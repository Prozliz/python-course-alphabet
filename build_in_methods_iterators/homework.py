from typing import List, Dict, Union, Generator
from string import ascii_lowercase

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    for list_dict in data:
        for key, value in list_dict.items():
            if key == 'name' and value[0] in ascii_lowercase:
                line = value[0].upper() + value[1:]
                list_dict.update(('name', line) for k, v in list_dict.items())

    """Make all `names` field in list of students to start from upper letter
    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    for names in d[name]:
        if 
    """
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    for dict in data:
        for reund_k in redundant_keys:
            if reund_k in dict.keys():
                del dict[reund_k]
    """given_data
    Remove from dictionaries given key value
    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    for dic in data:
        for key, valu in dic.items():
            if valu == value:

    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    return [dic]


def task_4_min_value_integers(data: List[int]) -> int:
    if data != []:
        """
        Find and return minimum value from list
        """
        return min(data)
    else:
        return None


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    dict = {}
    if data != []:

        for subj in data:
            if type(subj) == int:
                subj = str(subj)
                dict.update({len(subj): subj})
            else:
                dict.update({len(subj): subj})
        return dict[min(dict.keys())]
    else:
        return None


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    lst = []
    for dic in data:
        if key in dic:
            lst += [dic[key]]
    for dic in data:
        if key in dic:
            if min(lst) == dic[key]:
                return dic


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    max_num = -100
    for lst in data:
        for num in lst:
            if num >= max_num:
                max_num = num
            """
            Find max value from list of lists
            """
    return max_num


def task_8_sum_of_ints(data: List[int]) -> int:
    summa = 0
    for num in data:
        summa += num
    """
    Find sum of all items in given list
    """
    return summa


def task_9_sum_characters_positions(text: str) -> int:
    suma = 0
    for symb in text:
        suma += ord(symb)
    """
        Please read first about ascii table.
        https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
        You need to calculate sum of decimal value of each symbol in text
        Examples:
            task_9_sum_characters_positions("A")
            >>> 65
            task_9_sum_characters_positions("hello")
            >>> 532
    """
    return suma


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    return (number for number in range(2, 201) if all([1 if number % x != 0 else 0 for x in range(2, number)]))


def task_11_create_list_of_random_characters() -> List[str]:
    import random
    List = [random.choice(list(ascii_lowercase)) for x in range(20)]
    """
    Create list of 20 elements where each element is random letter from latin alphabet
    """
    return List

