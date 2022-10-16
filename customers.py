from typing import Dict

MAX_5 = 100000
MAX_6 = MAX_5 + 1000000
MAX_7 = MAX_6 + 10000000

DIGITS_6 = 1000000
DIGITS_7 = 10000000


def number_group(idx: str) -> int:
    """Функция, которая вычисляет номер группы"""
    group = 0
    for n in idx:
        group += int(n)
    return group


def count_members(group_dict, n_customers, number, i=0) -> Dict:
    """Функция, которая подсчитывает число покупателей в группах"""
    null = '0'
    while i < n_customers:
        null_to_insert = null * (number - len(str(i)))
        idx = f'{null_to_insert}{i}'
        key = number_group(idx)
        if key in group_dict:
            group_dict[key] = group_dict[key] + 1
        else:
            group_dict[key] = 1
        i += 1
    return group_dict


def func1(n_customers: int) -> Dict:
    """Функция, которая подсчитывает число покупателей,
    попадающих в каждую группу, если нумерация ID сквозная и начинается с 0.
    На вход функция получает целое число n_customers (количество клиентов)."""
    group_dict = {}
    if n_customers <= MAX_5:
        count_members(group_dict, n_customers, 5)
    if MAX_5 < n_customers <= MAX_6:
        i = n_customers - MAX_5
        count_members(group_dict, MAX_5, 5)
        count_members(group_dict, i, 6)
    if MAX_6 < n_customers <= MAX_7:
        i = n_customers - MAX_5 - DIGITS_6
        count_members(group_dict, MAX_5, 5)
        count_members(group_dict, DIGITS_6, 6)
        count_members(group_dict, i, 7)
    return group_dict


def func2(n_customers: int, n_first_id: str) -> Dict:
    """Функция, аналогичная первой, если ID начинается с произвольного числа.
    На вход функция получает целые числа: n_customers (количество клиентов)
    и n_first_id (первый ID в последовательности)."""""
    group_dict = {}
    first_id = int(n_first_id)
    amount_ids = n_customers + first_id
    start_pos = len(n_first_id)
    if start_pos == 5:
        difference = MAX_5 - first_id
        if amount_ids <= MAX_5:
            count_members(group_dict, amount_ids, 5, first_id)
        if MAX_5 < amount_ids <= DIGITS_6 + difference:
            i = n_customers - MAX_5 - first_id
            count_members(group_dict, MAX_5, 5, first_id)
            count_members(group_dict, i, 6)
        if DIGITS_6 + difference < amount_ids <= MAX_7:
            i = n_customers - DIGITS_6 - difference
            count_members(group_dict, MAX_5, 5, first_id)
            count_members(group_dict, DIGITS_6, 6)
            count_members(group_dict, i, 7)

    if start_pos == 6:
        if amount_ids <= DIGITS_6:
            count_members(group_dict, amount_ids, 6, first_id)
        if DIGITS_6 < amount_ids <= DIGITS_7 + DIGITS_6:
            i = n_customers - (DIGITS_6 - first_id)
            count_members(group_dict, DIGITS_6, 6, first_id)
            count_members(group_dict, i, 7)

    if start_pos == 7:
        if amount_ids <= DIGITS_7:
            count_members(group_dict, amount_ids, 7, first_id)
    return group_dict
