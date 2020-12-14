# from email.mime.text import MIMEText

# msg = MIMEText('hello,send by python...', 'plain', 'utf-8')




# from_addr = input('From: ')
# password = input('Password: ')

# to_addr = input('To: ')

# smtp_server = input('SMTP server: ')

# import smtplib

# server = smtplib.SMTP(smtp_server,25)

# server.set_debuglevel(1)

# server.login(from_addr,password)

# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()

import os,sqlite3
# exercise about db and python connection
db_file = os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key,name varchar(20),score int)')
cursor.execute(r"insert into user values('A-001','Adam',95)")
cursor.execute(r"insert into user values('A-002','Bart',62)")
cursor.execute(r"insert into user values('A-003','Lisa',78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low,hight):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('select name from user where score >=? and score <=?',(low,hight))
        values = cursor.fetchall()
        res = []
        for item in values:
            res.append(item[0])
        print(res)
        return res
        cursor.close()
        conn.commit()
        conn.close()
    except:
        pass
    finally:
        cursor.close()
        conn.commit()
        conn.close()


get_score_in(80,100)
