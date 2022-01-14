with open("newwords.txt", 'r') as f:
	words = [line.rstrip() for line in f]
	res = []
	[res.append(x) for x in words if x not in res]
	
with open("newwords_dupesremoved.txt", 'w') as g:
	for word in res:
		g.write(word + "\n")