from mysql.connector import connect
try:
    connection = connect(host="localhost", user="root", passwd="",database="firstdb")
    cursor = connection.cursor()
    sql = """
        SELECT
            e.id,
            e.name,
            e.salary,
            j.name,
            d.name
        FROM Employees as e
        JOIN Jobs as j ON e.job_id=j.id
        JOIN Departments as d ON e.dept_id=d.id;
        """
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Id   Name    Salary   Job  Department")
    for r in result:
        print(r[0], r[1], r[2], r[3], r[4])

except Exception as e:
    print(e)