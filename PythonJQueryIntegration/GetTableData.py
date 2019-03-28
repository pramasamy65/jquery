# Print Statement
print ("Get Tabele Data")

# DRDA protocol (https://en.wikipedia.org/wiki/DRDA) python database driver.
import drda

conn = drda.connect(host='localhost', database='db', port=1527)
cur = conn.cursor()
cur.execute('select * from test')
for r in cur.fetchall():
    print(r[0])
	
	