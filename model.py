import mysql.connector

def connect():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "students"
    )
    return conn

conn = connect()
cur = conn.cursor()
def show_all():
    query = "select * from student order by id"
    cur.execute(query)
    result = cur.fetchall()
    data =[] 
    data.clear()
    for i in result:
        data.append(i)
    return data

def create_student(name,family,phone,address):
    query = f"insert into student (name,family,phone,address)values('{name}','{family}','{phone}','{address}')"
    cur.execute(query)
    conn.commit()
    if conn.commit():
        return True

def delete_student(id):
    q = f"delete from student where id={id}"
    cur.execute(q)
    conn.commit

def update_student(id,name,family,phone,address):
    q = f"update student set name='{name}',family='{family}',phone='{phone}',address='{address}'where id='{id}'"
    cur.execute(q)
    conn.commit