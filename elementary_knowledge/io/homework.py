# 利用os模块编写一个能实现dir -l输出的程序。

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

import os

def recursive(x):
    path = os.path.join('.', x)
    

# def find_special(name):
#     for x in os.listdir('.'):
#         if os.path.isfile(x):

