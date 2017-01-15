IR_Final_project
=====================
IR Question answering Bot
---------------------------------------
### Main Function

* Segmentation 
* Filtering 
* Intersect the Resultants 

------------------------
For example:
```js

~$ python directed_answer_from_db.py
```

Questions:
```json
{
        "Question": "台灣搖滾樂團第一把交椅，號稱亞洲天團的五月天，他們的主唱是?",
        "A": "楊宗緯",
        "B": "阿信",
        "C": "林俊傑",
        "Answer : ": "B"
}

```

Result:
```js
========================================
臺灣  yes
搖滾樂團  yes
五月天  yes
交椅  yes
亞洲  yes
主唱  yes
天團  yes
----------------答案------------------
楊宗緯有結果
阿信 有結果
林俊傑沒有在db中有結果
3. [('B', 29326.000000000015), ('A', 4.600000000000001), ('C', 0)]

========================================

```














