from mysql.connector import connect
try:
    connection = connect(host="localhost", user="root", passwd="",database="firstdb")
    cursor = connection.cursor()
    sql = """
    CREATE TABLE Employees (
    id int(20) not null primary key,
    name varchar(20) not null,
    salary float not null,
    job_id int not null
    );
    """
    cursor.execute(sql)
except Exception as e:
    print(e)