import os
categories = {}
for filename in os.listdir("./history/statesvanilla"):
	if ".txt" not in filename:
		continue
	#print(filename)
	ideez = filename.replace("-", " - ").split(" ")[0]
	manpower = "1"
	provinces = []
	file = open("./history/statesvanilla/"+filename, "r", encoding="utf8")
	filetxt = file.read()
	filetxt = filetxt.replace("\n", " ")
	filetxt = filetxt.replace("=", " = ")
	filetxt = ' '.join(filetxt.split())
	categories[filename] = []
	indx = -1
	for word in filetxt.split(" "):
		indx += 1
		if word == "manpower":
			categories[filename] = filetxt.split(" ")[indx+2]

print(categories)
for x in categories:
	print(x+": "+categories[x])

	filetxt = ""
	with open("./history/states/"+x, "r", encoding="utf8") as file:
		filetxt = file.read()
	filetxt = filetxt.replace("manpower", "manpower = "+categories[x]+" #")

	with open("./history/states/"+x, "w", encoding="utf8") as file:
		file.write(filetxt)
