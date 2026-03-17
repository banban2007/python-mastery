from mysql.connector import connect
try:
    connection = connect(host="localhost", user="root", passwd="",database="firstdb")
    cursor = connection.cursor()
    sql = "INSERT INTO Employees (id, name,salary, job_id, dept_id)\
        VALUES (%s,%s,%s,%s,%s);"
    val = [
        (2,"Kyaw Kyaw",500000,10,25),
        (3,"Mg Mg",4000,12,26),k
        (4,"Ko Ko",6000,13,27)
    ]
    cursor.executemany(sql, val)
    connection.commit()
except Exception as e:
    print(e)