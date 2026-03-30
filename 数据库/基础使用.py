from pymysql import Connection
con=Connection(
    port=3306,
    host="localhost",
    user="root",
    password="20031017@",
    autocommit=True#自动确认
)
cursor=con.cursor()#游标作用类似对象
con.select_db("test")
# cursor.execute("create table test_DQ(id int,info varchar(255))")
cursor.execute("insert into test_DQ(id,info) values(3,'绿')")#插入需要确认
#con.commit()//手动确认
cursor.execute("select * from test_DQ")#查询
const=cursor.fetchall()#type:tuple#数据库输出
print(const)
con.close()