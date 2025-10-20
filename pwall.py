import sys
import random as r

chrs = "0123456789/*-+"

length = 20
if len(sys.argv) == 2:
	try: length = int(sys.argv[1])
	except: length = 20
if length < 1: length = 20

print("Generating password using only the numeric block")
pwd = "".join(r.choices(chrs, k=length))
print(pwd)
