#!/usr/bin/env python

from PIL import Image
import os

template_file = Image.open("./leader_unknown minister.dds")
for folder in os.walk('.'):
    if folder[0] != ".":
        for orig_file_name in folder[2]:
            if not os.path.isfile((folder[0] + "\\" + orig_file_name.replace(".dds", "") + " minister.dds")) and "minister" not in orig_file_name:
                print(folder[0] + "\\" + orig_file_name)
                orig_file = Image.open(folder[0] + "\\" + orig_file_name).crop((0, 0, 155, 209))
                new_file = template_file
                paste = orig_file.resize((35, 48))
                new_file.paste(paste, (15, 9))
                #new_file.show()
                new_file.save(folder[0] + "\\" + orig_file_name.replace(".dds", "") + " minister.dds")
