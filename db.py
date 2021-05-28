import pymysql
def mysqlconnect():
    conn=pymysql.connect(host="localhost",user="root",password="Pythonprince@9.8",database="company")
    cur=conn.cursor()
    sql="UPDATE employee set salary=50000 where ssn=123456789 "
    cur.execute(sql)
    conn.commit()
    sql="select * from employee where ssn=123456789"
    cur.execute(sql)
    output=cur.fetchall()
    for i in output:
        print(i)
    conn.close()
mysqlconnect()