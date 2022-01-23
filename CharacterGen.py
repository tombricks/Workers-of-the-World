characters = [
	{
		"tag": "CZE",
		"id": "Gustav_Husak",
		"name": "Gustáv Husák",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_First_Secretary", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "MON",
		"id": "Yumjaagiin_Tsedenbal",
		"name": "Yumjaagiin Tsedenbal",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_General_Secretary", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "AUS",
		"id": "Franz_Muhri",
		"name": "Franz Muhri",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_Chairman", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "HUN",
		"id": "Janos_Kadar",
		"name": "János Kádár",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_General_Secretary", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "ROM",
		"id": "Nicolae_Ceausescu",
		"name": "Nicolae Ceaușescu",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_General_Secretary", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "BUL",
		"id": "Todor_Zhivkov",
		"name": "Todor Zhivkov",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_First_Secretary", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "GRE",
		"id": "Charilaos_Florakis",
		"name": "Charilaos Florakis",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_Secretary_General", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "SWI",
		"id": "Gaston_Armand_Amaudruz",
		"name": "Gaston-Armand Amaudruz",
		"leaders": {
			"Reactionism": [ "TITLE_Fuhrer", "IDEOLOGY_Anti_Communism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "SPR",
		"id": "Santiago_Carrillo",
		"name": "Santiago Carrillo",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_Secretary_General", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "POR",
		"id": "Alvaro_Cunhal",
		"name": "Álvaro Cunhal",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_Secretary_General", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "IRE",
		"id": "Ruairi_O_Bradaigh",
		"name": "Ruairí Ó Bradaigh",
		"leaders": {
			"Socialism": [ "TITLE_President", "IDEOLOGY_Democratic_Socialism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "ITA",
		"id": "Enrico_Berlinguer",
		"name": "Enrico Berlinguer",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_General_Secretary", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "BEL",
		"id": "Louis_Van_Geyt",
		"name": "Louis Van Geyt",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_Chairman", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "HOL",
		"id": "Marcus_Bakker",
		"name": "Marcus Bakker",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_Chairman", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{
		"tag": "DEN",
		"id": "Jorgen_Jensen",
		"name": "Jørgen Jensen",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_Chairman", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
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

with open("characters_output.txt", "w", encoding="utf8") as file:
	file.write("--------- Localisation ---------\n")
	file.write(charactersLocalisation)
	file.write("\n---------    Recruit   ---------\n")
	file.write(charactersRecruit)
	file.write("\n---------  Characters  ---------\n")
	file.write(charactersFile)
	