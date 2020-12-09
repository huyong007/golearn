def foo(s):
    n = int(s,10.0)
    if n == 0:
        raise ValueError('invalid value:%s' % s)
    return 10/n


def bar():
    try:
        foo('7.6')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

