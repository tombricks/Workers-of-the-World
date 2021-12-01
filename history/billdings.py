import os
build = {}
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
	buildings = False
	scopes = 0
	build[filename] = []
	indx = -1
	for word in filetxt.split(" "):
		indx += 1
		if word == "buildings":
			buildings = True
		if buildings:
			if word == "{":
				scopes += 1
			elif word == "}":
				scopes -= 1
				if scopes == 0:
					buildings = False

			build[filename].append(word)
	tempstr = ""
	for word in build[filename]:
		tempstr += word + " "
	build[filename] = tempstr

for x in build:
	print(x+": "+build[x])
	filetxt = ""
	with open("./history/states/"+x, "r", encoding="utf8") as file:
		filetxt = file.read()
	filetxt = filetxt.replace("    ", "	").replace("""buildings = {
			infrastructure = 2
			industrial_complex = 1
		}""", build[x])
	filetxt = filetxt.replace("""
		buildings = {
			infrastructure = 2
			industrial_complex = 1

		}""", build[x])
	
	with open("./history/states/"+x, "w", encoding="utf8") as file:
		file.write(filetxt)