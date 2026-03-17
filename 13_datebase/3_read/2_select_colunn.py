from mysql.connector import connect
try:
    connection = connect(host="localhost", user="root", passwd="",database="firstdb")
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, salary FROM Employees;")
    result = cursor.fetchall()
    for r in result:
        print(r)

except Exception as e:
    print(e)