def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print('10 number %d' % fact(10))
