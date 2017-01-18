#IR Final Project Little Answering Bot

This is just an exmaple for that project, not an exactly optimal solution.

## Getting Started

### Requirement 

* Jieba
* OpenCC

### Offline Process 

1. According to the requirement of project, you need to download the json file right here [Wiki.json](https://drive.google.com/open?id=0ByoB_9NkZ9rRa3VUY25TeXRtdnM)

2. Use OpenCC to convert simple to traditional- [Tutorial](https://github.com/BYVoid/OpenCC)

	```js
	~$ opencc -i [input] -o [output]
	```

3. To get more accurate segmentated result, you need to download traditional dictionary for Jieba, and set another user dictionary for some specific word that doesn't correctly flag by Jieba. However, you just need to download the files into you current directory from [dict.txt.big](https://drive.google.com/open?id=0B4mpho8HMrxmZEczc2QzRGFuS1U) and [user_dict](https://drive.google.com/open?id=0B4mpho8HMrxmTjFVbkxkNUx3NlE)

4. Create a table in database with corresponding schema `Newindex (word,id)` and  Just execute `Inverted.py`

	```js
	~$ python Inverted.py
	```

### Answering 

1. Reside the `questions.json` from [IRFinalProject](https://github.com/UDICatNCHU/IRFinalProject) in your current directrory

2. Execute `directed_answer_from_db`

	```js
	~$ python directed_answer_from_db

	```
#### Result

	```python

	地中海  yes
	瑞士  yes
	歐洲  yes
	列支敦斯登  yes
	維尼亞  yes
	中心  yes
	奧地利  yes
	細分  yes
	部分  yes
	交界處  yes
	邊界  yes
	白朗峯  yes
	法國  yes
	阿爾卑斯山  yes
	山口  yes
	自治區  yes
	布勒  yes
	奧斯特  yes
	山脈  yes
	斯洛  yes
	德國  yes
	義大利  yes
	----------------答案------------------
	八卦山有結果
	阿爾卑斯山 有結果
	合歡山 有結果
	200. [('B', 166137.2631578964), ('A', 2.631578947368421), ('C', 2.31578947368421)]
	======================================================
	['B', 'C', 'B', 'A', 'C', 'A', 'A', 'C', 'B', 'B', 'A', 'C', 'C', 'B', 'A', 'B', 'A', 'C', 'B', 'B', 'C', 'A', 'C', 'A', 'A', 'C', 'B', 'C', 'A', 'B', 'C', 'A', 'C', 'C', 'A', 'B', 'A', 'C', 'B', 'A', 'B', 'C', 'A', 'B', 'A', 'C', 'A', 'B', 'A', 'C', 'C', 'B', 'B', 'A', 'C', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'C', 'C', 'C', 'C', 'B', 'C', 'B', 'A', 'B', 'C', 'B', 'C', 'B', 'B', 'B', 'A', 'B', 'C', 'A', 'A', 'B', 'A', 'C', 'C', 'B', 'C', 'A', 'C', 'B', 'C', 'A', 'A', 'B', 'A', 'A', 'C', 'B', 'C', 'C', 'A', 'B', 'B', 'A', 'A', 'C', 'B', 'B', 'A', 'C', 'B', 'B', 'B', 'A', 'A', 'A', 'C', 'B', 'A', 'B', 'B', 'A', 'C', 'C', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'C', 'C', 'B', 'A', 'B', 'C', 'A', 'A', 'C', 'A', 'A', 'B', 'C', 'B', 'A', 'A', 'C', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'C', 'A', 'A', 'B', 'A', 'C', 'A', 'A', 'B', 'A', 'C', 'C', 'C', 'C', 'A', 'C', 'A', 'C', 'B', 'C', 'A', 'B', 'A', 'C', 'B', 'A', 'C', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'A', 'A', 'B', 'B', 'B', 'B', 'B']

	```


## Authors

* 楊尚恩 [yangshaun](https://github.com/yangshaun)

## Acknowledgments

* Appreciate jieba library for segmentation from fxsjy.
* Appreciate that UDIC lab seniors and collaborators help me to do so.
* Thanks professor [Fan](http://web.nchu.edu.tw/~yfan/) for teaching Information Retrieval.

