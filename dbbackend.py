# dbbackend.py
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
def studentData():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        StdID text,
        Firstname text,
        Surname text,
        DoB text,
        Age text,
        Gender text,
        Address text,
        Mobile text
    )
    """)
    conn.commit()
    conn.close()

# Insert a new student record
def addStdRec(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    conn.commit()
    conn.close()

# View all student records
def viewData():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows

# Delete a student record by ID
def deleteRec(id):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Search for student records based on given parameters
def searchData(StdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?", 
                (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    conn.close()
    return rows

# Update a student record by ID
def updateData(id, StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("UPDATE student SET StdID=?, Firstname=?, Surname=?, DoB=?, Age=?, Gender=?, Address=?, Mobile=? WHERE id=?", 
                (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id))
    conn.commit()
    conn.close()
