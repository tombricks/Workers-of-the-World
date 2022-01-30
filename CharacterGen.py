import os

characters = [
	{
		"tag": "EGY",
		"id": "Kamal_el_Din_Hussein",
		"name": "Kamal el-Din Hussein",
		"leaders": {
			"Socialism": [ "TITLE_President", "IDEOLOGY_Nasserism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "SYR",
		"id": "Abdel_Hamid_al_Sarraj",
		"name": "Abdel Hamid al-Sarraj",
		"leaders": {
			"Socialism": [ "TITLE_Vice_President", "IDEOLOGY_Nasserism" ]
		},
		"advisors": {
			"influential_1": [ "TITLE_Vice_President" ]
		}
	}
]

charactersFile = ""
charactersLocalisation = ""
charactersRecruit = ""
output = False

for character in characters:
	characterId = character["tag"] + "_" + character["id"]

	charactersRecruit += "recruit_character = " + characterId + "\n"

	charactersLocalisation += F' {characterId}: "{character["name"]}"\n {characterId}_desc: ""\n'

	charactersFile += F'''	{characterId} = {{
		name = {characterId}

		allowed_civil_war = {{
		}}

		portraits = {{
			civilian = {{
				large = "GFX_Portrait_Generic_Leader"
			}}
			army = {{
				small = "GFX_idea_minister_Generic_Leader"
			}}
		}}
		
		'''
	for leader in character["leaders"]:
		traits = ""
		for trait in character["leaders"][leader]:
			traits += trait + " "
		charactersFile += F'''country_leader = {{
			ideology = {leader}_ideology
			traits = {{ {traits}}}
			desc = {characterId}_desc
		}}
		
		'''
	
	for advisor in character["advisors"]:
		traits = ""
		for trait in character["advisors"][advisor]:
			traits += trait + " "
		charactersFile += F'''advisor = {{
			slot = {advisor}
			idea_token = {characterId}_{advisor}
			allowed = {{
				original_tag = {character["tag"]}
			}}
			available = {{
			}}
			on_add = {{
				log = "[GetDateText]: [This.GetName]: Added Advisor {characterId}"
			}}
			on_remove = {{
				log = "[GetDateText]: [This.GetName]: Removed Advisor {characterId}"
			}}

			traits = {{ {traits}}}
		}}
		
		'''

	charactersFile += "\n	}\n"

	if output:
		with open("localisation/english/countries/Country_"+character["tag"]+"_l_english.yml", "a", encoding="utf8") as file:
			file.write('\n\n'+charactersLocalisation)
		
		with open("common/characters/"+character["tag"]+".txt", "a", encoding="utf8") as file:
			file.write('\ncharacters = {\n'+charactersFile+'\n}')
		
		#with open("history/characters/"+character["tag"]+".txt", "a", encoding="utf8") as file:
		#	file.write('\ncharacters = {\n'+charactersFile+'\n}')

		for filename in os.listdir("history/countries/"):
			if filename[0:3] == character["tag"]:
				with open("history/countries/"+filename, "a", encoding="utf8") as file:
					file.write("\n"+charactersRecruit)
		
		charactersLocalisation = ""
		charactersRecruit = ""
		charactersFile = ""

with open("characters_output.txt", "w", encoding="utf8") as file:
	file.write("--------- Localisation ---------\n")
	file.write(charactersLocalisation)
	file.write("\n---------    Recruit   ---------\n")
	file.write(charactersRecruit)
	file.write("\n---------  Characters  ---------\n")
	file.write(charactersFile)
