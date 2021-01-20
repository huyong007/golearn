#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-


__author__ = 'huyong'

from selenium import webdriver
# 文档地址https://selenium-python-zh.readthedocs.io/en/latest/index.html
from selenium.webdriver.chrome.options import Options
import sys

config = {
    'dev': 'http://localhost:9528/',
    'test': 'http://192.168.2.11:9020/',
    'rel': 'http://rel.new.boss.shunbus.com/',
}


def login():
    # 此处声明为全局变量否则会在打开chrome之后闪退
    global driver

    options = Options()
    # 如果是chromium内核,如果是chrome不用此操作就找到对应文件位置修改变量
    options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    # 驱动存放地址,下载地址http://chromedriver.storage.googleapis.com/index.html
    driver_path = '/usr/local/bin/chromedriver'
    # 生成驱动
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    # driver = webdriver.Chrome() # chrome直接执行此命令
    # 隐藏式等待执行,查找元素的时候最多等待10秒
    driver.implicitly_wait(10)
    # 根据不同的命令行参数登录不同的地址
    login_url = 'http://192.168.2.11:9020/' if len(
        sys.argv) == 1 else config[sys.argv[1]]
    driver.get(login_url)
    try:
        # 此处之所以是数组是因为我为了fix vue的autoinput的bug,用户名和密码都使用了两个input隐藏了其中的一个
        nameList = driver.find_elements_by_name('username')
        name = nameList[0] if len(nameList) == 1 else nameList[1]
        name.send_keys('huyong')
        psdList = driver.find_elements_by_name('password')
        psd = psdList[0] if len(psdList) == 1 else psdList[1]
        name.send_keys('xxx密码xx')
        driver.find_element_by_class_name("el-button").click()
    except:
        driver.quit()
    finally:
        print('成功登录了 %s' % login_url)


login()
