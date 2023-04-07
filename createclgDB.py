import pymysql

colstd=pymysql.connect(host="localhost",user="root",password="")

cur=colstd.cursor()

try:
    cur.execute("create database collage")
    print("database created")
    db=cur.execute("show database")
    for x in cur:
        print(x)

except:
    print("syntax error")

colstd.close()
