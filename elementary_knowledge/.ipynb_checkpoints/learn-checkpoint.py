#!/usr/bin/env python3
# -*- coding: utf-8  -*-

import sys
'a test module'


__author__ = 'Michael Liao'


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello,%s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == "__main__":
    test()

    # """ 启动交互式环境时候无法引入该模块 """


def _private_1(name):
    print('hello,%s' % name)


def _private_2(name):
    return 'Hi,%s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
