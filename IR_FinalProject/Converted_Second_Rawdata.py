# -*- coding: utf8 -*-
import MySQLdb
# ================DB 
class DBConn:
	def __init__(self):
		self.user = 'root'
		self.host = '127.0.0.1'
		self.passwd = '123'
		self.dbname = 'IR'

	def dbConnect(self):
		self.db = MySQLdb.connect(
			self.host,self.user,self.passwd,self.dbname,charset='utf8')
		self.cursor = self.db.cursor()

	# Exec SQL Query 
	def runQuery(self, sql):
		self.cursor.execute(sql)
		self.results = self.cursor.fetchall()

	# Exec SQL Insert
	def runInsert(self, sql):
		self.cursor.execute(sql)
		self.db.commit()

	# Exec SQL Update
	def runUpdate(self, sql):
		self.cursor.execute(sql)
		self.db.commit()

	# Exec SQL Delete
	def runDelete(self, sql):
		self.cursor.execute(sql)
		self.db.commit()

	# 關閉資料庫連線
	def dbClose(self):
		self.db.close()
try:
	dbuse = DBConn()
	dbuse.dbConnect()
except MySQLdb.Error, e:
	print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])  
# ================DB