from mysql.connector import connect

try:
    connection = connect(host="127.0.0.1", user="root", passwd="")
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES;")
    for i in cursor:
        print(i)
except Exception as e:
    print(e)