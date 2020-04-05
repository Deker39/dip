import psycopg2

def call_db():
    con = psycopg2.connect (
        database="leyla",
        user="postgres",
        password="1111",
        host="192.168.1.6",
        port="5432"
    )
    return con

def call_cursor(con):
    cur = con.cursor ( )
    return cur

def creat_table_db(cur,con):
    cur.execute ( '''CREATE TABLE USER_PHOTO
         (ID INT PRIMARY KEY NOT NULL,
         NAME TEXT NOT NULL,
         AGE INT NOT NULL,
         MAIL CHAR(50),
         COUNTRY CHAR(50),
         LANGUAGE CHAR(50));''' )
    con.commit ( )
    con.close ( )
    print ( "Table created successfully" )

def select_db(cur):
    cur.execute ( "SELECT id,name,age,mail,country, language from USER_NAME" )
    rows = cur.fetchall ( )
    return rows

def insert_db(cur,con):
    cur.execute (
        "INSERT INTO USER_NAME (ID,NAME,AGE,MAIL,COUNTRY,LANGUAGE) VALUES (3, 'John', 18,"
        " 'bigtige@gmial.com', 'Ukrain','ukrain')" )
    con.commit()
    con.close ( )
    print("Record inserted successfully into table")


def delete_db(cur,con,table_name,pk,number):
    cur.execute ( "DELETE from %s where %s=%s" %(table_name,pk,number,) )
    con.commit ( )
    con.close ( )
    print ( "Record deleted successfully" )

def update_db(cur,con):
    cur.execute ( "UPDATE USER_NAME set AGE = 25 where ID = 2" )
    con.commit ( )
    con.close ( )
    print ( "Record updated successfully" )




