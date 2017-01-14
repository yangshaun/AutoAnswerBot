# -*- coding: utf8 -*-
import json
import opencc
import MySQLdb
import jieba
import jieba.posseg as pseg
# 轉繁體
def traditionalize(text):
	return opencc.convert(text, config='zhs2zht.ini').encode('utf8')
# 
def get_filtered_word(txt):
	words = pseg.cut(txt)
	allow=[]
	yes={"n","i","t"}
	for w in words:
		if str(w.flag)[0].lower() in yes and len(w.word)>1:
			allow.append(w.word)
	t=set(allow)
	c=[traditionalize(i) for i in t]
	return c

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



jieba.set_dictionary('dict.txt.big')
jieba.load_userdict("NameDict_Ch_v2")
unique_set =set() #建立一個all word 的表
with open('WikiJson.json', 'r') as f:
	JsonList = json.load(f)
	dict_id_content = dict()#紀錄每一篇的id跟content
	#過濾掉重要的磁性
	for each in JsonList:
		content=each['content']+" "+each['title']
		bag_word=get_filtered_word(content)
			 #對content cut
		allowStr=str()
		for word in bag_word:
				allowStr+=(" "+word)
				unique_set.add(word)
		dict_id_content[each['id']]= allowStr	
		print dict_id_content[each['id']]
		sql = "INSERT INTO Rawdata (id,content) VALUES ('"+str(each['id'])+"','"+allowStr+"')"
		dbuse.runInsert(sql)

dbuse.dbClose()

# ================
with open('unique_words.txt','w') as w:
	for each in unique_set:
		w.write(each+" ")
		w.flush()
print "finished !"