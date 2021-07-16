import random
import json
import requests
import html


scoreFilePath = "C:/Path/To/score.txt"
#scoreFilePath = "score.txt"

rounds = 3

for qnum in range(rounds):
	input_file = open(scoreFilePath, "r")
	pScore = int(input_file.read())

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
		nScore = 0
		val = input("Enter your value: ")
		val = val.lower()
		try:
			if ansDict[val] == getQ['correct_answer']:
				print("Correct!")

				if (str(getQ['difficulty']).lower()) == "easy":
					nScore = 10
				if (str(getQ['difficulty']).lower()) == "medium":
					nScore = 25
				if (str(getQ['difficulty']).lower()) == "hard":
					nScore = 50

				pScore = pScore + nScore

				input_file = open(scoreFilePath, "w")
				input_file.write(str(pScore))
				input_file.close()

				print("Question Points", nScore)
				print("Total Points", pScore)
				break
			else:
				print("Sorry the correct answer was:", str(getQ['correct_answer']))
				break
		except:
			print("Incorrect Input!")
