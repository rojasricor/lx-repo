import psycopg2

dbname = "testdb"
user = "rojasricor"
password = "password"

con = psycopg2.connect(dbname=dbname, user=user, password=password)

cur = con.cursor()
cur.execute("select * from table1")
print(cur.fetchall())
con.close()
