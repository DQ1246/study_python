from data import record#
from file import filereader,textfilereader,jsonfilereader
from pymysql import Connection
text_record=textfilereader("2011年1月销售数据.txt")
json_record=jsonfilereader("2011年2月销售数据JSON.txt")
text_data=text_record.reader()
json_data=json_record.reader()
all_data=text_data+json_data#所有数据
con=Connection(#连接对象
    port=3306,
    host="localhost",
    user="root",
    password="20031017@",
    autocommit=True#自动确认
)
cursor=con.cursor()
con.select_db("py_sql")#选择数据库
# sql = "insert into orders(order_date,order_id,money,province) values(%s,%s,%s,%s)"
# for x in all_data:
#     cursor.execute(sql, (x.date, x.id, x.money, x.province))//运行一次，避免重复写入
cursor.execute("select * from orders")
result=cursor.fetchall()
for y in result:
    print(y)
con.close()