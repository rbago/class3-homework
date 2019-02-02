#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

#if os.path.isfile(myfilename):
#	print("I have a file")
#else:
#	print("no files")

with open(myfilename, 'r') as file_handle:
	for line in file_handle.readlines():
		#reduce 2 or 3 space to 1 
		line_clean = line.replace("   "," ").replace("  "," ")
		line_clean = line_clean.strip()
		values = line_clean.split(" ")
		print(values)
		#for value in values:
			
	print("finished!")
