
import sqlite3
def create_db():
    con=sqlite3.connect(database=r'studentmanagement.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,gender TEXT,contact INTEGER ,dob TEXT,Address TEXT,year NUMERIC ,course TEXT CHECK(LENGTH(contact)=10 AND EMAIL LIKE '%@%'))")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS faculty(department TEXT,empid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,gender TEXT,contact TEXT,dob TEXT,doj TEXT,proofType TEXT,proofNumber TEXT,Address TEXT CHECK(LENGTH(contact)=10))")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS department(dpid INTEGER PRIMARY KEY AUTOINCREMENT,departmentName TEXT)")
    con.commit()



create_db()

