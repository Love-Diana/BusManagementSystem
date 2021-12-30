# BusManagementSystem
一个基于django的简易的公交管理系统

## 使用方法

### 1.安装django和pymsql

在cmd或terminal输入

```bash
pip install django

pip install pymysql
```

### 2.数据库准备

在mysql cli里输入

```
CREATE DATABASE IF NOT EXISTS djangodemo default character set utf8 COLLATE utf8_general_ci;
```

用户名和密码分别为root和123456

当然也可以用自己的数据库和用户名密码，但需要在setting里改一下

### 3.运行

进入目录，在manage.py同级的目录下在命令行下输入

```
python3 manage.py makemigrations

python3 manage.py migrate
```

如果没反应的话试试把python3换成python

成功输入后会自动按照models里的模型建立数据库的表

完成之后输入

```
python3 manage.py runserver 8888
```

就可以运行了，点击弹出的链接或者在浏览器里输入localhost:8888就可以进入系统了
