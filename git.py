import os
import sys
# global commitTag
if len(sys.argv) == 1:
    commitTag = input('请输入commit参数')
else:
    commitTag = sys.argv[1]
os.system('git add -A')
os.system('git commit -m"%s"' % commitTag)

os.system('git push origin master')
