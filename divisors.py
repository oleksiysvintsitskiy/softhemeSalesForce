from math import sqrt

n = int(input())
l=[]

for i in range(2, int(sqrt(n))+2):
	if n%i==0 and i not in l:
		l.append(i)
for i in reversed(l):
	if n/i not in l:
		l.append(int(n/i))
print(l)
