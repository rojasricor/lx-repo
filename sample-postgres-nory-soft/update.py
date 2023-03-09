import psycopg2

dbname = "testdb"
user = "rojasricor"
password = "password"

con = psycopg2.connect(dbname=dbname, user=user, password=password)

cur = con.cursor()
cur.execute("insert into table1 values ('jun', 180)")
cur.execute("update table1 set height = 155 where name = 'hanako'")
cur.execute("delete from table1 where name = 'makoto'");
con.commit()
con.close()
