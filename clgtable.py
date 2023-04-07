import pymysql

colstd=pymysql.connect(host="localhost",user="root",passwd="",database="collage")

cur=colstd.cursor()
try:
    res=cur.execute("create table info(id int,name varchar(15),mark int,dept varchar(20),fees float)")
    print("table created")
    for x in cur:
        print(x)
except:
    print("table not created")

colstd.close()
