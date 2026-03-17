from mysql.connector import connect

try:
    connection = connect(host="localhost", user="root", passwd="",database="firstdb")
    print(connection)
except Exception as e:
    print(e)