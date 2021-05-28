import pymysql
def mysql_connect():
    conn=pymysql.connect(host="localhost",user="root",password="Pythonprince@9.8")
    cur=conn.cursor()
    sql="CREATE DATABASE teacher"
    cur.execute(sql)
    conn.commit()
    sql=" SHOW DATABASES"
    cur.execute(sql)
    output=cur.fetchall()
    print(output)
mysql_connect()