
with open("words2.txt", 'r') as f:
	words = [line.rstrip() for line in f]

firstguess = "tares"
whitelist = set()
blacklist = set()
posblacklist = {0: [], 1: [], 2: [], 3: [], 4: []} # positional blacklist
res = ["", "", "", "", ""]
c = 0

while len(words) > 1:

	# print out words if less than 7 possible words left
	#if len(words) < 7:
	#	r = ""
	#	for word in words:
	#		r += word + " "
	#	print("Possible words remaining: " + r)
	curr = words[0]
	inp = input("Please input " + curr + " and enter result: ")

	# check valid input
	valid = True
	if len(inp) != 5:
		valid = False
	for letter in inp:
		if letter not in {'0', '1', '2'}:
			valid = False
	if valid == False:
		print("Not a valid input. Please try again.")
		continue

	# go through input and add to whitelist/blacklist
	for i in range(len(inp)):
		if inp[i] == "0":
			blacklist.add(curr[i])
		elif inp[i] == "1":
			whitelist.add(curr[i])
			posblacklist[i].append(curr[i]) # if yellow letter, must add letter to blacklist for this position
		elif inp[i] == "2":
			res[i] = curr[i]
			whitelist.add(curr[i])
		else:
			print("Not a valid input. Please try again.")
			continue

	# filter words from dictionary
	i = 0
	while i < len(words):

		breaked = False

		# check if word has a blacklisted letter
		for j in range(len(words[i])):
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

if len(words) < 1:
	print("No solution found.")
else:
	print("The result is: " + words[0])







