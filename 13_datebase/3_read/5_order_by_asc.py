from mysql.connector import connect
try:
    connection = connect(host="localhost", user="root", passwd="",database="firstdb")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Employees ORDER BY id;")
    result = cursor.fetchall()
    print("Id   Name    Salary   Job  Department")
    for r in result:
        print(r[0], r[1], r[2], r[3], r[4])

except Exception as e:
    print(e)