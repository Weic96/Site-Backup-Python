# Python 网站自动备份脚本

边学边用的Python新人，欢迎指点https://weic96.cn/python-site-backup


### 开始

首先需要安装一些Python模块

> smtplib, MySQLdb, time, os, tarfile, ConfigParser

###### 开发版python是必须的

```
apt-get install python-dev                 # Debian系

yum install python-devel                   # RedHat系
```

<p></p>

###### MySQL-python
到 [这里](https://pypi.python.org/pypi/MySQL-python) 下载适合自己系统的版本，Windows系统的直接双击 ==exe== 安装，Linux解压并进入下载的 ==MySQL-python== 然后输入下面命令安装
```
python setup.py install
```

如果提示:
```
EnvironmentError: mysql_config not found
```

输入下面命令安装 ==mysql_config==
```
apt-get install libmysqlclient-dev                 # Debian系
yum install libmysqlclient-devel                   # RedHat系
```
然后重新安装 ==MySQL-python==

```
python setup.py install
```

<p></p>

###### ConfigParser模块
到 [这里](https://pypi.python.org/pypi/configparser) 下载ConfigParser，解压并进入目录，然后输入下面命令安装
```
python setup.py install
```
