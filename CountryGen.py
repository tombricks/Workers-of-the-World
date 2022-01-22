### tombricks
### [TAG, country name (generic), adjective, ideology, capital, rrr ggg bbb, common/countries file]

countries = [
	{
		"tag":				"ANG",
		"name":				"Angola",
		"adj":				"Angolan",
		"ideology":			"Marxism_Leninism",
		"capital":			"540",
		"colour":			"0 102 191",
		"culture":			"African",
		"long_name":		"People's Republic of Angola",
		"long_name_def":	"the People's Republic of Angola",
		"parties":			{
			"New_Marxism": [ "MPLA", "Movimento Popular de Libertação de Angola (People's Movement for the Liberation of Angola)" ],
		},
		"characters":		{
			"Jose_Eduardo_dos_Santos": {
				"name": "José Eduardo dos Santos",
				"title": "President",
				"subideology": "Marxism_Leninism",
				"ideologies": [ "Marxism_Leninism" ]
			} 
		}
	}
]

from shutil import copyfile
import os.path
import codecs
FileTags  = open("common/country_tags/00_countries.txt", "a+", encoding="utf8")
FileColor = open("common/countries/colors.txt", "a+", encoding="utf8")

for country in countries:
	if "long_name" not in country:
		country["long_name"] = country["name"]
	if "long_name_def" not in country:
		country["long_name_def"] = "the " + country["long_name"]

	FileTags.write(F'\n{country["tag"]} = "countries/{country["culture"]}.txt" ')
	FileLoc   = open("localisation/english/countries/Country_"+country["tag"]+"_l_english.yml", "w", encoding="utf8")

	FileLoc.write('\ufeff')
	FileLoc.write(F"""l_english:
### Country Names and Cosmetics
 {country["tag"]}: "{country["name"]}"
 {country["tag"]}_DEF: "{country["name"]}"
 {country["tag"]}_ADJ: "{country["adj"]}" 
 
 {country["tag"]}_Hypersocialism: "{country["long_name"]}"
 {country["tag"]}_Hypersocialism_DEF: "{country["long_name_def"]}"
 {country["tag"]}_Marxism_Leninism: "{country["long_name"]}"
 {country["tag"]}_Marxism_Leninism_DEF: "{country["long_name_def"]}"
 {country["tag"]}_New_Marxism: "{country["long_name"]}"
 {country["tag"]}_New_Marxism_DEF: "{country["long_name_def"]}"
 {country["tag"]}_Socialism: "{country["long_name"]}"
 {country["tag"]}_Socialism_DEF: "{country["long_name_def"]}"

 """)
	
	parties = {
		"Hypersocialism_party": "$Hypersocialism_party$",
		"Hypersocialism_party_long": "$Hypersocialism_party_long$",
		"Marxism_Leninism_party": "$Marxism_Leninism_party$",
		"Marxism_Leninism_party_long": "$Marxism_Leninism_party_long$",
		"New_Marxism_party": "$New_Marxism_party$",
		"New_Marxism_party_long": "$New_Marxism_party_long$",
		"Socialism_party": "$Socialism_party$",
		"Socialism_party_long": "$Socialism_party_long$",
		"Reactionism_party": "$Reactionism_party$",
		"Reactionism_party_long": "$Reactionism_party_long$"
	}

	for party in country["parties"]:
		parties[party+"_party"] = country["parties"][party][0]
		parties[party+"_party_long"] = country["parties"][party][1]
	
	for party in parties:
		FileLoc.write(F'{country["tag"]}_{party}: "{parties[party]}"\n ')

	FileColor.write(F"""
{country["tag"]} = {{
	color = rgb {{ {country["colour"]} }}
	color_ui = rgb {{ {country["colour"]} }}
}}""")

	path = F'history/countries/{country["tag"]} - {country["name"]}.txt'
	with open(path, "w", encoding="utf8") as FileHistory:
		FileHistory.write(F"""capital = {country["capital"]}
set_stability = 0.6
set_war_support = 0.6

# Starting tech
tech_setup_generic = yes

set_politics = {{
	ruling_party = {country["ideology"]}
	last_election = "1978.1.1"
	election_frequency = 48
	elections_allowed = no
}}

set_popularities = {{
	{country["ideology"]} = 100
}}

""")
		for character in country["characters"]:
			FileHistory.write(F'recruit_character = {country["tag"]}_{character}\n')
			FileLoc.write(F'\n {country["tag"]}_{character}: "{country["characters"][character]["name"]}"\n {country["tag"]}_{character}_desc: ""')

	path = F'common/characters/{country["tag"]}.txt'
	with open(path, "w", encoding="utf8") as FileCharacters:
		FileCharacters.write("characters = {")
		for character in country["characters"]:
			FileCharacters.write(F"""
	{country["tag"]}_{character} = {{
		name = {country["tag"]}_{character}

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
		
		""")
			for ideology in country["characters"][character]["ideologies"]:
				FileCharacters.write(F"""
		country_leader = {{
			ideology = {ideology}_ideology
			traits = {{ TITLE_{country["characters"][character]["title"]} IDEOLOGY_{country["characters"][character]["subideology"]} }}
			desc = {country["tag"]}_{character}_desc
		}}
""")
			FileCharacters.write("\n	}")
		FileCharacters.write("\n}")

	if not os.path.isfile(F'gfx/flags/{["tag"]}.tga'):
		copyfile("gfx/flags/ZZZ.tga", F'gfx/flags/{country["tag"]}.tga')
		copyfile("gfx/flags/medium/ZZZ.tga", F'gfx/flags/medium/{country["tag"]}.tga')
		copyfile("gfx/flags/small/ZZZ.tga", F'gfx/flags/small/{country["tag"]}.tga')

FileTags.seek(0)
print(FileTags.read())
FileColor.seek(0)
print(FileColor.read())
