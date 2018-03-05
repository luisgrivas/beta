import numpy as np

letters = 'abcdefghijklmnopqrstuvwxyz'


def splits(string):
    return [(string[:i], string[i:]) for i in range(len(string) + 1)]


def transposes(string):
    all_splits = splits(string)
    return [L + R[1] + R[0] + R[2:] for L, R in all_splits if len(R) > 1]


def deletes(string):
    all_splits = splits(string)
    return [L + R[1:] for L, R in all_splits if R]


def replaces(string):
    all_splits = splits(string)
    return [L + c + R[1:] for L, R in all_splits if R for c in letters]


def inserts(string):
    all_splits = splits(string)
    return [L + c + R for L, R in all_splits for c in letters]


def lev(str1, str2, weigts=(1, 1, 1)):
    m = len(str1)
    n = len(str2)
    dist = np.zeros((m + 1, n + 1))

    for i in range(m + 1):
        dist[i][0] = i

    for j in range(n + 1):
        dist[0][j] = j

    for j in range(n):
        for i in range(m):
            if str1[i] == str2[j]:
                dist[i + 1][j + 1] = dist[i][j]
            else:
                dist[i + 1][j + 1] = min(dist[i][j + 1] + 1,
                                         dist[i + 1][j] + 1,
                                         dist[i][j] + 1)
    return dist[m][n]


def dam_lev(str1, str2, weights=(1, 1, 1)):
    m = len(str1)
    n = len(str2)
    dist = np.zeros((m + 1, n + 1))

    for i in range(m + 1):
        dist[i][0] = i

    for j in range(n + 1):
        dist[0][j] = j

    for j in range(n):
        for i in range(m):
            if str1[i] == str2[j]:
                dist[i + 1][j + 1] = dist[i][j]
            else:
                dist[i + 1][j + 1] = min(dist[i][j + 1] + 1,
                                         dist[i + 1][j] + 1,
                                         dist[i][j] + 1)
            if i > 0 and j > 0:
                if str1[i] == str2[j - 1] and str1[i - 1] == str2[j]:
                    dist[i + 1][j + 1] = min(dist[i + 1][j + 1],
                                             dist[i - 1][j - 1] + 1)
    return dist[m][n]
