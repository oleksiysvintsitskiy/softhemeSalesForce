import re

f = open("INPUT.txt", "r")
s = f.read()

if len(s)>100:
	pass
else:
	m = re.findall(r'(0+)', s)

	f = open("OUTPUT.txt", "w")
	f.write(str(len(max(m,key=len))))
f.close()
