import pymysql
from pip._vendor.distlib.compat import raw_input

colstd = pymysql.connect(host="localhost", user="root", passwd="", database="collage")
cur = colstd.cursor()


# find student:
class addstd:
    def add(self):
        try:

            id = raw_input("enter the stdID                        :")
            name = raw_input("enter the name of the student        :")
            mark = raw_input("enter the mark of the student        :")
            dept = raw_input("enter the department of the student  :")
            fees = raw_input("enter the fees paid                  :")

            sql = "insert into info values(%s,%s,%s,%s,%s)"
            val = [id, name, mark, dept, fees]
            cur.execute(sql, val)
            print(cur.rowcount, "record added")
            colstd.commit()

        except:
            print("syntax error")


class find(addstd):
    def fnd(self):
        try:
            fs = raw_input(
                "enter the student id to show :")  # asking the student id to show the details of the student...
            sql = "select * from info where id=%s"
            val = [fs]
            cur.execute(sql, val)
            result = cur.fetchall()
            print("id\t\tname\t\tmark\t\tdept\t\tfees")
            for x in result:
                print("%d\t%s\t%d\t%s\t%.1f" % (x[0], x[1], x[2], x[3], x[4]))
        except:
            print("error")


# change data:
class change(addstd):
    def chg(self):
        try:
            id = raw_input("enter the student id to change   :")
            dept = raw_input("enter the department to change :")
            upd = "update info set dept=%s where id=%s"
            data = [dept, id]
            cur.execute(upd, data)
            print(cur.rowcount, "record updated")
            colstd.commit()
        except:
            print("syntax error")

    # cancellation of registration:


class cancel(change):
    def can(self):
        try:
            rid = raw_input("enter the student id that u wanted to cancel  :")
            delete = "delete from info where id=%s"
            rem = [rid]
            cur.execute(delete, rem)
            print(cur.rowcount, "record successfully deleted")
            colstd.commit()
        except:
            print("deletion error")

    # view all details


class view(cancel):
    def ve(self):
        try:
            view = "select * from info"
            cur.execute(view)
            result = cur.fetchall()
            print("id\t\tname\t\tmark\t\tdept\t\tfees")
            for x in result:
                print("%d\t%s\t%d\t%s\t%.1f" % (x[0], x[1], x[2], x[3], x[4]))
        except:
            print("viewing error")


ch = 0
vw = view()
while (1):
    ch = int(input(
        "enter the choice to perform the following functions :\n 1.add student data \n 2.find student \n 3.change details \n 4.cancellation of registration \n 5.view all details \n 6.exit \nEnter Choice : "))
    if (ch == 1):
        vw.add()
    elif (ch == 2):
        vw.fnd()
    elif (ch == 3):
        vw.chg()
    elif (ch == 4):
        vw.can()
    elif (ch == 5):
        vw.ve()
    elif (ch == 6):
        exit(0)
    else:
        print("wrong choice")
