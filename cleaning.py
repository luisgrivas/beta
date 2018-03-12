import distance as dis
import pandas as pd

titles = ['^LIC\s', '^DR\s.', '^MC\s', '^ING\s']

latin_characters = [('Á', 'A'), ('É', 'E'),
                    ('Í', 'I'), ('Ó', 'O'),
                    ('Ú', 'U'), ('Ñ', 'N')]

unwanted_characters = ['.', ',', ';']

RE = '(.*\d+.*|.*\sCV\W*|.*\sINC\W*|.*\sSA\W*|.*\sSC\W*|.*\sLLC\W*|.*\sRL\W*)'


def drop_char(column, char_list=unwanted_characters):
    for char in char_list:
        column = column.str.replace(char, '')
    return column


def sub_char(column, tuple_list=latin_characters):
    for tup in tuple_list:
        column = column.str.replace(tup[0], tup[1])
    return column


def sub_bydist(column, str_list, dist=dis.lev, n=3):
    result = column
    for str1 in str_list:
        tmp = column.apply(dist, args=(str1,))
        result[tmp <= n] = str1
    return result


def clean_name(column):
    return sub_char(drop_char((drop_char(column.fillna('')), titles))).str.strip()


def split_names(column):
    df_column = column.str.split(' ', expand=True)
    return df_column
