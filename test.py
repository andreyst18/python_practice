def func_apply(f, l):
    res = []
    for item in l:
        res.append(f(item))
    return res


def pow2(n):
    return n**2


print(func_apply(pow2, [3, 2]))
