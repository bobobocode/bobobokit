#!/usr/bin/env python3

import random


def select_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        min = i
        for j in range(i+1, n):
            if seq[min] > seq[j]:
                min = j
        if min != i:
            seq[i], seq[min] = seq[min], seq[i]
    return seq


def bubble_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq


def insert_sort(s):
    n = len(s)
    for i in range(1, n):
        for j in reversed(range(1, i + 1)):
            if s[j] < s[j-1]:
                s[j], s[j-1] = s[j-1], s[j]
            else:
                break
    return s


if __name__ == "__main__":
    seq = list(range(10))
    random.shuffle(seq)
    print(seq)
    #r = bubble_sort(seq)
    #r = select_sort(seq)
    r = insert_sort(seq)
    print(r)
