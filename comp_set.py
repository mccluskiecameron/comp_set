"""
a library for making and retrieving compact sets
"""

from itertools import islice

def last(it):
    for i in it:
        pass
    return i

def it_choose(n, k):
    f = 1
    for i in range(k+1, n+1):
        yield f
        f *= i
        f //= (i - k)
    yield f

def choose(n, k):
    return last(it_choose(n, k))

def it_cs(n, k, a):
    """
    retrieve the values of a compact set as an iterator

        n: any non-negative integer
        k: any non-negative integer not greater than n
        a: any non-negative integer below choose(n, k)
    """
    bottom = -1
    for k in range(k, 0, -1):
        pch = 0
        for i, ch in enumerate(it_choose(n, k)):
            if a < ch:
                bottom += n-i - k + 1
                yield bottom
                n = k + i - 1
                a -= pch
                break
            pch = ch
        else:
            raise ValueError(f"a >= than n choose k ({a} >= {ch})")

def l_cs(n, k, a):
    """
    retrieve the values of a compact set as a list

        n: any non-negative integer
        k: any non-negative integer not greater than n
        a: any non-negative integer below choose(n, k)
    """
    return list(it_cs(n, k, a))

def cs(n, l):
    """
    create a compact set

        n: a non-negative integer
        l: a list of non-negative integers below n, ordered from least to
           greatest, and without repetitions. 
    """
    k = len(l)
    a = 0
    ne = n
    pb = -1
    for i in range(k):
        diff = l[i] - pb - 1 + (k-i)
        pb = l[i]
        ie = ne - diff
        if ie>0:
            a += next(islice(it_choose(ne, k-i), ie-1, None))
        ne = n - l[i] - 1
    return a

__all__ = ["it_cs", "l_cs", "cs"]

