import psycopg2

def createtable():
    conn=psycopg2.connect("dbname='data2' user='postgres' password='postgres' port='5432' host='localhost'")
    cur =conn.cursor()

    cur.execute("CREATE TABLE data( rollno INTEGER, name TEXT, marks REAL) ")

    conn.commit()
    conn.close()

createtable()
