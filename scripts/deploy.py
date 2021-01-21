#!/usr/bin/env python3.7.9
# -*- coding: utf-8 -*-

__author__ = 'huyong'


import os
import stat
import paramiko
import traceback
import datetime
from time import sleep
local_dir = '/Users/huyong/allfile/housheng/backstage/dist/'
remote_dir = '/home/huyong/work/backstage/dist'


class SSH(object):

    def __init__(self, ip='192.168.2.11', port=22, username='huyong', password='Hy!!88&&', timeout=30):
        self.ip = ip  # ssh远程连接的服务器ip
        self.port = 22  # ssh的端口一般默认是22，
        self.username = username  # 服务器用户名
        self.password = password  # 密码
        self.timeout = 50  # 连接超时

        # paramiko.SSHClient() 创建一个ssh对象，用于ssh登录以及执行操作
        self.ssh = paramiko.SSHClient()

        # paramiko.Transport()创建一个文件传输对象，用于实现文件的传输
        self.t = paramiko.Transport(sock=(self.ip, self.port))

    def connect(self):
        try:
            self._password_connect()  # 密码登录
            print('login success')
        except:
            print('ssh password connect faild!')
    
    # 执行git打包命令
    def build(self):
        os.system('npm run build:test')
        os.system('git add -A')
        os.system('git commit -m"merge and rebuild"')
        os.system('git push origin test')


        


    # 密码登录
    def _password_connect(self):

        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.ip, port=22,
                         username=self.username, password=self.password)
        self.t.connect(username=self.username,
                       password=self.password)  # sptf 远程传输的连接

    def close(self):
        self.t.close()  # 断开文件传输的连接
        self.ssh.close()  # 断开ssh连接

    def execute_cmd(self, cmd):

        stdin, stdout, stderr = self.ssh.exec_command(cmd)

        res, err = stdout.read(), stderr.read()
        result = res if res else err

        return result.decode()

    # 递归遍历远程服务器指定目录下的所有文件
    def _get_all_files_in_remote_dir(self, sftp, remote_dir):
        all_files = list()
        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]

        files = sftp.listdir_attr(remote_dir)
        for file in files:
            filename = remote_dir + '/' + file.filename

            if stat.S_ISDIR(file.st_mode):  # 如果是文件夹的话递归处理
                all_files.extend(
                    self._get_all_files_in_remote_dir(sftp, filename))
            else:
                all_files.append(filename)

        return all_files

    # 远程服务器上的文件下载到本地
    def download(self, remote_dir, local_dir):
        try:
            sftp = paramiko.SFTPClient.from_transport(self.t)

            all_files = self._get_all_files_in_remote_dir(sftp, remote_dir)

            for file in all_files:
                print(file)
                local_filename = file.replace(remote_dir, local_dir)
                local_filepath = os.path.dirname(local_filename)

                if not os.path.exists(local_filepath):
                    os.makedirs(local_filepath)

                sftp.get(file, local_filename)

        except:
            print('ssh get dir from master failed.')
            print(traceback.format_exc())  # 具体报错信息

    # 上传本地文件到远程
    def upload(self, local_dir, remote_dir):
        try:
            # 连接远程服务器
            sftp = paramiko.SFTPClient.from_transport(self.t)
            # 递归遍历
            for root, dirs, files in os.walk(local_dir):
                for filespath in files:
                    local_file = os.path.join(root, filespath)
                    a = local_file.replace(local_dir, '')
                    remote_file = os.path.join(remote_dir,  a)
                    try:
                        print(local_file, remote_file, '--------------')
                        sftp.put(local_file, remote_file)
                    except:
                        print(traceback.format_exc())
                        sftp.mkdir(os.path.split(remote_file)[0])
                        sftp.put(local_file, remote_file)
                    print("upload %s to remote %s" % (local_file, remote_file))
                for name in dirs:
                    local_path = os.path.join(root, name)
                    a = local_path.replace(local_dir, '')
                    remote_path = os.path.join(remote_dir, a)
                    try:
                        sftp.mkdir(remote_path)
                        print("mkdir path %s" % remote_path)
                    except:
                        print(traceback.format_exc())  # 具体报错信息
            print('upload file success %s ' % datetime.datetime.now())
            

        except:
            print(traceback.format_exc())  # 具体报错信息

    def exec_command(self):
        # 将sshclient的对象的transport指定为以上的transport
        ssh = paramiko.SSHClient()
        ssh._transport = self.t
        # 执行命令,不同的命令使用分号分割开
        stdin, stdout, stderr = ssh.exec_command(
            'cd work/backstage;bash deploy.sh')
        # 获取命令结果
        res, err = stdout.read(), stderr.read()
        result = res if res else err
        print(result.decode())
        # 关闭连接
        ssh.close()
        self.t.close()


def login_push():
    connect = SSH()
    connect.build()
    connect.connect()
    sleep(1)
    connect.upload(local_dir, remote_dir)
    connect.exec_command()
    os.system('git checkout dev')



def login_pull():
    connect = SSH()
    connect.connect()
    sleep(1)
    connect.download(remote_dir, local_dir)


login_push()
