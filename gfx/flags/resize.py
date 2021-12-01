#!/usr/bin/env python

from PIL import Image
import os

for file in os.listdir('.'):
	print(file)
	if "." in file:
		if file.split('.')[1] == 'tga':
			image = Image.open(file)
			image.resize((41, 26)).save('medium/'+file)
			image.resize((10, 7)).save('small/'+file)