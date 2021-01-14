import random
import json
import requests
import html

rounds = 3

for qnum in range(rounds):
	qnum = qnum + 1
	getQ = requests.get("https://opentdb.com/api.php?amount=1")
	getQ = json.loads(getQ.text)['results'][0]

	ans = []
	for x in range(len(getQ['incorrect_answers'])):
		ans.append(html.unescape(getQ['incorrect_answers'][x]))

	ans.append(html.unescape(getQ['correct_answer']))

	ansDict = {}
	random.shuffle(ans)
	random.shuffle(ans)
	ansDict.clear()

	for x in range(len(ans)):
		p1 = chr(ord('`')+(x+1))
		p2 = ans[x]
		dict2 = {p1:p2}	
		ansDict.update(dict2)

	strQ = "\nQuestion #"+str(qnum)+": "+html.unescape(getQ['question'])+"\n\n"
	strFoot = "\n\nCategory: "+html.unescape(getQ['category'])+" | "+"Difficulty: "+getQ['difficulty'].upper()

	for k,v in ansDict.items():
		vals = k.upper() + " ) " + v
		strQ = strQ + str(vals) + "\n"

	strQ = strQ + strFoot

	print(strQ)

	while True:
		val = input("Enter your value: ")

		try:
			if ansDict[val] == getQ['correct_answer']:
				print("Correct!")
				break
			else:
				print("Nope!")
				break
		except:
			print("Incorrect Input!")
