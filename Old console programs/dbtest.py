import MySQLdb
con = MySQLdb.connect(host="galaxy-development.info", db="clients", user="client", passwd="galaxygin")
cur = con.cursor()
cur.execute("select * from clients")
for i in cur.fetchall():
    print i
cur.close()
con.close()
