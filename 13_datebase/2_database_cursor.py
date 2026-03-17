from mysql.connector import connect

try:
    host = input("host: ")
    user = input("username: ")
    passwd = input("password: ")
    connection = connect(host=host, user=user,passwd=passwd)
    cursor = connection.cursor()
    print(cursor)
except Exception as e:
    print(e)