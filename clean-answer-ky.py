cdata = []

with open("answer-key.txt", "r") as f:
	for line in f:
		if len(line) < 3: continue
		if(line[1] == '.' or line[2] == '.'):
			if line[-1] == 
			cdata.append(line.strip() + "\n")

with open("clean-answer-key.txt", "w") as f:
	f.writelines(cdata)