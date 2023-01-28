import mysql.connector

class Mysql_DBaccess:
    def __init__(self,host,user,password,db):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        try:
            self.connection=mysql.connector.connect(host=self.host,
                                                database=self.db,
                                                user=self.user,
                                                password=self.password)
        except:
            print("Error While connecting to the database")

    def insert_data(self,filename):
        self.filename=filename
        self.cur=self.connection.cursor()
        sql="insert into file(filename) values(%s);"
        val=(self.filename)
        self.cur.execute(sql,(val,))
        self.connection.commit()
    def search(self):
        self.cur=self.conection.cursor()
        sql="select * from file limit 0,10"
        data=self.cur.execute(sql)
        data=self.cur.fetchall()
        return data

    def SearchDB(self, file):
        self.cur=self.connection.cursor()
        sql = "select * from file where filename like '%{0}'".format(file)
        self.cur.execute(sql)
        row = self.cur.fetchone()
        if row == 0:
            return
        else:
            print(row)

dbobj=Mysql_DBaccess('localhost','root','Manjusha@17','searchfiles')
dbobj.SearchDB("C:/Hcl1/demo.txt")
#dbobj.insert_data("C:/Hcl1/demo.txt")
