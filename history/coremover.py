import os
for filename in os.listdir("."):
	if ".txt" not in filename:
		continue
	print(filename)
	ideez = filename.replace("-", " - ").split(" ")[0]
	manpower = "1"
	provinces = []
	file = open("./"+filename, "r", encoding="utf8")
	filetxt = file.read()
	filetxt = filetxt.replace("\n", " ")
	filetxt = filetxt.replace("=", " = ")
	filetxt = ' '.join(filetxt.split())
	prov = False
	manp = False
	for word in filetxt.split(" "):
		if word == "provinces":
			prov = True
		elif word == "manpower":
			manp = True
		if prov:
			if word.isdecimal():
				provinces.append(word)
			elif word == "}":
				prov = False
		if manpower:
			if word.isdecimal():
				manpower = word
				manp = False
	print(provinces)
	print(manpower)
	newf = F"""state = {{
	id = {ideez}
	name = "STATE_{ideez}"
	state_category = town
	
	resources = {{
		steel = 1
		oil = 1
		aluminium = 1
	}}

	history = {{
		owner = ZZZ
		buildings = {{
			infrastructure = 2
			industrial_complex = 1
		}}
	}}

	provinces = {{"""
	for provi in provinces:
		newf += " " + str(provi)
	newf += F""" }}

	manpower = {manpower}
	buildings_max_level_factor = 1.000
}}"""

	print(newf)
	file.close()
	file = open("./"+filename, "w", encoding="utf8")
	file.write(newf)
