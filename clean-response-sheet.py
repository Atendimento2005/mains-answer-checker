cdata = []

with open("response-sheet.txt", "r") as f:
	for line in f:
		if(line.split(' ')[0] in ["Chosen", "Option", "Question", "Status"]):
			cdata.append(line.strip())

i = 0
while i < len(cdata):
	if cdata[i].split(" ")[-1] == "MCQ":
		
	i += 1 

cdata = [x + "\n" for x in cdata]

with open("clean-response-sheet.txt", "w") as f:
	f.writelines(cdata)