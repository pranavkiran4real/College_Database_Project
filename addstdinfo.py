import pymysql
from pip._vendor.distlib.compat import raw_input

colstd=pymysql.connect(host="localhost",user="root",passwd="",database="collage")

cur=colstd.cursor()

try:
    id=raw_input("enter the stdID                        :")
    name=raw_input("enter the name of the student        :")
    mark=raw_input("enter the mark of the student        :")
    dept=raw_input("enter the department of the student  :")
    fees=raw_input("enter the fees paid                  :")

    sql="insert into info values(%s,%s,%s,%s,%s)"
    val=[id,name,mark,dept,fees]
    cur.execute(sql,val)
    print(cur.rowcount,"record added")
    colstd.commit()

except:
    print("syntax error")

colstd.close()
