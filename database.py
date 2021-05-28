import pymysql
def mysqlconnect():
    conn=pymysql.connect(host="localhost",user="root",password="Pythonprince@9.8",database="company")
    cur=conn.cursor()
    sql="INSERT INTO employee(fname,mname,lname,Bdate,Address,salary,Dno,ssn)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,('vijay','t','kumar','2000-9-13','germany','25000','5','123456789'))
    conn.commit()
    sql="select * from employee"
    cur.execute(sql)
    output=cur.fetchall()
    for i in output:
        print(i)
    conn.close()
mysqlconnect()