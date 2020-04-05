import db

table_name='USER_NAME'
pk ='ID'
number_pk = 2
values = 'id,name,age,mail,country, language'

names = []
con = db.call_db()  #вызов бв
cur = db.call_cursor(con)#вызов курсора
rows = db.select_db(cur,table_name,values)#выборка таблицы

for row in rows:
    print(row [:][1])
#title  = 'ID,NAME,AGE,MAIL,COUNTRY,LANGUAGE'
#values = (7, 'Marina', 21, 'shluha@gmial.com', 'Russian','ukrain')

#db.insert_db(cur,con,table_name,title,values)