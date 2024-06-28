import mysql.connector

class conndb:
    def __init__(self):
        pass

    def queryResult(self,strsql):
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='mahasiswa')
        conn = cnx.cursor()
        conn.execute(strsql)
        result = conn.fetchall()
        return result
        pass

    def queryExecute(self, strsql):
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='mahasiswa')
        conn = cnx.cursor()
        conn.execute(strsql)
        cnx.commit()
        pass