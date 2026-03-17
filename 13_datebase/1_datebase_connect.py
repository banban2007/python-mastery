from mysql.connector import connect

try:
    host = "localhost"
    user = "root"
    passwd = ""
    connection = connect(host=host, user=user,passwd=passwd)
    print(connection)
except Exception as e:
    print(e)

# <mysql.connector.connection.MySQLConnection object at 0x0000016B555C62D0>