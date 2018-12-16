
from pyhive import hive
conn = hive.Connection(host='xx', port=10000, database='xx')
cursor = conn.cursor()
cursor.execute('select * from xx limit 10')
for result in cursor.fetchall():
    print result


