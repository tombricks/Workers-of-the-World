titles = [
	["Collective", "Collective"]
]

# TRAITS
File_Traits = open("common/country_leader/01_traits.txt", "r", encoding="utf8")
File_Traits_Text = File_Traits.read()
File_Traits.close()

for title in titles:
	File_Traits_Text = File_Traits_Text.replace("	# <END OF TITLES>", F"	TITLE_{title[0]} = {{ random = no }} # {title[1]}\n	# <END OF TITLES>")

print("--- common/country_leader/01_traits.txt ---")
print(File_Traits_Text)

File_Traits = open("common/country_leader/01_traits.txt", "w", encoding="utf8")
File_Traits.write(File_Traits_Text)
File_Traits.close()

# LOCALISATION
File_Localisation = open("localisation/english/parties_l_english.yml", "r", encoding="utf8")
File_Localisation_Text = File_Localisation.read()
File_Localisation.close()

for title in titles:
	File_Localisation_Text = File_Localisation_Text.replace(" # <END OF TITLES>", F" TITLE_{title[0]}: \"{title[1]}\"\n # <END OF TITLES>")

print("--- localisation/english/parties_l_english.yml ---")
print(File_Localisation_Text)

File_Localisation = open("localisation/english/parties_l_english.yml", "w", encoding="utf8")
File_Localisation.write(File_Localisation_Text)
File_Localisation.close()

# SCRIPTED LOCALISATION
File_Scripted_Localisation = open("common/scripted_localisation/politics_scripted_localisation.txt", "r", encoding="utf8")
File_Scripted_Localisation_Text = File_Scripted_Localisation.read()
File_Scripted_Localisation.close()

for title in titles:
	File_Scripted_Localisation_Text = File_Scripted_Localisation_Text.replace("	# <END OF TITLES>", F"	text = {{ trigger = {{ has_country_leader_with_trait = TITLE_{title[0]} }} localization_key = TITLE_{title[0]} }} # {title[1]}\n	# <END OF TITLES>")

print("--- common/scripted_localisation/politics_scripted_localisation.txt ---")
print(File_Scripted_Localisation_Text)

File_File_Scripted_Localisation = open("common/scripted_localisation/politics_scripted_localisation.txt", "w", encoding="utf8")
File_File_Scripted_Localisation.write(File_Scripted_Localisation_Text)
File_File_Scripted_Localisation.close()

# SCRIPTED TRIGGERS
File_Scripted_Triggers = open("common/scripted_triggers/ideology_scripted_triggers.txt", "r", encoding="utf8")
File_Scripted_Triggers_Text = File_Scripted_Triggers.read()
File_Scripted_Triggers.close()

for title in titles:
	File_Scripted_Triggers_Text = File_Scripted_Triggers_Text.replace("# <END OF TITLES TRIGGER>", F"has_country_leader_with_trait = TITLE_{title[0]}\n		# <END OF TITLES TRIGGER>")

print("--- common/scripted_triggers/ideology_scripted_triggers.txt ---")
print(File_Scripted_Triggers_Text)

File_Scripted_Triggers = open("common/scripted_triggers/ideology_scripted_triggers.txt", "w", encoding="utf8")
File_Scripted_Triggers.write(File_Scripted_Triggers_Text)
File_Scripted_Triggers.close()