import json

cdata = []
dout = {}

with open("answer-key.txt", "r") as f:
	for line in f:
		if len(line) < 3: continue
		if(line[0].isdigit() and (line[2] == "." or line[1] == ".")):
			cdata.append(line.strip())

for line in cdata:
	line = line.split(" ")
	qobj = {}
	qobj["answer"] = int(line[2])
	dout[line[1].lstrip()] = qobj

with open("clean-answer-key.txt", "w") as f:
    f.writelines([line + "\n" for line in cdata])
    f.write("lmao")

with open("answers.json", "w") as f:
	f.write(json.dumps(dout, indent=4))
