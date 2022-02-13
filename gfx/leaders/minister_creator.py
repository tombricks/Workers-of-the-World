#!/usr/bin/env python

from PIL import Image
import os

for folder in os.walk('.'):
    if folder[0] != ".":
        print(folder[0])
