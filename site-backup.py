# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import strftime,gmtime
import smtplib, MySQLdb, time, os, tarfile, ConfigParser

config=ConfigParser.ConfigParser()
config.read("site-backup.cfg")

# 获取时间
serverTime = str(time.strftime("%Y-%m-%d"))
backTime = float(config.get("time", "backTime"))
# 邮件变量
from_addr = config.get("mail", "from_addr")
password = config.get("mail", "password")
smtp_server = config.get("mail", "smtp_server")
to_addr = config.get("mail", "to_addr")
mail_sender = config.get("mail", "mail_sender")
mail_recipient =  config.get("mail", "mail_recipient")
mail_title = config.get("mail", "mail_title")
# Mysql变量
mysql_host = config.get("mysql", "mysql_host")
mysql_user = config.get("mysql", "mysql_user")
mysql_password = config.get("mysql", "mysql_password")
mysql_database = config.get("mysql", "mysql_database")

# 网站文件变量
siteName = config.get("flies", "siteName")
dirName = siteName + "-" + serverTime
dirPath = config.get("flies", "dirPath")
siteBack_name = 'dirName.tar.gz'

# SQL和压缩包变量
backMysql_name = siteName + "-" + serverTime + '.sql'
sendSitePack = dirName + ".tar.gz"


# 导出数据库函数
def outMysql():
    mysql_cmd = "mysqldump -u " + mysql_user + " -p" + mysql_password + " " + mysql_database + " > " + dirPath + backMysql_name
    os.system(mysql_cmd)

# 打包网站文件函数
def siteFile():
    t = tarfile.open(dirName + ".tar.gz", "w:gz")
    for root, dir, files in os.walk(dirPath):
        for file in files:
            fullpath = os.path.join(root, file)
            t.add(fullpath)
    t.close()

# 发送邮件（备份包）函数
def sendMail():
    message = MIMEMultipart()
    message.attach(MIMEText('备份于' + serverTime, 'plain', 'utf-8'))
    att = MIMEText(open(sendSitePack, 'rb').read(), 'base64', 'gb2312')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = "attachment; filename=" + sendSitePack
    message.attach(att)
    message['From'] = mail_sender
    message['To'] = mail_recipient
    message['Subject'] = mail_title + serverTime

    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], message.as_string())
    server.quit()


# 整个任务函数
def backSite():
    outMysql()
    if os.path.exists(dirPath + backMysql_name):
        siteFile()

    if os.path.exists(sendSitePack):
        sendMail()

    os.remove(dirPath + backMysql_name)
    os.remove(sendSitePack)

# 循环执行备份任务
while True:
    backSite()
    time.sleep(backTime)
