
file = open('CONTACT.in', 'r')
s = {}
for x in file :
	if x[-1] == '\n' :
		x = x[:-1]
	s[x.lower()] = 1
s = sorted(s.keys())
for x in s :
	print(x)

