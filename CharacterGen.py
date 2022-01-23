import os

characters = [
	{ # https://en.wikipedia.org/wiki/Communist_Party_of_Norway
		"tag": "NOR",
		"id": "Martin_Gunnar_Knutsen",
		"name": "Martin Gunnar Knutsen",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_Chairman", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{ # https://en.wikipedia.org/wiki/Communist_Party_of_Malta
		"tag": "MLT",
		"id": "Anthony_Vassallo",
		"name": "Anthony Vassallo",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_General_Secretary", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{ # https://en.wikipedia.org/wiki/Tudeh_Party_of_Iran
		"tag": "IRN",
		"id": "Iraj_Eskandari",
		"name": "Iraj Eskandari",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_General_Secretary", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{ # https://en.wikipedia.org/wiki/Palestine_Liberation_Organization
		"tag": "PAL",
		"id": "Yasser_Arafat",
		"name": "Yasser Arafat",
		"leaders": {
			"Socialism": [ "TITLE_Chairman", "IDEOLOGY_Arab_Socialism" ]
		},
		"advisors": {
		}
	},
	{ # https://en.wikipedia.org/wiki/Al-Jama%27a_al-Islamiyya
		"tag": "ISI",
		"id": "Omar_Abdel_Rahman",
		"name": "Omar Abdel-Rahman",
		"leaders": {
			"Reactionism": [ "TITLE_Sheikh", "IDEOLOGY_Islamism" ]
		},
		"advisors": {
		}
	},
	{ # https://en.wikipedia.org/wiki/Communist_Party_of_Turkey_(historical)
		"tag": "TUR",
		"id": "Ismail_Bilen",
		"name": "İsmail Bilen",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_General_Secretary", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{ # https://en.wikipedia.org/wiki/People%27s_Democratic_Party_of_Afghanistan
		"tag": "AFG",
		"id": "Hafizullah_Amin",
		"name": "Hafizullah Amin",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_General_Secretary", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{ # Unified Communist Party https://en.wikipedia.org/wiki/Communist_Party_of_India_(Marxist)
		"tag": "IND",
		"id": "E_M_S_Namboodiripad",
		"name": "E. M. S. Namboodiripad",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_General_Secretary", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{ # https://en.wikipedia.org/wiki/Awami_Tahreek#History
		"tag": "PAK",
		"id": "Rasul_Bux_Palejo",
		"name": "Rasul Bux Palejo",
		"leaders": {
			"New_Marxism": [ "TITLE_President", "IDEOLOGY_Marxism_Leninism_Maoism" ]
		},
		"advisors": {
		}
	},
	{ # https://en.wikipedia.org/wiki/Bangladesh_National_Awami_Party
		"tag": "BNG",
		"id": "Muzaffar_Ahmed",
		"name": "Muzaffar Ahmed",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_President", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{ # https://en.wikipedia.org/wiki/Communist_Party_of_Nepal_(Fourth_Convention)
		"tag": "NEP",
		"id": "Mohan_Bikram_Singh",
		"name": "Mohan Bikram Singh",
		"leaders": {
			"New_Marxism": [ "TITLE_General_Secretary", "IDEOLOGY_Marxism_Leninism_Maoism" ]
		},
		"advisors": {
		}
	},
	{ # a momment
		"tag": "BHU",
		"id": "Sherub_Gyeltshen",
		"name": "Sherub Gyeltshen",
		"leaders": {
			"New_Marxism": [ "TITLE_General_Secretary", "IDEOLOGY_Marxism_Leninism_Maoism" ]
		},
		"advisors": {
		}
	},
	{ # https://en.wikipedia.org/wiki/Communist_Party_of_Burma
		"tag": "BRM",
		"id": "Thakin_Ba_Thein_Tin",
		"name": "Thakin Ba Thein Tin",
		"leaders": {
			"New_Marxism": [ "TITLE_Chairman", "IDEOLOGY_Marxism_Leninism_Maoism" ]
		},
		"advisors": {
		}
	},
	{ # https://en.wikipedia.org/wiki/Lao_People%27s_Revolutionary_Party
		"tag": "LAO",
		"id": "Kaysone_Phomvihane",
		"name": "Kaysone Phomvihane",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_Chairman", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	},
	{ # https://en.wikipedia.org/wiki/Communist_Party_of_Vietnam
		"tag": "VIE",
		"id": "Ton_Duc_Thang",
		"name": "Tôn Đức Thắng",
		"leaders": {
			"Marxism_Leninism": [ "TITLE_President", "IDEOLOGY_Marxism_Leninism" ]
		},
		"advisors": {
		}
	}
]

charactersFile = ""
charactersLocalisation = ""
charactersRecruit = ""
output = True

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
