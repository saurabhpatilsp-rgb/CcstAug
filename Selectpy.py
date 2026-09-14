import mysql.connector


connection = mysql.connector.connect(
                                    host="mysql_db",
                                    port=3306,
                                    user="root",
                                    password="root123",
                                    database="student_db",
)

try:
    cursor = connection.cursor()
    cursor.execute("SELECT rollno, name FROM students ORDER BY rollno")
    for rollno, name in cursor.fetchall():
        print(f"{rollno}: {name}")
finally:
    cursor.close()
    connection.close()