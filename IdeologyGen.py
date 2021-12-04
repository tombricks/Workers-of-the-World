ideologies = [
	#["Military_Junta", "Military Junta", "Military Junta"]
]

# TRAITS
File_Traits = open("common/country_leader/01_traits.txt", "r", encoding="utf8")
File_Traits_Text = File_Traits.read()
File_Traits.close()

for ideology in ideologies:
	File_Traits_Text = File_Traits_Text.replace("	# <END OF IDEOLOGIES>", F"	IDEOLOGY_{ideology[0]} = {{ random = no }} # {ideology[1]}\n	# <END OF IDEOLOGIES>")

print("--- common/country_leader/01_traits.txt ---")
print(File_Traits_Text)

File_Traits = open("common/country_leader/01_traits.txt", "w", encoding="utf8")
File_Traits.write(File_Traits_Text)
File_Traits.close()

# LOCALISATION
File_Localisation = open("localisation/english/parties_l_english.yml", "r", encoding="utf8")
File_Localisation_Text = File_Localisation.read()
File_Localisation.close()

for ideology in ideologies:
	File_Localisation_Text = File_Localisation_Text.replace(" # <END OF IDEOLOGIES>", F" IDEOLOGY_{ideology[0]}: \"{ideology[1]}\"\n IDEOLOGY_{ideology[0]}_ADJ: \"{ideology[2]}\"\n # <END OF IDEOLOGIES>")

print("--- localisation/english/parties_l_english.yml ---")
print(File_Localisation_Text)

File_Localisation = open("localisation/english/parties_l_english.yml", "w", encoding="utf8")
File_Localisation.write(File_Localisation_Text)
File_Localisation.close()

# SCRIPTED LOCALISATION
File_Scripted_Localisation = open("common/scripted_localisation/politics_scripted_localisation.txt", "r", encoding="utf8")
File_Scripted_Localisation_Text = File_Scripted_Localisation.read()
File_Scripted_Localisation.close()

for ideology in ideologies:
	File_Scripted_Localisation_Text = File_Scripted_Localisation_Text.replace("	# <END OF IDEOLOGIES>", F"	text = {{ trigger = {{ has_country_leader_with_trait = IDEOLOGY_{ideology[0]} }} localization_key = IDEOLOGY_{ideology[0]} }} # {ideology[1]}\n	# <END OF IDEOLOGIES>")
	File_Scripted_Localisation_Text = File_Scripted_Localisation_Text.replace("	# <END OF IDEOLOGIES ADJ>", F"	text = {{ trigger = {{ has_country_leader_with_trait = IDEOLOGY_{ideology[0]} }} localization_key = IDEOLOGY_{ideology[0]}_ADJ }} # {ideology[2]}\n	# <END OF IDEOLOGIES ADJ>")

print("--- common/scripted_localisation/politics_scripted_localisation.txt ---")
print(File_Scripted_Localisation_Text)

File_File_Scripted_Localisation = open("common/scripted_localisation/politics_scripted_localisation.txt", "w", encoding="utf8")
File_File_Scripted_Localisation.write(File_Scripted_Localisation_Text)
File_File_Scripted_Localisation.close()