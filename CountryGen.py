### tombricks
### [TAG, country name (generic), adjective, ideology, capital, rrr ggg bbb, common/countries file]

countries = [
	["UKR", "Ukraine", "Ukrainian", "Marxism_Leninism", "202", "49 79 173", "Eastern_European", ["DoSSR"]]
]

from shutil import copyfile
import os.path
import codecs
FileTags  = open("common/country_tags/00_countries.txt", "a+", encoding="utf8")
FileColor = open("common/countries/colors.txt", "a+", encoding="utf8")

for country in countries:
	FileTags.write(F"\n{country[0]} = \"countries/{country[6]}.txt\" ")
	FileLoc   = open("localisation/english/Country_"+country[0]+"_l_english.yml", "w", encoding="utf8")

	FileLoc.write(F"""l_english:
 {country[0]}: "{country[1]}"
 {country[0]}_DEF: "{country[1]}"
 {country[0]}_ADJ: "{country[2]}" """)
	if "DoSSR" in country[7]:
		FileLoc.write(F"""l_english:
 {country[0]}_SSR: "{country[2]} Soviet Socialist Republic"
 {country[0]}_SSR_DEF: "the {country[2]} Soviet Socialist Republic"
 {country[0]}_SSR_ADJ: "{country[2]}" """)


	FileColor.write(F"""
{country[0]} = {{
	color = rgb {{ {country[5]} }}
	color_ui = rgb {{ {country[5]} }}
}}""")

	path = F"history/countries/{country[0]} - {country[1]}.txt"
	with open(path, "w", encoding="utf8") as FileHistory:import codecs
		FileHistory.write(codecs.BOM_UTF16_LE)
		FileHistory.write(F"""capital = {country[4]}
set_stability = 0.6
set_war_support = 0.6

# Starting tech
set_technology = {{
	infantry_weapons = 1
	infantry_weapons1 = 1
	tech_recon = 1
	tech_support = 1		
	tech_engineers = 1
	tech_military_police = 1
	tech_mountaineers = 1
	motorised_infantry = 1
	paratroopers = 1
	gw_artillery = 1
	interwar_antiair = 1
	gwtank = 1
	basic_light_tank = 1
	early_fighter = 1
	fighter1 = 1
	early_bomber = 1
	strategic_bomber1 = 1
	naval_bomber1 = 1
	mass_assault = 1
	fleet_in_being = 1
	fuel_silos = 1
	fuel_refining = 1
}}
if = {{
	limit = {{ not = {{ has_dlc = "Man the Guns" }} }}
	set_technology = {{
		early_submarine = 1
		basic_submarine = 1
		early_destroyer = 1
		early_light_cruiser = 1
		early_heavy_cruiser = 1
		early_battleship = 1
		early_battlecruiser = 1
		transport = 1
	}}
}}
if = {{
	limit = {{
		has_dlc = "La Resistance"
	}}
	set_technology = {{
		armored_car1 = 1
	}}
	else = {{
		set_technology = {{
			basic_naval_mines = 1
			submarine_mine_laying = 1
			early_ship_hull_light = 1
			basic_ship_hull_light = 1
			early_ship_hull_submarine = 1
			basic_ship_hull_submarine = 1
			early_ship_hull_cruiser = 1
			early_ship_hull_heavy = 1
			basic_battery = 1
			basic_light_battery = 1
			basic_torpedo = 1
			basic_depth_charges = 1
			basic_secondary_battery = 1
			mtg_transport = 1
		}}
	}}
}}

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
