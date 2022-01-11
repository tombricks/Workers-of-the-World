characters = [
	{
		"tag": "CHI",
		"id": "Hua_Guofeng",
		"name": "Hua Guofeng",
		"leaders": {
			"New_Marxism": [ "TITLE_Chairman", "IDEOLOGY_Mao_Zedong_Thought" ]
		},
		"advisors": {
		}
	},

	{
		"tag": "CHI",
		"id": "Wang_Dongxing",
		"name": "Wang Dongxing",
		"leaders": {
			"New_Marxism": [ "TITLE_Vice_Chairman", "IDEOLOGY_Mao_Zedong_Thought" ],
			"Hypersocialism": [ "TITLE_Vice_Chairman", "IDEOLOGY_Mao_Zedong_Thought" ]
		},
		"advisors": {
			"political_advisor": [ "TITLE_Vice_Chairman" ]
		}
	}
]

charactersFile = ""
charactersLocalisation = ""
charactersRecruit = ""

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
			idea_token = {characterId}
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

with open("characters_output.txt", "w", encoding="utf8") as file:
	file.write("--------- Localisation ---------\n")
	file.write(charactersLocalisation)
	file.write("\n---------    Recruit   ---------\n")
	file.write(charactersRecruit)
	file.write("\n---------  Characters  ---------\n")
	file.write(charactersFile)
	