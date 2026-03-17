from mysql.connector import connect
try:
    connection = connect(host="localhost", user="root", passwd="",database="firstdb")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Employees WHERE id=3;")
    connection.commit()
    for r in cursor:
        print(r)
except Exception as e:
    print(e)