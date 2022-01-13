
with open("words.txt", 'r') as f:
	words = [line.rstrip() for line in f]

firstguess = "tares"
whitelist = set()
blacklist = set()
posblacklist = {0: [], 1: [], 2: [], 3: [], 4: []}
res = ["", "", "", "", ""]
c = 0
# for word in words:
# 	print(word, c)
# 	c += 1

while len(words) > 1:
	curr = words[0]
	inp = input("Please input " + curr + " and enter result: ")
	for i in range(len(inp)):
		if inp[i] == "0":
			blacklist.add(curr[i])
		elif inp[i] == "1":
			whitelist.add(curr[i])
			print(i, curr[i])
			posblacklist[i].append(curr[i])
		elif inp[i] == "2":
			res[i] = curr[i]
			whitelist.add(curr[i])
		else:
			print("Not a valid input. Please try again.")
			continue
	i = 0
	while i < len(words):
		breaked = False
		# check if word has a blacklisted letter
		if len(words) < 20:
			print(words, i)
		for j in range(len(words[i])):
			print(j)
			if words[i][j] in blacklist:
				words.pop(i)
				# i -= 1
				breaked = True
				break
		if breaked: 
			continue
		# check to make sure word contains all of whitelisted letters
		for let in whitelist:
			if let not in words[i]:
				words.pop(i)
				breaked = True
				break
		if breaked: 
			continue
		# check to make sure word has letters in established positions
		for k in range(len(res)):
			if res[k] != "":
				if res[k] != words[i][k]:
					words.pop(i)
					breaked = True
					break
		if breaked:
			continue
		# check to make sure yellow letters are not repeated
		for l in range(len(words[i])):
			if words[i][l] in posblacklist[l]:
				words.pop(i)
				breaked = True
				break
		if breaked:
			continue
		i += 1
print("The result is: " + words[0])







