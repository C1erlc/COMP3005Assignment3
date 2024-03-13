import psycopg,datetime

db = ""
username = ""
pw = ""

#in case database name, and postgresql username/pw differ, uses any that
#can be input by the user
if __name__ == '__main__':
    db = input("What is the name of your database?")
    username = input("What is your postgresql username?")
    pw = input("What is your postgresql password?")

#prints off all records in the student table
def getAllStudents():
    with psycopg.connect(dbname=db, user=username, password=pw) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM students")
            for record in cur:
                print(record)

#adds a new student with specified name, email, and enrollment date,
#with student ID automatically set by the table's auto increment
def addStudent(first_name:str, last_name:str, email:str, enrollment_date:str):
    lst = enrollment_date.split("/")
    date = datetime.date(int(lst[0]),int(lst[1]),int(lst[2]))
    with psycopg.connect(dbname=db, user=username, password=pw) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES(%s, %s, %s, %s);
            """,
            (first_name, last_name, email, date))
            conn.commit()
            conn.close()

#uses given student ID to update the corresponding record's email attribute
#to the one specified
def updateStudentEmail(student_id:int, new_email:str):
    with psycopg.connect(dbname=db, user=username, password=pw) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            UPDATE students
            SET email = %s
            WHERE student_id = %s;
            """,
            (new_email, student_id))
            conn.commit()
            conn.close()

#deletes the record of the student with the specified student ID
def deleteStudent(student_id:int):
    with psycopg.connect(dbname=db, user=username, password=pw) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
            conn.commit()
            conn.close()
