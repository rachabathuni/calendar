#!/usr/bin/python3

import holidays
import json

START_YEAR = 1970
END_YEAR = 2099

try:
	outfd = open("holidays.json", "w")
except Exception as e:
	print(e)
	print("Failed to open output file")
	sys.exit(1)

outputjson = []
us_holidays = holidays.US()

for year in range(START_YEAR, END_YEAR+1):
	for month in range(1, 13):
		for day in range(1, 32):
			fmt = "%04d-%02d-%02d" % (year, month, day)
			ishol = False
			try:
				ishol = fmt in us_holidays
			except ValueError:
				continue
			if ishol:
				outputjson.append(fmt)				

outfd.write(json.dumps(outputjson))
outfd.close()


