# 仅写个mysql支持
import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.70.135", "root", "123", "mysql")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()

print('mysql基础操作:', 'http://www.runoob.com/python3/python3-mysql.html')
"""
数据库可支持
GadFly
mSQL
MySQL
PostgreSQL
Microsoft SQL Server 2000
Informix
Interbase
Oracle
Sybase
"""
