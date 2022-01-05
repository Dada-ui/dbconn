import pymysql

A = pymysql.connect(
    user='root',
    password='Shaik@123',
    host='localhost',
    port=3306,
    db='Qdb',
)

cus = A.cursor()