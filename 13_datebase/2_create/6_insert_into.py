
from mysql.connector import connect
try:
    connection = connect(host="localhost", user="root", passwd="",database="firstdb")
    cursor = connection.cursor()
    sql = """
        INSERT INTO Employees (id,name,salary, job_id, dept_id)
        VALUES (1, "Kyaw Kyaw",5000,10,25);
    """
    cursor.execute(sql)
    connection.commit()
except Exception as e:
    print(e)