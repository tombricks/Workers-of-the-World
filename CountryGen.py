### tombricks
### [TAG, country name (generic), adjective, ideology, capital, rrr ggg bbb, common/countries file]

countries = [
	["CAN",
	"Canada",
	"Canadian",
	"Marxism_Leninism",
	"276",
	"163 61 70",
	"Western_European",
	[],
	"Confederative Republic of Canada",
	"the Confederative Republic of Canada"]
]

from shutil import copyfile
import os.path
import codecs
FileTags  = open("common/country_tags/00_countries.txt", "a+", encoding="utf8")
FileColor = open("common/countries/colors.txt", "a+", encoding="utf8")

for country in countries:
	FileTags.write(F"\n{country[0]} = \"countries/{country[6]}.txt\" ")
	FileLoc   = open("localisation/english/countries/Country_"+country[0]+"_l_english.yml", "w", encoding="utf8")

	FileLoc.write('\ufeff')
	FileLoc.write(F"""l_english:
### Country Names and Cosmetics
 {country[0]}: "{country[1]}"
 {country[0]}_DEF: "{country[1]}"
 {country[0]}_ADJ: "{country[2]}" 
 
 {country[0]}_Hypersocialism: "{country[8]}"
 {country[0]}_Hypersocialism_DEF: "{country[9]}"
 {country[0]}_Hypersocialism_ADJ: "{country[2]}" 
 {country[0]}_Marxism_Leninism: "{country[8]}"
 {country[0]}_Marxism_Leninism_DEF: "{country[9]}"
 {country[0]}_Marxism_Leninism_ADJ: "{country[2]}" 
 {country[0]}_New_Marxism: "{country[8]}"
 {country[0]}_New_Marxism_DEF: "{country[9]}"
 {country[0]}_New_Marxism_ADJ: "{country[2]}" 
 {country[0]}_Socialism: "{country[8]}"
 {country[0]}_Socialism_DEF: "{country[9]}"
 {country[0]}_Socialism_ADJ: "{country[2]}" """)
	if "DoSSR" in country[7]:
		FileLoc.write(F"""
 
 {country[0]}_SSR: "{country[2]} Soviet Socialist Republic"
 {country[0]}_SSR_DEF: "the {country[2]} Soviet Socialist Republic"
 {country[0]}_SSR_ADJ: "{country[2]}" """)


	FileColor.write(F"""
{country[0]} = {{
	color = rgb {{ {country[5]} }}
	color_ui = rgb {{ {country[5]} }}
}}""")

	dossrcos = ""
	if "DoSSR" in country[7]:
		dossrcos = F"set_cosmetic_tag = {country[0]}_SSR\n"

	path = F"history/countries/{country[0]} - {country[1]}.txt"
	with open(path, "w", encoding="utf8") as FileHistory:
		FileHistory.write(F"""capital = {country[4]}
set_stability = 0.6
set_war_support = 0.6
{dossrcos}
# Starting tech
tech_setup_generic = yes

set_politics = {{
	ruling_party = {country[3]}
	last_election = "1.1.1"
	election_frequency = 48
	elections_allowed = yes
}}

set_popularities = {{
	{country[3]} = 100
}}
""")
	if not os.path.isfile(F"gfx/flags/{country[0]}.tga"):
		copyfile("gfx/flags/ZZZ.tga", F"gfx/flags/{country[0]}.tga")
		copyfile("gfx/flags/medium/ZZZ.tga", F"gfx/flags/medium/{country[0]}.tga")
		copyfile("gfx/flags/small/ZZZ.tga", F"gfx/flags/small/{country[0]}.tga")

FileTags.seek(0)
print(FileTags.read())
FileColor.seek(0)
print(FileColor.read())
