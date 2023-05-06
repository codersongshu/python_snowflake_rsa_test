import snowflake.connector

conn = snowflake.connector.connect(
  user='test_user2',
  password='Linlan1988',
  account='aq54466.ca-central-1.aws'
)

cur = conn.cursor()

cur.execute('SELECT * FROM MYDB2.MYSCHEMA.MYTABLE')

results = cur.fetchall()

print(results)