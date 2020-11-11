import os

print(os.environ.get('x', 'default'))


print(os.path.abspath('.'))


# os.path.join('/Users/huyong/allfile/learn/python','testdir')
# os.mkdir('/Users/huyong/allfile/learn/python/testdir')

# os.rmdir('/Users/huyong/allfile/learn/python/testdir')

print(os.path.split('/Users/huyong/allfile/learn/python/io/test.txt'))

print([x for x in os.listdir('.') if os.path.isfile(
    x)])
