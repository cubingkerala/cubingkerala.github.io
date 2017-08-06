import urllib
import zipfile
import MySQLdb
import os

print('Connecting to MySQL...')
db = MySQLdb.connect(host="localhost", user="dany", passwd="emmaus", db="wca")
print('Connected to MySQL.')
cur1 = db.cursor()
print('Adding Kerala Cubers table...')
cur1.execute("create table KeralaCubers (id varchar(10));")
for line in open("membersID.dat","r").readlines():
	cur1.execute("insert into KeralaCubers values ('" + line[:10] + "')")
print('Added Kerala Cubers table.')
print('Closing MySQL...')
db.commit()
db.close()
print('Closed MySQL...')