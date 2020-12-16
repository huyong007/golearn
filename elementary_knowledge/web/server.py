# server.py
# 从wsgiref模块导入：
from wsgiref.simple_server import  make_server

# 导入自己编写的application函数
from hello import application

httpd = make_server('',8000,application)
print('Serving HTTP on port 8000...')

# 开始监听http请求：
httpd.serve_forever()