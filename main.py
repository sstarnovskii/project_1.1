import random
import time


def list_generator():
    list__ = []
    a = 0
    p = 1
    while a < 100000:
        list__.append(p)
        p += random.randrange(0, 20)
        a += 1
    print(list__)
    return list__


def bin_find(a_, b_, list__, number):
    if a_ >= b_:
        return None
    if list__[a_] == number:
        return a_
    center = a_ + (b_ - a_) // 2
    if list__[center] == number:
        if center == a_ + 1:
            return center
        else:
            return bin_find(a_, center + 1, list__, number)
    if list__[center] >= number:
        return bin_find(a_, center, list__, number)
    else:
        return bin_find(center + 1, b_, list__, number)


def iteration_find(list__, number):
    for i in range(0, len(list__)):
        if list__[i] != number:
            i += 1
        elif i == len(list__):
            return None
        else:
            return i


list_ = list_generator()
num = int(input('Insert a number to look for: '))
start_bin = time.time()
print('Binary search result:', bin_find(0, len(list_), list_, num))
finish_bin = time.time()
print('Binary search time:', finish_bin - start_bin, 'sec')
start_itr = time.time()
print('Iteration search result:', iteration_find(list_, num))
finish_itr = time.time()
print('Iteration search time:', finish_itr - start_itr, 'sec')
