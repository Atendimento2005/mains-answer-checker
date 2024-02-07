import json

cdata = []

with open("response-sheet.txt", "r") as f:

	c = 0

	lines = f.readlines()
	lines = [line.strip() for line in lines]

	i = 0
	while i < len(lines):

		line = lines[i]

		if(line.split(' ')[0] in ["Chosen", "Option", "Question", "Status"]):
			cdata.append(line.strip())
		elif line.split(" ")[0] == "Given":
			cdata.append(" ".join(lines[i:i+3])) #bring current line and next 2 lines (3 lines total) together
			i += 2 # skip next 2 linees

		i += 1

i = 0
while i < len(cdata):
	if cdata[i].split(" ")[-1] == "MCQ":
		(cdata[i+2:i+6]) = sorted(cdata[i+2:i+6], key=lambda elem: int(elem.split(" ")[-1]))
	
	if cdata[i].split(" ")[0] == "Given":
		cdata[i: i+4] = cdata[i+1:i+4] + [cdata[i]]
		i += 3


	i += 1 

with open("clean-response-sheet.txt", "w") as f:
	f.writelines([x + "\n" for x in cdata])

dout = {}

i = 0
while i < len(cdata):
	qtype = cdata[i].split(" ")[-1]
	qid = cdata[i+1].split(" ")[-1]
	qobj = {}

	if(qtype == "MCQ"):
		qobj["type"] = "MCQ"

		status = cdata[i+6].split(" ")[2]
		if status == "Answered":
			copt = int(cdata[i+7].split(" ")[-1])
			for j in range(4):
				if int(cdata[i+2+j].split(" ")[1]) == copt:
					option = j+1
					qobj["option"] = option
					qobj["status"] = "Answered"
					break
		else:
			qobj["status"] = "Not Attempted"

		dout[qid] = qobj	

		i += 7

	elif qtype == "SA":
		qobj["type"] = "Numerical"

		status = cdata[i+2].split(" ")[2]
		if status == "Answered":
			ans = int(cdata[i+3].split(" ")[-1])
			qobj["status"] = "Answered"
			qobj["option"] = ans
		else:
			qobj["status"] = "Not Attempted"

		dout[qid] = qobj
		
		i += 3

	i+=1

with open("response.json", "w") as f:
	f.write(json.dumps(dout, indent=4))