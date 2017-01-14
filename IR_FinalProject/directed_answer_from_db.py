# -*- coding: utf8 -*-
import MySQLdb
import json
import jieba
import opencc
import operator
import jieba.posseg as pseg
# #############################################
import MySQLdb
# ----------------------------------
def traditionalize(text):
	return opencc.convert(text, config='zhs2zht.ini').encode('utf8')
def get_filtered_word(txt):
	words = pseg.cut(txt)
	allow=set()
	yes={"n","i","t"}
	for w in words:
		if str(w.flag)[0].lower() in yes and len(w.word)>1:
			allow.add(traditionalize(w.word.lower().strip()))
	c=[i for i in allow ] 
	return c
# ----------------------------------


class DBConn:
  def __init__(self,second='IR'):
    self.user = 'root'
    self.host = '127.0.0.1'
    self.passwd = '123'
    self.dbname = second

  def dbConnect(self):
    self.db = MySQLdb.connect(
      self.host,self.user,self.passwd,self.dbname,charset='utf8')
    self.cursor = self.db.cursor()

  # Exec SQL Query 
  def runQuery(self, sql):
    self.cursor.execute(sql)
    return self.cursor.fetchone()

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
# #############################################
'''
看要不要寫黨 with

'''
#####################################################
FINAL_ANSWER=[]
count_all=1
jieba.load_userdict('dict.txt.big')
jieba.load_userdict("NameDict_Ch_v2")
with open('questions.json', 'r') as f:
	JsonList = json.load(f)
	for each in JsonList:
		print "=========================",count_all,". ===================================="
		question_set = dict()#每1題目自己重要的id文章
		score={"A":0,"B":0,"C":0}#每1題個選項的分數
		question=each['Question']
		a=each["A"]
		b=each["B"]
		c=each["C"]
		filtered_question=get_filtered_word(question)# segment the questions
		#=====================================抓出每一提的關鍵詞
		for each_seg in filtered_question:
			sql_str  = "select id from Newindex where word ='"+each_seg+"'"
			results=dbuse.runQuery(sql_str) #return 出來1個2d list
			if results is not None:
				print each_seg ,' yes'
				resultant=results[0].split()
				for id_question in resultant:		
					if id_question in question_set: #如果重複道題目很多id的月是重要的慈
						question_set[id_question]+=1
					else:
						question_set[id_question]=1
			else: #如果查不到的題目<-------------------------------------
					print each_seg,' NO '
		maxvalue=max(question_set.iteritems(), key=operator.itemgetter(1))[1]
		for every_key,every_value in question_set.iteritems():
			if every_value != 1 and every_value == maxvalue:
				question_set[every_key]+= len(question_set)
			else:
				if maxvalue ==0:
					continue
				else:
					question_set[every_key] = (float(int(question_set[every_key])-0)/maxvalue)
				

		
		print "----------------答案------------------"
		#=====================================抓出每一提的關鍵詞
		for e in range(3):
			if e == 0:#a
				# print a 
				sql_str  = "select id from Newindex where word ='"+a.lower().strip()+"'"
				results=dbuse.runQuery(sql_str)
				if results is not None:
					print (a+u'有結果').encode('utf8')
					resultant_a=results[0].split()
					for id_a in resultant_a:
						if id_a in question_set:
							score['A']+=question_set[id_a]
				else:
					print (a+u"沒有在db中有結果").encode('utf8')
			elif e == 1:#b
				# print b
				sql_str  = "select id from Newindex where word ='"+b.lower().strip()+"'"
				results=dbuse.runQuery(sql_str)
				if results is not None:
					print (b+u' 有結果').encode('utf8')
					resultant_b=results[0].split()
					for id_b in resultant_b:
						if id_b in question_set:
							score['B']+=question_set[id_b]
				else:
					print (b+u"沒有在db中有結果").encode('utf8')
			elif e == 2:#cs
				# print c
				sql_str  = "select id from Newindex where word ='"+c.lower().strip()+"'"
				results=dbuse.runQuery(sql_str)
				if results is not None:
					print (c+u' 有結果').encode('utf8')
					resultant_c=results[0].split()
					for id_c in resultant_c:
						if id_c in question_set:
							score['C']+=question_set[id_c]
				else:
					print (c+u"沒有在db中有結果").encode('utf8')
		# print sorted(question_set.items(),key=operator.itemgetter(1),reverse=True)[:5]
		sorted_answer=sorted(score.items(),key=operator.itemgetter(1),reverse=True)				
		print (str(count_all) +". "+str(sorted_answer)).encode('utf8')
	 	FINAL_ANSWER.append(sorted_answer[0][0])
	 	count_all+=1
	print "======================================================"
	print "======================================================"
	print FINAL_ANSWER
