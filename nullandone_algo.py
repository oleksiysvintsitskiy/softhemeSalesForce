f = open("INPUT.txt", "r")
s = f.read()

counter = 0
m = 0

if len(s)>100:
	pass
else:
	for i in s:
		if i =="1":
			if(counter>m):
				m = counter
			counter = 0
		else:
			counter+=1

	f = open("OUTPUT.txt", "w")
	f.write(str(m))
f.close()
