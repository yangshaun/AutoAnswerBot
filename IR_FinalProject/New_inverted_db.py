# -*- coding: utf8 -*-
import json
import MySQLdb
import jieba
import jieba.posseg as pseg
# def traditionalize(text):
# 	return opencc.convert(text, config='zhs2zht.ini').encode('utf8')
# 
def get_filtered_word(txt):
	words = pseg.cut(txt)
	allow=set()
	yes={"n","i","t"}
	for w in words:
		if str(w.flag)[0].lower() in yes and len(w.word)>1:
			allow.add(w.word.lower())
	c=[i for i in allow ] 
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
	def runInsert(self, sql,arrayx):
		self.cursor.executemany(sql,arrayx)
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

# ================DB
jieba.load_userdict('dict.txt.big')
jieba.load_userdict("NameDict_Ch_v2")
count =1
uniqueword_dict=dict()
page_count =1



with open('wiki_tw.json', 'r') as f:
	JsonList = json.load(f)
	for each in JsonList:
		page_id = each['id']
		content=each['content']+" "+each['title']
		bag_word=get_filtered_word(content)

		for sql_word in bag_word:
			uniqueword_dict.setdefault(sql_word.lower(),[]).append(page_id)
		print "==============page. ",page_count,"========= page_id =",page_id,"=============="
		page_count+=1
try:
	dbuse = DBConn()
	dbuse.dbConnect()
	word_count =0
	inverted_index=dict()
	len_uni=len(uniqueword_dict)
	tatol = 0
	Manyrow=[]
 	for key, array in uniqueword_dict.iteritems():
 		print key.encode('utf8')
 		if word_count<500 and tatol !=(len_uni-1):
 			oneRowStr=str()
 			total_str=[]
 			for indexx in uniqueword_dict[key]: #所有的Id array
 				oneRowStr+=str(indexx)+' '
 			total_str.append(key)
 			total_str.append(oneRowStr)
 			Manyrow.append(tuple(total_str))
 			# print 'time'
 			word_count+=1
 			tatol+=1
 		else:
 			oneRowStr=str()
 			total_str=[]
 			for indexx in uniqueword_dict[key]: #所有的Id array
 				oneRowStr+=str(indexx)+' '
 			total_str.append(key)
 			total_str.append(oneRowStr)
 			Manyrow.append(tuple(total_str))

			sql ="INSERT INTO LastIndex (word, id) VALUES (%s,%s)"						
			dbuse.runInsert(sql,Manyrow)
			word_count=0
			del Manyrow[:]
			print 'finish'
			tatol+=1
 	dbuse.dbClose()
 		
except MySQLdb.Error, e:
	print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])  		

	
