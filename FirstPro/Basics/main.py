import numpy as np
from sys import stdin, stdout


def get_xs(Type=int): return map(Type, stdin.readline().strip().split())


def input_int(): return int(stdin.readline())


def write(w, end="\n"): stdout.write(str(w) + end)


for i in range(input_int()):
    n, m, k = get_xs()
    arr = np.array([],dtype='int8')
    for j in range(n):
        arr = np.append(arr,list(get_xs()))

    print(arr)