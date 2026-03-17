from mysql.connector import connect

try:
    connection = connect(host="127.0.0.1", user="root", passwd="")
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE FirstDB;")
except Exception as e:
    print(e)