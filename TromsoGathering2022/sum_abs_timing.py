import random
import numpy as np

N = 1_000_000
xlst = list( random.uniform(-10.,10.) for _ in range(N) )
xarr = np.array(xlst, dtype='float64')


def ranged_forloop(xs):
    total = 0
    for i in xs:
        total += abs(i)
    return total


def indexed_forloop(xs):
    total = 0
    L = len(xs)
    for i in range(L):
        total += abs(xs[i])
    return total


def functional_plain(xs):
    return sum(map(abs,xs))


def functional_numpy(xs):
    return np.sum(np.abs(xs))


ones = np.ones_like(xarr)
def dotprod(xs):
    return np.dot(np.abs(xs), ones)


# python -m timeit -s "import sum_abs_timing as M" "M.ranged_forloop(M.xlst)"
# python -m timeit -s "import sum_abs_timing as M" "M.ranged_forloop(M.xarr)"
# ...


def filter_usage(xs):
    xs = np.asarray(xs)
    # make a boolean array of True/False values
    filter = (xs > 7) & (xs < 8)
    # use the array as index to reference the matching elements
    xs[filter] *= 1000
    
