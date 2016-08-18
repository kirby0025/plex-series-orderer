#!/usr/bin/python3
# -*- coding: utf-8 -*

import os #commande systeme
import glob #recherche des fichiers selon un motif

folderPath = "/home/kirby/downloads/"
folderDest = "/home/kirby/series/"
patternGlob = "*S0*"
patternSplit = ".S0"
patternSplit2 = ".s0"

list = glob.glob(folderPath+"*")
for filename in list:	
	if filename.find(patternSplit) != -1 or filename.find(patternSplit2) != -1:
		if os.path.isfile(filename):
			name,ext = os.path.splitext(filename)
			if ext == ".mkv" or ext == ".avi" or ext == ".mp4":
				p = name+ext
				path = p.split(folderPath)
				if not os.path.exists(folderDest+path[1]):
					os.symlink(filename,folderDest+path[1])
		else:
			path = filename.split(folderPath)
			if path[1].find(".S0") == -1:
				path = path[1].split(patternSplit2)
			else:
				path = path[1].split(patternSplit)
			num = path[1][:1]
			path = path[0].replace('.',' ')
			s = path+" Season "+num
			if not os.path.exists(folderDest+s):
				os.symlink(filename, folderDest+s)
files = glob.glob(folderDest+"*")
for filename in files:
    if os.path.islink(filename) and not os.path.exists(filename):
        os.remove(filename)
    else:
        continue
