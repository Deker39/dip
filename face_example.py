import db

names = []
con = db.call_db()  #вызов бв
cur = db.call_cursor(con)#вызов курсора
rows = db.select_db(cur)#выборка таблицы

for row in rows:
    print(row [:][1])
table_name='USER_NAME'
pk ='ID'
number = 2
#db.delete_db(cur,con,table_name,pk,3)
db.delete_db(cur,con,table_name,pk,number)

