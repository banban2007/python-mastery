
from mysql.connector import connect
try:
    connection = connect(host="localhost", user="root", passwd="",database="firstdb")
    cursor = connection.cursor()
    sql = "ALTER TABLE Employees ADD dept_id varchar(20) not null;" #date add shin yin use tap har
    cursor.execute(sql)
    for r in cursor:
        print(r)
except Exception as e:
    print(e)