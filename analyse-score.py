import json

with open("answers.json", "r") as f:
	answers = json.load(f)

with open("response.json", "r") as f:
	responses = json.load(f)

correct = []
incorrect = []
unattempted = []

for qid in responses:
	if responses[qid]["status"] == "Answered":
		if responses[qid]["option"] == answers[qid]["answer"]:
			correct.append(qid)
		else:
			incorrect.append(qid)

	else:
		unattempted.append(qid)

print("Correct:", len(correct))
print("Incorrect:", len(incorrect))
print("Unattempted:", len(unattempted)-15)
print(f"\nMarks: {len(correct)*4}/-{len(incorrect)} = {len(correct)*4 - len(incorrect)}")

def printMistakes():
	print("\nMistakes:")
	for qid in incorrect:
		print(f"Question ID: {qid} \nYour Answer: {responses[qid]['option']} \nGiven Answer: {answers[qid]['answer']} \n")

printMistakes()
